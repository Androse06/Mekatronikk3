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
        self.max_readings = 10

        self.get_logger().info("Signalbehandlings-node er initialisert.")

    ### HEADING CALLBACK FUNKSJON ###
    def heading_callback(self, msg: HeadingDevice):

        if self.current_heading is not None:
            if msg.heading != self.current_heading:
                self.last_heading = self.current_heading
        else:
            self.last_heading = msg.heading


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
                    self.get_logger().info(f'Publiserte: filtret heading={self.current_heading}')

                # Sender ut not_valid signal dersom signal ikkje er godkjent
                else:
                    heading_filtered_msg                = HeadingDevice()
                    heading_filtered_msg.valid_signal   = False
                    self.Heading_pub.publish(heading_filtered_msg)
                    self.get_logger().info(f'Heading verdier er ikkje innanfor intervall')


    ### GNSS CALLBACK FUNKSJON ###
    def gnss_callback(self, msg: GNSS):
        if self.current_lat is not None:
            if msg.lat != self.current_lat:
                self.last_lat = self.current_lat
        else:
            self.last_lat = msg.lat
        
        if self.current_lon is not None:        
            if msg.lon != self.current_lon:
                self.last_lon = self.current_lon
        else:
            self.last_lon = msg.lon

        self.current_lat    = msg.lat
        self.current_lon    = msg.lon
        self.current_sog    = msg.sog
        self.current_cog    = msg.cog
        self.GnssState      = msg.valid_signal

        if (len(self.lat_readings) > 8) and (len(self.lon_readings) > 8):
            gnss_readings_initialized = True
        else:
            self.lat_readings = np.append(self.lat_readings, self.current_lat)
            self.lon_readings = np.append(self.lon_readings, self.current_lon)
            gnss_readings_initialized = False

        if gnss_readings_initialized:
            if self.GnssState:
                # Rekne ut variansen til målingar
                self.lat_S, self.lat_average = self.varians_kalkulator(self.lat_readings)
                self.lon_S, self.lon_average = self.varians_kalkulator(self.lon_readings)

                # Sjekker om nye verdier er innanfor intervall
                if self.check_intervall(self.current_lat, self.last_lat, self.lat_S, 2):
                    self.lat_readings = np.append(self.lat_readings, self.current_lat)
                    filtered_lat = True
                    if (len(self.lat_readings) > self.max_readings):
                        self.lat_readings = np.delete(self.lat_readings, 0)
                else:
                    filtered_lat = False
                
                if self.check_intervall(self.current_lon, self.last_lon, self.lon_S, 2):
                    self.lon_readings = np.append(self.lon_readings, self.current_lon)
                    filtered_lon = True
                    if (len(self.lon_readings) > self.max_readings):
                        self.lon_readings = np.delete(self.lon_readings, 0)
                else:
                    filtered_lon = False

                # Sjekker om begge verdiene er godkjent og publiserer
                if filtered_lat and filtered_lon:
                    gnss_filtered_msg               = GNSS()
                    gnss_filtered_msg.lat           = self.current_lat
                    gnss_filtered_msg.lon           = self.current_lon
                    gnss_filtered_msg.sog           = self.current_sog
                    gnss_filtered_msg.cog           = self.current_cog
                    gnss_filtered_msg.valid_signal  = self.GnssState
                    self.Gnss_pub.publish(gnss_filtered_msg)
                    self.get_logger().info(f'Publiserte: filtret lat={self.current_lat}, filtrert lon={self.current_lon}')
                    filtered_lat = False
                    filtered_lon = False
                
                # Sender ut not_valid signal dersom signal ikkje er godkjent
                else:
                    gnss_filtered_msg               = GNSS()
                    gnss_filtered_msg.valid_signal  = False
                    self.Gnss_pub.publish(gnss_filtered_msg)
                    self.get_logger().info(f'GNSS verdier er ikkje innanfor intervall')

                
            
        
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
    """
    def check_intervall(self, value, average, stand_avvik, toleranse):
        # Reknar ut intervall etter gitt antall standardavvik
        nedre_grense = average - (toleranse * stand_avvik)
        ovre_grense  = average + (toleranse * stand_avvik)

        if (value > nedre_grense) and (value < ovre_grense):
            return True
        else:
            return False
    """
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