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

        self.Gnss_Sub       = self.create_subscription(GNSS, 'gnss_measurement', self.gnss_callback, default_qos_profile)
        self.Heading_Sub    = self.create_subscription(HeadingDevice, 'heading_measurement', self.heading_callback, default_qos_profile)

        self.lat_readings       = np.array([])
        self.lon_readings       = np.array([])
        self.heading_readings   = np.array([])

        self.max_readings = 10

    def heading_callback(self, msg: HeadingDevice):
        self.current_heading    = msg.heading
        self.current_rot        = msg.rot
        self.HeadingState       = msg.valid_signal
        
        
    def gnss_callback(self, msg: GNSS):
        self.current_lat    = msg.lat
        self.current_lon    = msg.lon
        self.GnssState      = msg.valid_signal
        self.gnss_behandling()
        

    def gnss_behandling(self):
       # Reknar ut gjennomsnitt
        self.lat_average = np.sum(self.lat_readings) / len(self.lat_readings)
        self.lon_average = np.sum(self.lon_readings) / len(self.lon_readings)

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