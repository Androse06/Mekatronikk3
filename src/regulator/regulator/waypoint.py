import rclpy
from rclpy.node import Node
import gpxpy
from ngc_interfaces.msg import Waypoint, Route, Mode, Eta
from ngc_utils.qos_profiles import default_qos_profile
import numpy as np

class WaypointNode(Node):
    def __init__(self):
        super().__init__('waypoint')



        self.step_size = 0.1
        self.mode_sub       = self.create_subscription(Mode, 'mode', self.mode_callback, default_qos_profile)
        self.eta_hat_sub    = self.create_subscription(Eta, "eta_hat", self.eta_callback, default_qos_profile)

        self.waypoint_pub   = self.create_publisher(Waypoint, 'waypoint_data', default_qos_profile)
        self.route_pub      = self.create_publisher(Route, 'route', default_qos_profile)

        self.standby = False
        self.position = False
        self.sail = False
        self.track = False

        self.repeat_check = False

        self.timer = self.create_timer(self.step_size, self.step_waypoint)

        self.get_logger().info("Waypoint-node er initialisert.")

        self.debug = False


    def mode_callback(self, msg: Mode):
        self.standby = msg.standby
        self.position = msg.position
        self.sail = msg.sail
        self.track = msg.track

        if self.standby or self.sail or self.position:
            self.repeat_check = False


    def eta_callback(self, msg: Eta):
        self.eta = np.array([msg.lat, msg.lon, msg.z, msg.phi, msg.theta, msg.psi])



    def step_waypoint(self):

        if self.standby or self.sail:
            return
        
        if self.track and not self.repeat_check:
            with open('/home/adolf-fick/Documents/waypoints/routes.gpx', 'r') as gpx_file:
                gpx = gpxpy.parse(gpx_file)
            
            coordinates = []

            for route in gpx.routes:
                for point in route.points:
                    latitude = point.latitude
                    longitude = point.longitude
                    coordinates.append((latitude, longitude))

                    self.get_logger().info("****************************Route konvertert til csv*****************************************")

                    self.repeat_check = True
                    
            self.get_logger().info(f'Koordinater: {coordinates}')

def main(args=None):
    rclpy.init(args=args)
    node = WaypointNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == 'main':
    main()