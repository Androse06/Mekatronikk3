### Signal Behandling ###
import rclpy
from rclpy.node import Node
import gpxpy
from ngc_interfaces.msg import GNSS, HeadingDevice
from ngc_utils.qos_profiles import default_qos_profile
import numpy as np
import ngc_utils.geo_utils as geo
import ngc_utils.math_utils as mu


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
        self.lat_readings       = np.array([])
        self.lon_readings       = np.array([])
        self.heading_readings   = np.array([])
        self.max_readings = 10

    ### HEADING CALLBACK FUNKSJON ###
    def heading_callback(self, msg: HeadingDevice):
        self.current_heading    = msg.heading
        self.current_rot        = msg.rot
        self.HeadingState       = msg.valid_signal

        if self.HeadingState:
            # Rekne ut variansen til målingar
            self.heading_S, self.heading_average = self.varians_kalkulator(self.heading_readings)

            # Sjekker om ny verdi er innanfor intervall og publiserer
            if self.check_intervall(self.current_heading, self.heading_average, self.heading_S, 2):
                self.heading_readings = np.append(self.heading_readings, self.current_heading)
                
                heading_filtered_msg                = HeadingDevice()
                heading_filtered_msg.heading        = self.current_heading
                heading_filtered_msg.rot            = self.current_rot
                heading_filtered_msg.HeadingState   = self.HeadingState
                self.Heading_pub.publish(heading_filtered_msg)

                if (len(self.heading_readings) > self.max_readings):
                    self.heading_readings = np.delete(self.heading_readings, 0)

            # Sender ut not_valid signal dersom signal ikkje er godkjent
            else:
                heading_filtered_msg                = HeadingDevice()
                heading_filtered_msg.HeadingState   = False
                self.Heading_pub.publish(heading_filtered_msg)


    ### GNSS CALLBACK FUNKSJON ###
    def gnss_callback(self, msg: GNSS):
        self.current_lat    = msg.lat
        self.current_lon    = msg.lon
        self.current_sog    = msg.sog
        self.current_cog    = msg.cog
        self.GnssState      = msg.valid_signal

        if self.GnssState:
            # Rekne ut variansen til målingar
            self.lat_S, self.lat_average = self.varians_kalkulator(self.lat_readings)
            self.lon_S, self.lon_average = self.varians_kalkulator(self.lon_readings)

            # Sjekker om nye verdier er innanfor intervall
            if self.check_intervall(self.current_lat, self.lat_average, self.lat_S, 2):
                self.lat_readings = np.append(self.lat_readings, self.current_lat)
                filtered_lat = True
                if (len(self.lat_readings) > self.max_readings):
                    self.lat_readings = np.delete(self.lat_readings, 0)
            else:
                filtered_lat = False
            
            if self.check_intervall(self.current_lon, self.lon_average, self.lon_S, 2):
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
                filtered_lat = False
                filtered_lon = False
            
            # Sender ut not_valid signal dersom signal ikkje er godkjent
            else:
                gnss_filtered_msg               = GNSS()
                gnss_filtered_msg.valid_signal  = False
                self.Gnss_pub.publish(gnss_filtered_msg)

                
            
        
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

    ### INTERVALL SJEKK FUNKSJON ###
    def check_intervall(self, value, average, stand_avvik, toleranse):
        # Reknar ut intervall etter gitt antall standardavvik
        nedre_grense = average - (toleranse * stand_avvik)
        ovre_grense  = average + (toleranse * stand_avvik)

        if (value > nedre_grense) and (value < ovre_grense):
            return True
        else:
            return False


    ##### GAMMALT ##### 

    def gnss_behandling(self):
       # Reknar ut gjennomsnitt
        self.lat_average = sum(self.lat_readings) / len(self.lat_readings)
        self.lon_average = sum(self.lon_readings) / len(self.lon_readings)

        # Reknar ut sum for emperisk varians
        for i in self.lat_readings:
            self.lat_sum += (self.lat_readings[i] - self.lat_average)**2
            i + 1
            
        for i in self.lon_readings:
            self.lon_sum += (self.lon_readings[i] - self.lon_average)**2
            i + 1
            
        # Reknar ut empirisk varians
        self.emp_var_lat = (1 / (len(self.lat_readings) - 1)) * self.lat_sum
        self.emp_var_lon = (1 / (len(self.lon_readings) - 1)) * self.lon_sum

        # Reknar ut empirisk standardavvik
        self.lat_S = np.sqrt(self.emp_var_lat)
        self.lon_S = np.sqrt(self.emp_var_lon)

        # Sjekker om nyaste måling er innnanfor empirisk standardavvik
        if abs(self.current_lat - self.lat_readings[:-1]) < self.lat_S:
            np.append(self.lat_readings, self.current_lat)
                
        if abs(self.current_lon - self.lon_readings[:-1]) < self.lon_S:
            np.append(self.lon_readings, self.current_lon)

        # Sjekker at lat/lon readings ikkje inneheld meir en n målingar 
        if len(self.lat_readings) > self.max_readings:
            np.delete(self.lat_readings[0])
            
        if len(self.lon_readings) > self.max_readings:
            np.delete(self.lon_readings[0])



    def MedianFilter(self):
        ### Median filter ###
        return 1


    def LowPassFilter(self):
        ### LowPass filter ###
        return 2
        

    def AverageFilter(self):
        ### Flyttande gjennomsnitts filter ###
        return 3
    

def main(args=None):
    rclpy.init(args=args)
    node = SignalbehandlingsNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == 'main':
    main()