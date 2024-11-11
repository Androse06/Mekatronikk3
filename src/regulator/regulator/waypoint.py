import rclpy
from rclpy.node import Node
import gpxpy
from ngc_interfaces.msg import HMI, Eta, Nu, SystemMode, TravelData, Coordinate
from ngc_utils.qos_profiles import default_qos_profile
import numpy as np
import ngc_utils.geo_utils as geo
import ngc_utils.math_utils as mu
from std_msgs.msg import String
import os
import yaml
from ament_index_python.packages import get_package_share_directory
class WaypointNode(Node):
    def __init__(self):
        super().__init__('waypoint')

        self.step_size = 0.1

        ### YAML ###
        self.declare_parameter('yaml_package_name', 'ngc_bringup')
        self.declare_parameter('control_config_file', 'config/control_config.yaml')

        yaml_package_name           = self.get_parameter('yaml_package_name').get_parameter_value().string_value
        yaml_package_path           = get_package_share_directory(yaml_package_name)
        self.control_config_path    = os.path.join(yaml_package_path, self.get_parameter('control_config_file').get_parameter_value().string_value)
        self.control_config         = self.load_yaml_file(self.control_config_path)

        ### SUB ###
        self.mode_sub               = self.create_subscription(HMI, 'hmi', self.mode_callback, default_qos_profile)
        self.eta_hat_sub            = self.create_subscription(Eta, "eta_hat", self.eta_callback, default_qos_profile)
        self.nu_hat_sub             = self.create_subscription(Nu, "nu_hat", self.nu_callback, default_qos_profile)
        self.reload_config_sub      = self.create_subscription(String, 'reload_configs', self.reload_configs_callback, default_qos_profile)

        ### PUB ###
        self.mode_pub           = self.create_publisher(HMI, 'hmi', default_qos_profile)
        self.nu_setpoint_pub    = self.create_publisher(Nu, 'nu_setpoint', default_qos_profile)
        self.eta_setpoint_pub   = self.create_publisher(Eta, 'eta_setpoint', default_qos_profile)
        self.TravelData_pub     = self.create_publisher(TravelData, 'traveldata', default_qos_profile)
        self.system_mode_pub    = self.create_publisher(SystemMode, 'system_mode', default_qos_profile)

        ### VARIABLER ###
        self.mode           = 0     # id for modus til step_wayopint(). 0=standby, 1=sail, 2=DP, 3=track
        self.load_route     = False # parcer waypoints.gpx når True og appender self.waypoint
        self.load_waypoint  = False # parcer routes.gpx når True og appender self.coordinates
        self.load_anchor    = False
        self.proximity_lock = False # låser track mode på line-of-sight når True
        self.dp_init        = True
        self.dp_counter     = 0
        self.correction     = True

        self.eta    = np.zeros(6)  # til callback
        self.nu     = np.zeros(6)   # til callback

        self.eta_psi    = 0.0   # til publish
        self.nu_u       = 0.0   # til publish
        self.theta_dp   = 0.0
        self.p_m        = np.zeros(2)
        self.push_dp    = np.zeros(2)

        self.coordinates    = []   # skal inneholde [(lat, lon), (lat, lon), ...] for wp i rute
        self.waypoint       = []      # skal inneholde [(lat, lon)] for wp til dp 

        self.i = 0 # self.i er wp i ruten den er på. når et wp i ruten er nådd kjører 'self.i += 1'

        self.timer = self.create_timer(self.step_size, self.step_waypoint)

        self.get_logger().info("Waypoint-node er initialisert.")

        self.debug = self.control_config['debug']['waypoint']

    def load_yaml_file(self, file_path):
        with open(file_path, 'r') as file:
            return yaml.safe_load(file)

    def reload_configs_callback(self, msg: String):
        self.control_config = self.load_yaml_file(self.control_config_path)
        self.get_logger().info("Waypoint-node har lastet in config!")
        
    def mode_callback(self, msg: HMI): # data fra HMI. publisher bare når det er interaksjon med HMI.
        if (self.mode != 3) and (msg.mode == 3) and (self.i > 0):
            self.proximity_lock = True

        self.mode: int              = msg.mode  # 0 = standby, 1 = sail, 2 = position, 3 = track
        self.load_route: bool       = msg.route # for track
        self.load_waypoint: bool    = msg.point # for position
        self.load_anchor: bool      = msg.anchor
        self.eta_psi: float         = msg.eta   # eta setpunkt
        self.nu_u: float            = msg.nu    # nu setpunkt

        if msg.route: # .gpx parsing løkke
            self.coordinates = self.gpx_parsing(3)
            self.i = 0 
            if self.debug >= 1:
                self.get_logger().info(f'Coordinates: {self.coordinates}')
        elif msg.point:
            waypoint = self.gpx_parsing(2)
            self.waypoint = waypoint[0]
            if self.debug >= 1:
                self.get_logger().info(f'Coordinates: {self.waypoint}')

        if msg.mode != 2 and not self.dp_init:
            self.dp_init = True

        if msg.anchor:
            self.waypoint = []
            self.waypoint.append((self.eta[0], self.eta[1]))
            self.mode_publisher(2)

        if self.debug == 1:
            self.get_logger().info(
                f'callback - mode: {msg.mode}\n'
                f'callback - route: {msg.route}\n'
                f'callback - point: {msg.point}\n'
                f'callback - eta: {msg.eta}\n'
                f'callback - nu: {msg.nu}'
            )
            
    def gpx_parsing(self, mode):
        try:
            coordinates: list[tuple[float, float]] = []

            if mode == 2:
                file_path = 'gpx_file/waypoints.gpx'
            elif mode == 3:
                file_path = 'gpx_file/routes.gpx'
                coordinates.append((self.eta[0], self.eta[1])) # waypoint 0 er startposisjonen til båten
            else:
                return

            with open(file_path, 'r') as gpx_file: # filepath må endres på avhengig av hvor .gpx filen ligger
                gpx = gpxpy.parse(gpx_file)

            if mode == 3:
                for route in gpx.routes:
                    for point in route.points:
                        lat = point.latitude
                        lon = point.longitude
                        coordinates.append((lat, lon))
            elif mode == 2:
                for waypoint in gpx.waypoints:
                    lat = waypoint.latitude
                    lon = waypoint.longitude
                    coordinates.append((lat, lon))
            else:
                return

            self.load_route     = False
            self.load_waypoint  = False
            
            return coordinates

        except FileNotFoundError:
            self.get_logger().error(f"File not found: {file_path}")
            return []
        except Exception as e:
            self.get_logger().error(f"Error parsing GPX file: {e}")
            return []    

    
    def eta_publisher(self, eta):
        eta_msg     = Eta()
        eta_msg.psi = mu.mapToPiPi(eta)
        self.eta_setpoint_pub.publish(eta_msg)
        if self.debug == 1:
            self.get_logger().info(f'psi: {eta}')

    def eta_callback(self, msg: Eta):
        self.eta = np.array([msg.lat, msg.lon, msg.z, msg.phi, msg.theta, msg.psi])

    def nu_publisher(self, nu):
        nu_msg      = Nu()
        nu_msg.u    = nu
        self.nu_setpoint_pub.publish(nu_msg)
        if self.debug == 1:
            self.get_logger().info(f'nu: {nu}')

    def nu_callback(self, msg: Nu):
        self.nu = np.array([msg.u, msg.v, msg.w, msg.p, msg.q, msg.r])

    def sys_publisher(self, mode):
        system_msg = SystemMode()
        if mode == 'auto':
            system_msg.standby_mode = False
            system_msg.auto_mode    = True
        elif mode == 'standby':
            system_msg.standby_mode = True
            system_msg.auto_mode    = False
        self.system_mode_pub.publish(system_msg)

        if self.debug == -1:
            self.get_logger().info(f'system mode pub: {system_msg}')

    def mode_publisher(self, mode):
        self.mode       = mode

        mode_msg = HMI()
        mode_msg.mode   = mode
        mode_msg.route  = False
        mode_msg.point  = False
        mode_msg.eta    = self.eta_psi
        mode_msg.nu     = self.nu_u
        self.mode_pub.publish(mode_msg)

    def traveldata_publisher(self, status):

        wp_data = []
        travel_msg = TravelData()
        
        if status == True:
            travel_msg.i        = self.i
            travel_msg.status   = True
            for wp in self.coordinates:
                coor_msg        = Coordinate()
                lat, lon        = wp
                coor_msg.lat    = lat
                coor_msg.lon    = lon
                wp_data.append(coor_msg)
            travel_msg.coordinates = wp_data
        else:
            travel_msg.status = False

        self.TravelData_pub.publish(travel_msg)

    def magnitude(self, vec):
        a = vec[0]
        b = vec[1]
        return np.sqrt(a**2 + b**2)


    def step_waypoint(self):
        self.debug = self.control_config['debug']['waypoint']

        if len(self.coordinates) > 0:
            self.traveldata_publisher(True)
        else:
            self.traveldata_publisher(False)

        if self.mode == 0: # Standby
            self.sys_publisher('standby') # Setter system mode til standby for otter interface
            self.nu_publisher(0.0)
            return

        elif self.mode == 1: # Sail
            self.sys_publisher('auto') # Setter system mode til auto for otter interface
            self.eta_publisher(self.eta_psi)
            self.nu_publisher(self.nu_u)
            return
        
        elif self.mode == 2: # DP
            self.sys_publisher('auto') # Setter system mode til auto for otter interface

            if len(self.waypoint) > 0:
                setpoint = self.waypoint
                if self.debug >= 2:
                    self.get_logger().info(
                        f'setpoint i dp mode: {setpoint}, type: {type(setpoint)}'
                    )
            else:
                self.mode_publisher(0)
                self.get_logger().info('waypoint mangler')
                return
            
            ### Nu ###
            delta       = self.control_config['waypoint']['dp']['delta']
            tanh_var    = self.control_config['waypoint']['dp']['tanh_var']
            max_nu      = self.control_config['waypoint']['dp']['max_nu']
            
            ### WP koordinat ###
            lat_set = setpoint[0]
            lon_set = setpoint[1]

            ### Båt koordinat ###
            lat_hat = self.eta[0]
            lon_hat = self.eta[1]

            if self.dp_init:
                self.lat_set = lat_set
                self.lon_set = lon_set
                self.dp_init = False

            u_vec = geo.calculate_distance_north_east(lat_hat, lon_hat, lat_set, lon_set)
            u_vec_m = geo.calculate_distance_north_east(lat_hat, lon_hat, self.lat_set, self.lon_set)

            error_m = self.magnitude(u_vec_m) - delta # 0 når båten ligger 'delta' meter unna p_m
            error = self.magnitude(u_vec) - delta # 0 når båten ligger 'delta' meter unna wp

            nu_setpoint = np.tanh(error/tanh_var) * max_nu
            nu_setpoint_m = np.tanh(error_m/tanh_var) * max_nu

            self.nu_publisher(nu_setpoint_m) # *

            ### psi ###

            psi_angle = np.arctan2(u_vec_m[1], u_vec_m[0]) # *

            psi_setpoint = (psi_angle)

            self.eta_publisher(psi_setpoint)

            dp_msg = TravelData()
            dp_msg.dp = True
            dp_msg.error = self.magnitude(u_vec)
            self.TravelData_pub.publish(dp_msg)

            if self.debug >= 2:
                self.get_logger().info(
                    f'error til wp: {error}\n'
                    f'distance (wp act): {u_vec}\n'
                    f'nu_setpoint: {nu_setpoint}\n'
                    f'psi_setpoint: {np.rad2deg(mu.mapToPiPi(psi_setpoint))}'
                )

            if self.debug <= -2:
                self.get_logger().info(
                    f'error: {error}\n'
                    f'distance (wp act): {u_vec}\n'
                    f'p_m: {self.p_m}\n'
                    f'psi_setpoint: {np.rad2deg(mu.mapToPiPi(psi_setpoint))}'
                )

            if self.dp_counter >= 1000:
                self.push_dp = geo.add_distance_to_lat_lon(lat_set, lon_set, u_vec[0], u_vec[1])
                self.lat_set = self.push_dp[0]
                self.lon_set = self.push_dp[1]
                self.dp_counter = 0
                self.correction = True
            elif error <= delta * 1.5:
                self.dp_counter += 1
                self.correction = False
                if self.debug >= 2:
                    self.get_logger().info(f'dp counter: {self.dp_counter}')
            else:
                self.lat_set = lat_set
                self.lon_set = lon_set


        elif self.mode == 3: # Waypoint step-funksjon.
            self.sys_publisher('auto') # Setter system mode til auto for otter interface

            if self.debug >= 2:
                self.get_logger().info(f'i = {self.i}')

            if len(self.coordinates) == 0: # sjekker at man har lastet inn or parset waypoints
                self.get_logger().info('No waypoints loaded')
                self.mode_publisher(0)
                self.coordinates = []
                return

            waypoint: tuple[float, float] = self.coordinates[self.i] # self.i oppdateres når båten er innenfor radiusen til waypointet (wp2).
            if self.debug >= 2:
                self.get_logger().info(f'waypoint: {waypoint}')

            if self.i < len(self.coordinates) - 1: # Definerer Wp2 når det er minst 2 waypoints igjen
                waypoint_next = self.coordinates[self.i + 1]
            elif self.i == len(self.coordinates) - 1: # når siste waypoint er nådd, så stopper track-mode. Her må det implementeres DP funksjon som skrur seg på
                self.get_logger().info('Last waypoint reached')
                if self.debug >= 0:
                    self.get_logger().info(
                        f'Siste element i coord-liste: {self.coordinates[-1]}'
                    )
                self.waypoint = self.coordinates[-1]
                self.mode_publisher(2)
                return

            ### yaml variabler ###
            delta_max       = self.control_config['waypoint']['track']['delta_max']
            delta_tanh_var  = self.control_config['waypoint']['track']['delta_tanh_var']
            LOS_dist        = self.control_config['waypoint']['track']['LOS_dist']
            nu_tanh_var     = self.control_config['waypoint']['track']['nu_tanh_var']
            wp_radius       = self.control_config['waypoint']['track']['wp_radius']

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
            pos_m: tuple[float, float] = geo.add_distance_to_lat_lon(lat_wp1, lon_wp1, a_vec_m[0], a_vec_m[1])

            ### d_vektor; vektor mellom båt og P_merket ###
            d_vec: tuple[float, float] = geo.calculate_distance_north_east(lat_hat, lon_hat, pos_m[0], pos_m[1])

            ### Kryssprodukt mellom a og d for å se om båten har passert linjen ###
            d_vec_pass_check: int = np.sign(-np.cross(a_vec, d_vec))

            ### Magnituden til d_vektor ###
            d: float = d_vec_pass_check * self.magnitude(d_vec)

            ### Radiusen som båten svinger inn mot linjen ###
            delta: float = np.tanh(p_distance/delta_tanh_var) * delta_max

            psi_L: float = np.arctan(d/delta) # angrepsvinkelen båten har på linjen

            psi_east: float = np.arctan2(lat_wp2 - lat_wp1, lon_wp2 - lon_wp1) # vinkelen til linjen med øst=0deg
            
            psi_T: float = 1/2 * np.pi - psi_east # vinkelen til linjen med nord=0deg
            
            if psi_T < 0:
                psi_T += 2 * np.pi

            psi_d: float = psi_T - psi_L # utregnet kurs; eta_setpoint for heading

            wp2_error_vec: tuple[float, float] = geo.calculate_distance_north_east(pos_m[0], pos_m[1], waypoint_next[0], waypoint_next[1])
            wp2_error: float = self.magnitude(wp2_error_vec)
            wp1_error: float = self.magnitude(b_vec)

            nu: float = abs(self.nu_u)

            if wp2_error < wp1_error: # Sakker farten nær waypoints
                nu_dynamic: float = np.tanh(wp2_error/nu_tanh_var) * nu
            elif wp2_error > wp1_error and (self.i != 0):
                nu_dynamic: float = np.tanh(wp1_error/nu_tanh_var) * nu
            else:
                nu_dynamic = nu

            self.nu_publisher(nu_dynamic)

            pos_m_wp_vec: tuple[float, float] = geo.calculate_distance_north_east(pos_m[0], pos_m[1], waypoint_next[0], waypoint_next[1])
            pos_m_wp: float = self.magnitude(pos_m_wp_vec)

            ### Låser guidingen til waypoint peiling når p_merket er innenfor en meter avstand fra WP2 ###
            if pos_m_wp < LOS_dist or self.proximity_lock:
                psi_angle: float    = np.arctan2(-p_vec[1], -p_vec[0])
                self.eta_publisher(psi_angle)
                self.proximity_lock: bool = True
                if self.debug >= 2:
                    self.get_logger().info(
                        'Waypoint guiding\n'
                        f'psi_angle = {np.rad2deg(psi_angle)}'
                    )
            else:
                self.eta_publisher(psi_d)
                if self.debug >= 2:
                    self.get_logger().info('Line guiding')

            ### Hopper til neste WP når båten er innenfor en gitt radius an nåværende WP2 ###
            if p_distance <= wp_radius: 
                self.i += 1
                self.proximity_lock = False
                if self.debug >= 2:
                    self.get_logger().info('***Next waypoint***')


            if self.debug >= 3:
                if d_vec_pass_check < 0:
                    self.get_logger().info('Line pass: True')
                elif d_vec_pass_check > 0:
                    self.get_logger().info('Line pass: False')

                self.get_logger().info(
                    f'wp nr: {self.i + 1}\n'
                    f'boat to wp distance: {p_distance}\n'
                    f'Distance between wp1 and p_m: {a_vec_m}\n'
                    f'pos_m: {pos_m}\n'
                    f'd; distance between boat and line: {d}\n'
                    f'psi_L; boat attack angle: {np.rad2deg(psi_L)}\n'
                    f'psi_T; angle - waypoint line: {np.rad2deg(psi_T)}\n'
                    f'psi_d: {np.rad2deg(psi_d)}'
                )
            return

def main(args=None):
    rclpy.init(args=args)
    node = WaypointNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == 'main':
    main()
