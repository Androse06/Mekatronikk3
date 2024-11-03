import rclpy
from rclpy.node import Node
import gpxpy
from ngc_interfaces.msg import HMI, Eta, Nu, SystemMode, TravelData, Coordinate
from ngc_utils.qos_profiles import default_qos_profile
import numpy as np
import ngc_utils.geo_utils as geo
import ngc_utils.math_utils as mu

class WaypointNode(Node):
    def __init__(self):
        super().__init__('waypoint')

        self.step_size = 0.1

        self.mode_sub       = self.create_subscription(HMI, 'hmi', self.mode_callback, default_qos_profile)
        self.eta_hat_sub    = self.create_subscription(Eta, "eta_hat", self.eta_callback, default_qos_profile)
        self.nu_hat_sub     = self.create_subscription(Nu, "nu_hat", self.nu_callback, default_qos_profile)

        self.mode_pub           = self.create_publisher(HMI, 'hmi', default_qos_profile)
        self.nu_setppoint_pub   = self.create_publisher(Nu, 'nu_setpoint', default_qos_profile)
        self.eta_setppoint_pub  = self.create_publisher(Eta, 'eta_setpoint', default_qos_profile)
        self.TravelData_pub     = self.create_publisher(TravelData, 'traveldata', default_qos_profile)
        self.system_mode_pub    = self.create_publisher(SystemMode, 'system_mode', default_qos_profile)

        self.mode           = 0
        self.load_route     = False
        self.load_waypoint  = False
        self.proximity_lock = False
        
        self.eta_psi = 0.0
        self.nu_u = 0.0

        self.coordinates = []
        self.coordinates_min = []

        self.pass_counter = 0

        self.i = 0

        self.timer = self.create_timer(self.step_size, self.step_waypoint)

        self.get_logger().info("Waypoint-node er initialisert.")

        self.debug = False
        self.debug1 = False

    def mode_callback(self, msg: HMI): # I ngc_hmi_autopilot sendes det setpunkter. 1 er True, alle andre er False.
        self.mode: int              = msg.mode # 0 = standby, 1 = sail, 2 = position, 3 = track
        self.load_route: bool       = msg.route # for track
        self.load_waypoint: bool    = msg.point # for position
        self.eta_psi: float         = msg.eta
        self.nu_u: float            = msg.nu

        if msg.route: # .gpx parsing løkke
            self.coordinates = self.gpx_parsing()
            self.i = 0
            self.pass_counter = 0
            if self.debug:
                self.get_logger().info(f'Waypoints: {self.pass_counter}')
                self.get_logger().info(f'Coordinates: {self.coordinates}')

        if self.debug1:
            self.get_logger().info(f'callback - mode: {msg.mode}')
            self.get_logger().info(f'callback - route: {msg.route}')
            self.get_logger().info(f'callback - point: {msg.point}')
            self.get_logger().info(f'callback - eta: {msg.eta}')
            self.get_logger().info(f'callback - nu: {msg.nu}')
            
    def eta_callback(self, msg: Eta):
        self.eta = np.array([msg.lat, msg.lon, msg.z, msg.phi, msg.theta, msg.psi])

    def nu_callback(self, msg: Nu):
        self.nu = np.array([msg.u, msg.v, msg.w, msg.p, msg.q, msg.r])
    
    def gpx_parsing(self):
        coordinates: list[tuple[float, float]] = [] 
        coordinates.append((self.eta[0], self.eta[1])) # waypoint 0 er startposisjonen til båten

        with open('gpx_file/routes.gpx', 'r') as gpx_file: # filepath må endres på avhengig av hvor .gpx filen ligger
            gpx = gpxpy.parse(gpx_file)
        for route in gpx.routes:
            for point in route.points:
                latitude = point.latitude
                longitude = point.longitude
                coordinates.append((latitude, longitude))
        
        self.load_route = False
        self.i = 0
        
        return coordinates
    
    def eta_publisher(self, eta):
        eta_msg = Eta()
        eta_msg.psi = eta
        self.eta_setppoint_pub.publish(eta_msg)
        if self.debug:
            self.get_logger().info(f'psi: {eta}')

    def nu_publisher(self, nu):
        nu_msg = Nu()
        nu_msg.u = nu
        self.nu_setppoint_pub.publish(nu_msg)
        if self.debug:
            self.get_logger().info(f'nu: {nu}')

    def sys_publisher(self, mode):
        system_msg = SystemMode()
        if mode == 'auto':
            system_msg.standby_mode = False
            system_msg.auto_mode    = True
        elif mode == 'standby':
            system_msg.standby_mode = True
            system_msg.auto_mode    = False
        self.system_mode_pub.publish(system_msg)

        if self.debug1:
            self.get_logger().info(f'system mode pub: {system_msg}')

    def mode_publisher(self, mode):
        self.mode       = mode

        mode_msg = HMI()
        mode_msg.mode   = mode
        mode_msg.route  = self.load_route
        mode_msg.point  = self.load_waypoint
        mode_msg.eta    = self.eta_psi
        mode_msg.nu     = self.nu_u
        self.mode_pub.publish(mode_msg)

    def traveldata_publisher(self, status):

        wp_data = []
        travel_msg = TravelData()
        
        if status == True:
            travel_msg.i                = self.i
            travel_msg.status           = True
            for wp in self.coordinates:
                coor_msg = Coordinate()
                lat, lon = wp
                coor_msg.lat = lat
                coor_msg.lon = lon
                wp_data.append(coor_msg)
            travel_msg.coordinates = wp_data
        else:
            travel_msg.status = False

        self.TravelData_pub.publish(travel_msg)

    def meter_p_coordinate(self, lat, lon, v_north, v_east): # koordinatene er gitt i grader, v_north og v_east er gitt i meter. denne brukes til å kunne plusse a_merket på wp1 for å finne posisjon_merket.
        R_earth = 6371000 # meter
        meter_per_degree_lat = 2 * np.pi * R_earth / 360

        d_lat = v_north / meter_per_degree_lat
        lat_new = lat + d_lat

        meter_per_degree_lon = meter_per_degree_lat * np.cos(np.deg2rad(lat))
        d_lon = v_east / meter_per_degree_lon
        lon_new = lon + d_lon

        return lat_new, lon_new

    def magnitude(self, vec):
        a = vec[0]
        b = vec[1]
        return np.sqrt(a**2 + b**2)


    def step_waypoint(self):

        if len(self.coordinates) > 0:
            self.traveldata_publisher(True)
        else:
            self.traveldata_publisher(False)

        if self.mode == 0: # Standby
            # Setter system mode til standby for otter interface
            self.sys_publisher('standby')
            self.nu_publisher(0.0)
            return

        elif self.mode == 1: # Sail
            # Setter system mode til auto for otter interface
            self.sys_publisher('auto')
            self.eta_publisher(self.eta_psi)
            self.nu_publisher(self.nu_u)
            return

        
        elif self.mode == 2: # Dynamisk posisjonering
            # Setter system mode til auto for otter interface
            self.sys_publisher('auto')

            if len(self.coordinates) > 0:
                setpoint = self.coordinates[-1]
            else:
                self.mode_publisher(0)
                self.get_logger().info('waypoint mangler')
                return
            
            ### Nu ###
            delta = 5
                
            lat_set = setpoint[0]
            lon_set = setpoint[1]
            lat_hat = self.eta[0]
            lon_hat = self.eta[1]

            distance = geo.calculate_distance_north_east(lat_hat, lon_hat, lat_set, lon_set)

            error = self.magnitude(distance) - delta # 0 når båten ligger 5 meter unna wp

            nu_setpoint = np.tanh(error/10) * 2

            self.nu_publisher(nu_setpoint)

            ### psi ###
            psi_angle = np.arctan2(distance[1], distance[0])

            psi_setpoint = mu.mapToPiPi(psi_angle)

            self.eta_publisher(psi_setpoint)

            if self.debug:
                self.get_logger().info(f'error: {error}')
                self.get_logger().info(f'distance: {distance}')
                self.get_logger().info(f'nu_setpoint: {nu_setpoint}')
                self.get_logger().info(f'psi_setpoint: {np.rad2deg(mu.mapToPiPi(psi_setpoint))}')


        elif self.mode == 3: # Waypoint step-funksjon.
            self.sys_publisher('auto') # Setter system mode til auto for otter interface

            if self.debug:
                self.get_logger().info(f'i = {self.i}')

            if len(self.coordinates) == 0: # sjekker at man har lastet inn or parset waypoints
                self.get_logger().info('No waypoints loaded')
                self.mode_publisher(0)
                self.coordinates = []
                return

            waypoint: tuple[float, float] = self.coordinates[self.i] # self.i oppdateres når båten er innenfor radiusen til waypointet (wp2).
            if self.debug:
                self.get_logger().info(f'waypoint: {waypoint}')

            if self.i < len(self.coordinates) - 1: # Definerer Wp2 når det er minst 2 waypoints igjen
                waypoint_next = self.coordinates[self.i + 1]
            elif self.i == len(self.coordinates) - 1: # når siste waypoint er nådd, så stopper track-mode. Her må det implementeres DP funksjon som skrur seg på
                self.get_logger().info('Last waypoint reached')
                self.mode_publisher(2)
                return


            ### Waypoint 1 - WP1 ###
            lat_wp1: float = waypoint[0]
            lon_wp1: float = waypoint[1]

            ### Waypoint 2 - WP2 ###
            lat_wp2: float = waypoint_next[0]
            lon_wp2: float = waypoint_next[1]

            ### Båtens posisjon - P ###
            lat_hat: float = self.eta[0]
            lon_hat: float = self.eta[1]

            ### Avstanden mellom båt og waypoint 2 ###
            p_vec: tuple[float, float]  = geo.calculate_distance_north_east(lat_wp2, lon_wp2, lat_hat, lon_hat)
            p_distance: float           = self.magnitude(p_vec)

            ### Avstanden mellom wayoint 1 og 2 - a ###
            a_vec: tuple[float, float] = geo.calculate_distance_north_east(lat_wp1, lon_wp1, lat_wp2, lon_wp2)

            ### Avstanden mellom waypoint 1 og båt - b ###
            b_vec: tuple[float, float] = geo.calculate_distance_north_east(lat_wp1, lon_wp1, lat_hat, lon_hat)

            ### Avstanden mellom waypoint 1 og P_merket - a_merket ###
            a_vec_m: tuple[float, float] = np.dot(((np.dot(a_vec, b_vec) / np.dot(a_vec, a_vec))), a_vec)

            ### Koordinat til P_merket ###
            pos_m: tuple[float, float] = self.meter_p_coordinate(lat_wp1, lon_wp1, a_vec_m[0], a_vec_m[1])

            ### d_vektor; vektor mellom båt og P_merket ###
            d_vec: tuple[float, float] = geo.calculate_distance_north_east(lat_hat, lon_hat, pos_m[0], pos_m[1])

            ### Kryssprodukt mellom a og d for å se om båten har passert linjen ###
            d_vec_pass_check: int = np.sign(-np.cross(a_vec, d_vec))

            ### Magnituden til d_vektor ###
            d: float = d_vec_pass_check * self.magnitude(d_vec)

            ### Radiusen som båten svinger inn mot linjen ###
            delta: float = np.tanh(p_distance/150) * 80

            psi_L: float = np.arctan(d/delta) # angrepsvinkelen båten har på linjen

            psi_east: float = np.arctan2(lat_wp2 - lat_wp1, lon_wp2 - lon_wp1) # vinkelen til linjen med øst=0deg
            
            psi_T: float = 1/2 * np.pi - psi_east # vinkelen til linjen med nord=0deg
            
            if psi_T < 0:
                psi_T += 2 * np.pi

            psi_d: float = psi_T - psi_L # utregnet kurs; eta_setpoint for heading

            wp2_error_vec: tuple[float, float] = geo.calculate_distance_north_east(pos_m[0], pos_m[1], waypoint_next[0], waypoint_next[1])
            wp2_error: float = self.magnitude(wp2_error_vec)
            wp1_error: float = self.magnitude(b_vec)

            nu: float = self.nu_u

            if wp2_error < wp1_error: # Sakker farten nær waypoints
                nu_dynamic: float = np.tanh(wp2_error/10) * nu
            elif wp2_error > wp1_error:
                nu_dynamic: float = np.tanh(wp1_error/10) * nu
                
            self.nu_publisher(nu_dynamic)

            pos_m_wp_vec: tuple[float, float] = geo.calculate_distance_north_east(pos_m[0], pos_m[1], waypoint_next[0], waypoint_next[1])
            pos_m_wp: float = self.magnitude(pos_m_wp_vec)

            ### Låser guidingen til waypoint peiling når p_merket er innenfor 50 meter av WP2 ###
            if pos_m_wp < 50 or self.proximity_lock:
                psi_angle: float = np.arctan2(-p_vec[1], -p_vec[0])
                psi_setpoint: float = mu.mapToPiPi(psi_angle)
                self.eta_publisher(psi_setpoint)
                self.proximity_lock: bool = True
                if self.debug:
                    self.get_logger().info('Waypoint guiding')
                    self.get_logger().info(f'psi_setpoint = {np.rad2deg(psi_setpoint)}')
            else:
                self.eta_publisher(psi_d)
                if self.debug:
                    self.get_logger().info('Line guiding')

            ### Hopper til neste WP når båten er innenfor 10m radius an nåværende WP2 ###
            if p_distance < 10: 
                self.i += 1
                self.proximity_lock = False
                if self.debug:
                    self.get_logger().info('***Next waypoint***')


            if self.debug:
                if d_vec_pass_check < 0:
                    self.get_logger().info('Line pass: True')
                elif d_vec_pass_check > 0:
                    self.get_logger().info('Line pass: False')
                self.get_logger().info(f'wp nr: {self.i + 1}')
                self.get_logger().info(f'boat to wp distance: {p_distance}')
                self.get_logger().info(f'Distance between wp1 and p_m: {a_vec_m}')
                self.get_logger().info(f'pos_m: {pos_m}')
                self.get_logger().info(f'd; distance between boat and line: {d}')
                self.get_logger().info(f'psi_L; boat attack angle: {np.rad2deg(psi_L)}')
                self.get_logger().info(f'psi_T; angle - waypoint line: {np.rad2deg(psi_T)}')
                self.get_logger().info(f'psi_d: {np.rad2deg(psi_d)}')
            return

def main(args=None):
    rclpy.init(args=args)
    node = WaypointNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == 'main':
    main()
