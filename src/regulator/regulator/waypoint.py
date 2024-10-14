import rclpy
from rclpy.node import Node
import gpxpy
from ngc_interfaces.msg import Waypoint, Route, Mode, Eta
from ngc_utils.qos_profiles import default_qos_profile
import numpy as np
import ngc_utils.geo_utils as geo
class WaypointNode(Node):
    def __init__(self):
        super().__init__('waypoint')

        self.step_size = 0.1

        self.mode_sub       = self.create_subscription(Mode, 'mode', self.mode_callback, default_qos_profile) # Bool for Standby, position, sail, track. Jeg lagde en ny .msg i ngc_interfaces.
        self.eta_hat_sub    = self.create_subscription(Eta, "eta_hat", self.eta_callback, default_qos_profile) # Nåværende posisjon fra estimator som kan brukes til å velge når waypoint er nådd og man må bytte til neste.

        self.eta_setppoint_pub  = self.create_publisher(Eta, 'eta_waypoint_setpoint', default_qos_profile) # Eget setpoint topic for waypoint regulatoren for å forhindre konflikter med autopilot regulatoren.

        self.standby    = False
        self.position   = False
        self.sail       = False
        self.track      = False
        self.load_route = False
        
        self.coordinates = []

        self.pass_counter = 0

        self.i = 0

        self.repeat_check = False # Brukes for å unngå å indekse gpx filen flere ganger enn nødvendig. Første pass når track mode settes skal waypoints hentes ut fra den spesifiserte filen.

        self.timer = self.create_timer(self.step_size, self.step_waypoint)

        self.get_logger().info("Waypoint-node er initialisert.")

        self.debug = True


    def mode_callback(self, msg: Mode): # I ngc_hmi_autopilot sendes det setpunkter. 1 er True, alle andre er False.
        self.standby        = msg.standby
        self.position       = msg.position
        self.sail           = msg.sail
        self.track          = msg.track
        self.load_route     = msg.route

        if msg.route:
            self.repeat_check = False
            self.pass_counter = 0


    def eta_callback(self, msg: Eta):
        self.eta = np.array([msg.lat, msg.lon, msg.z, msg.phi, msg.theta, msg.psi])

    def gpx_parsing(self):

        coordinates = []
        
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
        
        self.repeat_check   = True
        self.load_route     = False
        self.i = 0

        return coordinates


    def meter_p_coordinate(self, lat, lon, v_north, v_east):
        R_earth = 6371000 # meter
        meter_per_degree_lat = 2 * np.pi * R_earth / 360

        d_lat = v_north / meter_per_degree_lat
        lat_new = lat + d_lat

        meter_per_degree_lon = meter_per_degree_lat * np.cos(np.deg2rad(lat))
        d_lon = v_east / meter_per_degree_lon
        lon_new = lon + d_lon

        return lat_new, lon_new


    def step_waypoint(self):

        if self.standby or self.sail:
            return
        
        if self.load_route and not self.repeat_check: # .gpx parsing løkke

            self.coordinates = self.gpx_parsing()
            
            if self.debug:
                self.get_logger().info(f'Waypoints: {self.pass_counter}')
                self.get_logger().info(f'Coordinates: {self.coordinates}')

        if self.track:

            if len(self.coordinates) == 0:
                self.get_logger().info('No waypoints loaded')
                self.track = False
                self.coordinates = []
                return

            waypoint = self.coordinates[self.i]

            if self.i + 1 < len(self.coordinates):
                waypoint_next = self.coordinates[self.i + 1]
            else:
                self.get_logger().info('Last waypoint reached')
                self.track = False
                return

            delta = 10

            if self.debug:
                self.get_logger().info(f'waypoint: {waypoint}, Lat: {waypoint[0]}, Lon: {waypoint[1]}')

            lat_wp1 = waypoint[0]
            lon_wp1 = waypoint[1]

            lat_wp2 = waypoint_next[0]
            lon_wp2 = waypoint_next[1]

            lat_hat = self.eta[0]
            lon_hat = self.eta[1]

            pos = np.array([lat_hat, lon_hat])

            a_vec = geo.calculate_distance_north_east(lat_wp1, lon_wp1, lat_wp2, lon_wp2) # avstand i meter
            b_vec = geo.calculate_distance_north_east(lat_wp1, lon_wp1, lat_hat, lon_hat) # avstand i meter

            a_vec_m = np.dot(((np.dot(a_vec, b_vec) / np.dot(a_vec, a_vec))), a_vec)

            pos_m = self.meter_p_coordinate(lat_wp1, lon_wp1, a_vec_m[0], a_vec_m[1])

            d_vec = geo.calculate_distance_north_east(pos[0], pos[1], pos_m[0], pos_m[1])

            d = np.sqrt(d_vec[0]**2 + d_vec[1]**2)

            if d_vec[0] < 0:
                d = -d

            psi_L = np.arctan(d/delta)

            psi_east = np.arctan2(lat_wp2 - lat_wp1, lon_wp2 - lon_wp1)
            
            psi_T = 1/2 * np.pi - psi_east
            
            if psi_T < 0:
                psi_T += 2 * np.pi

            psi_d = psi_T - psi_L

            p_distance = geo.calculate_distance_north_east(lat_wp2, lon_wp2, lat_hat, lon_hat)
            if np.sqrt(p_distance[0]**2 + p_distance[1]**2) < 10:
                self.i += 1

            eta_message = Eta()
            eta_message.psi = psi_d
            self.eta_setppoint_pub.publish(eta_message)

            if self.debug:
                self.get_logger().info(f'a merket: {a_vec_m}')
                self.get_logger().info(f'pos_m: {pos_m}')
                self.get_logger().info(f'd vec: {d_vec}')
                self.get_logger().info(f'd: {d}')
                self.get_logger().info(f'psi_L: {np.rad2deg(psi_L)}')
                self.get_logger().info(f'psi_d: {np.rad2deg(psi_d)}')
                self.get_logger().info(f'psi_T: {np.rad2deg(psi_T)}')
                self.get_logger().info(f'psi_east: {np.rad2deg(psi_east)}')


def main(args=None):
    rclpy.init(args=args)
    node = WaypointNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == 'main':
    main()


'''
TANKER:

-   Nåværende funker eta PID'en med å hente inn grader fra hmi_autopilot og konvertere til radianer, så mappper den til -pi til pi og dataene settes i psi og sendes. 
    Her har vi koordinater. Vi må finne en måte å konvertere forskjellen til koordinatene eta_hat og setpoint til grader for å kunne sende til regulatoren.
    
-   Når 'track' mode er satt bør kontroller bytte om til å høre på 'eta_waypoint_setpoint' topic og bruke disse koordinatene til å regulere.
    Her bør setpointet på førte waypoint publiseres fram til eta_hat sier at båten er innenfor en viss radius av waypointet.
    så bør den bytte til neste waypoint og så videre.

-   Som rutedata fungerer nå må man tegne ut er rute i OpenCPN og eksportere som .gpx fil. Denne filen må så legges i en mappe som kan nås av noden og indekes med gpxpy. 
    Når regulatoren mottar 'track' signal over mode topic, så skal den hente ut koordinatene fra .gpx filen og sende til regulatoren. 
    Det virker som det skal være mulig å streame dataene fra OpenCPN direkte til ROS, men jeg klarte ikke å finne ut av hvordan det må settes opp.

'''