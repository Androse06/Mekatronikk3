### Signal Behandling ###
import rclpy
from rclpy.node import Node
import gpxpy
from ngc_interfaces.msg import HMI, Eta, Nu, Route
from ngc_utils.qos_profiles import default_qos_profile
import numpy as np
import ngc_utils.geo_utils as geo
import ngc_utils.math_utils as mu


class SignalbehandlingsNode(Node):

    
    def __init__(self):
        super().__init__('signalbehandling')


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