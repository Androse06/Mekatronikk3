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

        self.mode_sub       = self.create_subscription(Mode, 'mode', self.mode_callback, default_qos_profile) # Bool for Standby, position, sail, track. Jeg lagde en ny .msg i ngc_interfaces.
        self.eta_hat_sub    = self.create_subscription(Eta, "eta_hat", self.eta_callback, default_qos_profile) # Nåværende posisjon fra estimator som kan brukes til å velge når waypoint er nådd og man må bytte til neste.

        self.eta_setppoint_pub  = self.create_publisher(Eta, 'eta_waypoint_setpoint', default_qos_profile) # Eget setpoint topic for waypoint regulatoren for å forhindre konflikter med autopilot regulatoren.

        self.standby    = False
        self.position   = False
        self.sail       = False
        self.track      = False
        
        self.pass_counter = 0

        self.repeat_check = False # Brukes for å unngå å indekse gpx filen flere ganger enn nødvendig. Første pass når track mode settes skal waypoints hentes ut fra den spesifiserte filen.

        self.timer = self.create_timer(self.step_size, self.step_waypoint)

        self.get_logger().info("Waypoint-node er initialisert.")

        self.debug = True


    def mode_callback(self, msg: Mode): # I ngc_hmi_autopilot sendes det setpunkter. 1 er True, alle andre er False.
        self.standby    = msg.standby
        self.position   = msg.position
        self.sail       = msg.sail
        self.track      = msg.track

        if self.standby or self.sail or self.position:
            self.repeat_check = False
            self.pass_counter = 0


    def eta_callback(self, msg: Eta):
        self.eta = np.array([msg.lat, msg.lon, msg.z, msg.phi, msg.theta, msg.psi])



    def step_waypoint(self):

        if self.standby or self.sail:
            return
        
        if self.track and not self.repeat_check:
            with open('/home/adolf-fick/Documents/waypoints/routes.gpx', 'r') as gpx_file: # filepath må endres på avhengig av hvor .gpx filen ligger
                gpx = gpxpy.parse(gpx_file)
            
            coordinates = []

            for route in gpx.routes:
                for point in route.points:
                    latitude = point.latitude
                    longitude = point.longitude
                    coordinates.append((latitude, longitude))
                    if self.debug: # Den jobber seg gjennom filen og indekserer waypoints helt til alle punktene i ruten er stacket inn i coordinates arrayet.
                        self.get_logger().info("*************************** gpx indexing pass *****************************************")
                        self.pass_counter += 1
                    self.repeat_check = True
            
            if self.debug:
                self.get_logger().info(f'Waypoints: {self.pass_counter}')
                self.get_logger().info(f'Coordinates: {coordinates}')


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