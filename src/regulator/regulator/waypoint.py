import rclpy
from rclpy.node import Node
import gpxpy
from ngc_interfaces.msg import HMI, Eta
from ngc_utils.qos_profiles import default_qos_profile
import numpy as np
import ngc_utils.geo_utils as geo
class WaypointNode(Node):
    def __init__(self):
        super().__init__('waypoint')

        self.step_size = 0.1

        self.mode_sub       = self.create_subscription(HMI, 'hmi', self.mode_callback, default_qos_profile) # Bool for Standby, position, sail, track. Jeg lagde en ny .msg i ngc_interfaces.
        self.eta_hat_sub    = self.create_subscription(Eta, "eta_hat", self.eta_callback, default_qos_profile) # Nåværende posisjon fra estimator som kan brukes til å velge når waypoint er nådd og man må bytte til neste.

        self.eta_setppoint_pub  = self.create_publisher(Eta, 'eta_waypoint_setpoint', default_qos_profile) # Eget setpoint topic for waypoint regulatoren for å forhindre konflikter med autopilot regulatoren.

        self.mode           = 0
        self.load_route     = False
        self.load_waypoint  = False
        
        self.coordinates = []
        
        self.pass_counter = 0

        self.i = 0

        self.timer = self.create_timer(self.step_size, self.step_waypoint)

        self.get_logger().info("Waypoint-node er initialisert.")

        self.debug = True


    def mode_callback(self, msg: HMI): # I ngc_hmi_autopilot sendes det setpunkter. 1 er True, alle andre er False.

        self.mode = msg.mode
        self.load_route     = msg.route
        self.load_waypoint  = msg.point

        self.i = 0

        if msg.route: # .gpx parsing løkke
            self.coordinates = self.gpx_parsing()
            self.pass_counter = 0
            if self.debug:
                self.get_logger().info(f'Waypoints: {self.pass_counter}')
                self.get_logger().info(f'Coordinates: {self.coordinates}')

    def eta_callback(self, msg: Eta):
        self.eta = np.array([msg.lat, msg.lon, msg.z, msg.phi, msg.theta, msg.psi])

    def gpx_parsing(self):

        coordinates = [] 
        
        coordinates.append((self.eta[0], self.eta[1])) # waypoint 0 er startposisjonen til båten

        with open('/home/adolf-fick/Documents/waypoints/routes.gpx', 'r') as gpx_file: # filepath må endres på avhengig av hvor .gpx filen ligger
            gpx = gpxpy.parse(gpx_file)

        for route in gpx.routes:
            for point in route.points:
                latitude = point.latitude
                longitude = point.longitude
                coordinates.append((latitude, longitude))
                if self.debug: # Den jobber seg gjennom filen og indekserer waypoints helt til alle punktene i ruten er stacket inn i coordinates arrayet.
                    #self.get_logger().info('gpx indexing pass')
                    self.pass_counter += 1
        
        self.load_route = False
        self.i = 0

        return coordinates


    def meter_p_coordinate(self, lat, lon, v_north, v_east): # koordinatene er gitt i grader, v_north og v_east er gitt i meter. denne brukes til å kunne plusse a_merket på wp1 for å finne posisjon_merket.
        R_earth = 6371000 # meter
        meter_per_degree_lat = 2 * np.pi * R_earth / 360

        d_lat = v_north / meter_per_degree_lat
        lat_new = lat + d_lat

        meter_per_degree_lon = meter_per_degree_lat * np.cos(np.deg2rad(lat))
        d_lon = v_east / meter_per_degree_lon
        lon_new = lon + d_lon

        return lat_new, lon_new


    def step_waypoint(self):

        if self.mode == 0 or self.mode == 1:
            return
        
        if self.mode == 3: # step funksjonen til waypoint regulering.

            if len(self.coordinates) == 0: # sjekker at man har lastet inn or parset waypoints
                self.get_logger().info('No waypoints loaded')
                self.mode = 0
                self.coordinates = []
                return

            waypoint = self.coordinates[self.i] # self.i oppdateres når båten er innenfor radiusen til waypointet (wp2).

            if self.i < len(self.coordinates) - 1:
                waypoint_next = self.coordinates[self.i + 1]

            elif self.i == len(self.coordinates) - 1: # når siste waypoint er nådd, så stopper track-mode. Her må det implementeres DP funksjon som skrur seg på
                self.get_logger().info('Last waypoint reached')
                self.mode = 2
                self.i = 0
                return

            delta = 20 # radiusen som båten svinger inn mot linjen

            if self.debug:
                self.get_logger().info(f'waypoint: {waypoint}, Lat: {waypoint[0]}, Lon: {waypoint[1]}')

            ### waypoint 1 ###
            lat_wp1 = waypoint[0]
            lon_wp1 = waypoint[1]

            ### waypoint 2 ###
            lat_wp2 = waypoint_next[0]
            lon_wp2 = waypoint_next[1]

            ### båtens posisjon ###
            lat_hat = self.eta[0]
            lon_hat = self.eta[1]

            ### avstanden mellom wayoint 1 og 2 ###
            a_vec = geo.calculate_distance_north_east(lat_wp1, lon_wp1, lat_wp2, lon_wp2) # avstand i meter

            ### avstanden mellom waypoint 1 og båt ###
            b_vec = geo.calculate_distance_north_east(lat_wp1, lon_wp1, lat_hat, lon_hat) # avstand i meter

            a_vec_m = np.dot(((np.dot(a_vec, b_vec) / np.dot(a_vec, a_vec))), a_vec) # a_merket

            pos_m = self.meter_p_coordinate(lat_wp1, lon_wp1, a_vec_m[0], a_vec_m[1]) # p_merket

            d_vec = geo.calculate_distance_north_east(lat_hat, lon_hat, pos_m[0], pos_m[1]) # d_vektor; vektor mellom båt og p_merket

            d_vec_pass_check = - np.cross(a_vec, d_vec) # kryssprodukt mellom a og d for å se om båten har passert linjen

            d = np.sign(d_vec_pass_check) * np.sqrt(d_vec[0]**2 + d_vec[1]**2) # magnituden til d_vektor

            psi_L = np.arctan(d/delta) # angrepsvinkelen båten har på linjen

            psi_east = np.arctan2(lat_wp2 - lat_wp1, lon_wp2 - lon_wp1) # vinkelen til linjen med øst=0deg
            
            psi_T = 1/2 * np.pi - psi_east # vinkelen til linjen med nord=0deg
            
            if psi_T < 0:
                psi_T += 2 * np.pi

            psi_d = psi_T - psi_L # utregnet kurs; eta_setpoint for heading

            p_distance = geo.calculate_distance_north_east(lat_wp2, lon_wp2, lat_hat, lon_hat)

            if np.sqrt(p_distance[0]**2 + p_distance[1]**2) < 20: # hopper til neste waypoint når båten er innenfor 20m radius an nåværende waypoint
                self.i += 1

            eta_message = Eta()
            eta_message.psi = psi_d
            self.eta_setppoint_pub.publish(eta_message)

            if self.debug:
                if d_vec_pass_check < 0:
                    self.get_logger().info('Pass: True')
                elif d_vec_pass_check > 0:
                    self.get_logger().info('Pass: False')
                
                self.get_logger().info(f'wp nr: {self.i + 1}')
                self.get_logger().info(f'båt til wp avstand: {p_distance}')
                self.get_logger().info(f'a merket; avstand fra wp1 til p_merket: {a_vec_m}')
                self.get_logger().info(f'pos_merket: {pos_m}')
                self.get_logger().info(f'd; avstand fra båt til linje: {d}')
                self.get_logger().info(f'psi_L; angrepsvinkel til båt: {np.rad2deg(psi_L)}')
                self.get_logger().info(f'psi_T; waypoint linje sin vinkel: {np.rad2deg(psi_T)}')
                self.get_logger().info(f'psi_d: {np.rad2deg(psi_d)}')

        if self.mode == 2:
            self.get_logger().info('Position mode not implemented yet')
            self.mode = 0

def main(args=None):
    rclpy.init(args=args)
    node = WaypointNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == 'main':
    main()


'''

NOTATER:

-   Som rutedata fungerer nå må man tegne ut er rute i OpenCPN og eksportere som .gpx fil. Denne filen må så legges i en mappe som kan nås av noden og indekes med gpxpy. 
    Når regulatoren mottar 'track' signal over mode topic, så skal den hente ut koordinatene fra .gpx filen og sende til regulatoren. 
    Det skal være mulig å streame dataene fra OpenCPN direkte til ROS, og bør utforskes.

-   (12.10.24 - oskar) Track mode fungerer nå, men variablen 'd' (avstanden fra båt til linje) har ikke fortegn. 
    Jeg har laget en if løkke som justerer fortegnet hvis den ser at båten har forbipasert linjen, men den feiler igjen når den må begynne å kjøre vestover.

'''