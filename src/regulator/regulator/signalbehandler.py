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

        self.Gnss_Sub = self.create_subscription(GNSS, 'gnss_measurement', self.gnss_callback, default_qos_profile)
        self.Heading_Sub = self.create_subscription(HeadingDevice, 'heading_measurement', self.heading_callback, default_qos_profile)


        def heading_callback(self):
            ###tull
            return 1

        def Gnss_callback(self):
            ###tull
            return 1

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