### Signal Behandling ###
import rclpy
from rclpy.node import Node
import gpxpy
from ngc_interfaces.msg import GNSS, HeadingDevice
from ngc_utils.qos_profiles import default_qos_profile
import numpy as np
import ngc_utils.geo_utils as geo
import ngc_utils.math_utils as mu
from scipy.stats import circmean, circstd

class SignalbehandlingsNode(Node):
    def __init__(self):
        super().__init__('Signalbehandling')

        ### SUB ###
        self.Gnss_Sub       = self.create_subscription(GNSS, 'gnss_measurement', self.gnss_callback, default_qos_profile)
        self.Heading_Sub    = self.create_subscription(HeadingDevice, 'heading_measurement', self.heading_callback, default_qos_profile)
        
        ### PUB ###
        self.Gnss_pub       = self.create_publisher(GNSS, 'gnss_measurement_filtered', default_qos_profile)
        self.Heading_pub    = self.create_publisher(HeadingDevice, 'heading_measurement_filtered', default_qos_profile)

        ### VARIABLER ###
        self.current_lon        = None
        self.current_lat        = None
        self.last_lon           = None
        self.last_lat           = None
        self.current_heading    = None
        self.last_heading       = None
        self.lat_readings       = np.array([])
        self.lon_readings       = np.array([])
        self.heading_readings   = np.array([])
        self.distance_readings = np.array([])
        self.max_readings = 20

        self.get_logger().info("Signalbehandlings-node er initialisert.")



    ### HEADING CALLBACK FUNKSJON ###
    def heading_callback(self, msg: HeadingDevice):
        self.current_heading    = msg.heading
        self.current_rot        = msg.rot
        self.HeadingState       = msg.valid_signal

        self.heading_readings = np.append(self.heading_readings, self.current_heading)
        if len(self.heading_readings) > self.max_readings:
            self.heading_readings = np.delete(self.heading_readings, 0)

        if len(self.heading_readings) > 8:
            heading_readings_intalized = True
        else:
            heading_readings_intalized = False

        
        if heading_readings_intalized:
            if self.HeadingState:
                # Rekne ut variansen til målingar
                #self.heading_S, self.heading_average = self.varians_kalkulator(self.heading_readings)
                self.heading_S, self.heading_average = self.varians_kalkulator_heading(self.heading_readings)

                # Sjekker om ny verdi er innanfor intervall og publiserer
                #if self.check_intervall(self.current_heading, self.last_heading, self.heading_S, 2):
                if self.check_intervall_heading(self.current_heading, self.last_heading, self.heading_S, 2):
                    heading_filtered_msg                = HeadingDevice()
                    heading_filtered_msg.heading        = self.current_heading
                    heading_filtered_msg.rot            = self.current_rot
                    heading_filtered_msg.valid_signal   = self.HeadingState
                    self.Heading_pub.publish(heading_filtered_msg)
                    #self.get_logger().info(f'Publiserte: filtret heading={self.current_heading}')

                # Sender ut not_valid signal dersom signal ikkje er godkjent
                else:
                    heading_filtered_msg                = HeadingDevice()
                    heading_filtered_msg.valid_signal   = False
                    self.Heading_pub.publish(heading_filtered_msg)
                    #self.get_logger().info(f'Heading verdier er ikkje innanfor intervall')
        else:
            #self.get_logger().info('Samler inn heading data til filtrering')
            pass
        
        self.last_heading = self.current_heading



    ### GNSS CALLBACK FUNKSJON ###
    def gnss_callback(self, msg: GNSS):
        self.current_lat    = msg.lat
        self.current_lon    = msg.lon
        self.current_sog    = msg.sog
        self.current_cog    = msg.cog
        self.GnssState      = msg.valid_signal

        if self.last_lat is not None and self.last_lon is not None:
            delta_distance = self.calculate_distance(self.current_lat, self.current_lon, self.last_lat, self.last_lon)
        else:
            delta_distance = 0
            self.get_logger().info('Første gnss måling mottatt')
        
        self.distance_readings = np.append(self.distance_readings, delta_distance)
        if len(self.distance_readings) > self.max_readings:
            self.distance_readings = np.delete(self.distance_readings, 0)

        if (len(self.distance_readings) > 8):
            gnss_readings_initialized = True
        else:
            gnss_readings_initialized = False

        if gnss_readings_initialized:
            if self.GnssState:
                # Rekne ut variansen til målingar
                #self.lat_S, self.lat_average = self.varians_kalkulator(self.lat_readings)
                #self.lon_S, self.lon_average = self.varians_kalkulator(self.lon_readings)
                self.distance_S, self.distance_average = self.varians_kalkulator(self.distance_readings)

                if delta_distance <= (2 * self.distance_S):
                    gnss_filtered_msg               = GNSS()
                    gnss_filtered_msg.lat           = self.current_lat
                    gnss_filtered_msg.lon           = self.current_lon
                    gnss_filtered_msg.sog           = self.current_sog
                    gnss_filtered_msg.cog           = self.current_cog
                    gnss_filtered_msg.valid_signal  = self.GnssState
                    self.Gnss_pub.publish(gnss_filtered_msg)
                    #self.get_logger().info(f'Publiserte: filtret lat={self.current_lat}, filtrert lon={self.current_lon}')

                else:
                    gnss_filtered_msg               = GNSS()
                    gnss_filtered_msg.valid_signal  = False
                    self.Gnss_pub.publish(gnss_filtered_msg)
                    #self.get_logger().info('GNSS verdier er ikkje innanfor intervall')
        else:
            #self.get_logger().info('Samler inn GNSS data for å starte filtrering')
            pass
        
        self.last_lat = self.current_lat
        self.last_lon = self.current_lon

    
    def calculate_distance(self, lat1, lon1, lat2, lon2):
        # Convert degrees to radians
        lat1_rad, lon1_rad = np.radians([lat1, lon1])
        lat2_rad, lon2_rad = np.radians([lat2, lon2])

        # Haversine formula
        dlat = lat2_rad - lat1_rad
        dlon = lon2_rad - lon1_rad
        a = np.sin(dlat / 2.0)**2 + np.cos(lat1_rad) * np.cos(lat2_rad) * np.sin(dlon / 2.0)**2
        c = 2 * np.arcsin(np.sqrt(a))
        R = 6371000  # Earth radius in meters
        distance = R * c
        return distance

    ### VARIANS KALKULATOR FUNKSJON ###
    def varians_kalkulator(self, value):
        value_average   = 0
        value_sum       = 0
        value_emp_var   = 0
        value_S         = 0

        # Reknar ut gjennomsnitt
        value_average = sum(value) / len(value)

        # Reknar ut sum for emperisk varians
        for i in value:
            value_sum += (i - value_average)**2
            
        # Reknar ut empirisk varians
        value_emp_var = value_sum / (len(value) - 1)

        # Reknar ut empirisk standardavvik
        value_S = np.sqrt(value_emp_var)
    
        return value_S, value_average

    ### VARIANS KALKULATOR HEADING ###
    def varians_kalkulator_heading(self, values):
        value_average   =  circmean(values, high=np.pi, low=-np.pi)
        value_S         = circstd(values, high=np.pi, low=-np.pi)
        return value_S, value_average
    
    def vinkel_forskjell(self, angle1, angle2):
        delta = (angle1 - angle2 + np.pi) % (2 * np.pi) - np.pi
        return delta
    
    def check_intervall_heading(self, value, last_value, stand_avvik, toleranse):
        delta = self.vinkel_forskjell(value, last_value)
        limit = toleranse * stand_avvik
        return abs(delta) <= limit
    
    ### INTERVALL SJEKK FUNKSJON ###
    def check_intervall(self, value, last_value, stand_avvik, toleranse):
        # Reknar ut intervall etter gitt antall standardavvik
        nedre_grense = last_value - (toleranse * stand_avvik)
        ovre_grense  = last_value + (toleranse * stand_avvik)

        if (value > nedre_grense) and (value < ovre_grense):
            return True
        else:
            return False


def main(args=None):
    rclpy.init(args=args)
    node = SignalbehandlingsNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()