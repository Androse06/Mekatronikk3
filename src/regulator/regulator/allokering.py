import rclpy
from rclpy.node import Node
import numpy as np
import os
import yaml
from ngc_interfaces.msg import Tau, ThrusterSignals
from ament_index_python.packages import get_package_share_directory
from ngc_utils.qos_profiles import default_qos_profile
import time
import ngc_utils.math_utils as mu


class Allokering(Node):
    def __init__(self):
        super().__init__('allokering')
        
        self.declare_parameter('yaml_package_name', 'ngc_bringup')
        self.declare_parameter('simulation_config_file', 'config/simulator_config.yaml')
        self.declare_parameter('propulsion_config_file', 'config/propulsion_config.yaml')

        yaml_package_name           = self.get_parameter('yaml_package_name').get_parameter_value().string_value
        yaml_package_path           = get_package_share_directory(yaml_package_name)
        simulation_config_path      = os.path.join(yaml_package_path, self.get_parameter('simulation_config_file').get_parameter_value().string_value)
        self.propulsion_config_path = os.path.join(yaml_package_path, self.get_parameter('propulsion_config_file').get_parameter_value().string_value)

        self.simulation_config      = self.load_yaml_file(simulation_config_path)
        self.propuslion_config      = self.load_yaml_file(self.propulsion_config_path)
        
        self.step_size = self.simulation_config['simulation_settings']['step_size']

        ##### SUB ####
        self.tau_sub                = self.create_subscription(Tau, "tau_control", self.tau_callback, default_qos_profile)
        
        ##### PUB ####
        self.thruster1_pub          = self.create_publisher(ThrusterSignals, "thruster_1_setpoints", default_qos_profile)
        self.thruster2_pub          = self.create_publisher(ThrusterSignals, "thruster_2_setpoints", default_qos_profile)
        self.tau_max_pub            = self.create_publisher(Tau, "tau_max", default_qos_profile)

        ##### Variabler ####
        self.rho                     = self.simulation_config['physical_parameters']['rho_water']
        self.tau                     = np.zeros(3)

                ### Thruster 1 ###
        self.id_1                    = self.propuslion_config['main_propulsion_1']['id']
        self.propellerDiameter_1     = self.propuslion_config['main_propulsion_1']['propeller']['diameter']
        self.Kt0_1                   = self.propuslion_config['main_propulsion_1']['propeller']['Kt0']
        self.max_rps_1               = self.propuslion_config['main_propulsion_1']['propeller']['max_rpm'] / 60
        self.min_rps_1               = self.propuslion_config['main_propulsion_1']['propeller']['min_rpm'] / 60
        self.position_1              = self.propuslion_config['main_propulsion_1']['position']               # [-1,-0.5,0.3]
        self.type_1                  = self.propuslion_config['main_propulsion_1']['type']

                ### Thruster 2 ###
        self.id_2                    = self.propuslion_config['main_propulsion_2']['id']
        self.propellerDiameter_2     = self.propuslion_config['main_propulsion_2']['propeller']['diameter']
        self.Kt0_2                   = self.propuslion_config['main_propulsion_2']['propeller']['Kt0']
        self.max_rps_2               = self.propuslion_config['main_propulsion_2']['propeller']['max_rpm'] / 60
        self.min_rps_2               = self.propuslion_config['main_propulsion_2']['propeller']['min_rpm'] / 60
        self.position_2              = self.propuslion_config['main_propulsion_2']['position']               # [-1,0.5,0.3]
        self.type_2                  = self.propuslion_config['main_propulsion_2']['type']

        ######################

        self.timer = self.create_timer(self.step_size, self.step_allokering)

        self.get_logger().info("allokering-node er initialisert.")

        self.debug = False


    def load_yaml_file(self, file_path):
        with open(file_path, 'r') as file:
            return yaml.safe_load(file)

    def tau_callback(self, msg: Tau):
        self.tau = np.array([msg.surge_x, msg.sway_y, msg.yaw_n])

    def rps(self, x, KT0, propellerDiameter):
        return np.sign(x) * np.sqrt((2 * np.abs(x)) / ( self.rho * KT0 * (propellerDiameter ** 4)))
    
    def force(self, rps, KT0, propellerDiameter):
        return 0.5 * self.rho * KT0 * (propellerDiameter**4) * abs(rps) * rps 


    def step_allokering(self):

        We = np.eye(4)

        Te = np.array([[1, 0, 1, 0],
                       [0, 1, 0, 1],
                       [abs(self.position_1[1]), 0, -abs(self.position_2[1]), 0]])


        Twt = np.linalg.inv(We) @ Te.T @ np.linalg.inv(Te @ np.linalg.inv(We) @ Te.T)
        
        fe = Twt @ self.tau

        rps_1 = self.rps(fe[0], self.Kt0_1, self.propellerDiameter_1)
        rps_2 = self.rps(fe[2], self.Kt0_2, self.propellerDiameter_2)


        ########### PUBLISH ###########
        thruster1_message               = ThrusterSignals()
        thruster1_message.thruster_id   = self.id_1
        thruster1_message.rps           = mu.saturate(rps_1, self.min_rps_1, self.max_rps_1)
        thruster1_message.pitch         = 0.0
        thruster1_message.azimuth_deg   = 0.0
        thruster1_message.active        = True
        thruster1_message.error         = False

        thruster2_message               = ThrusterSignals()
        thruster2_message.thruster_id   = self.id_2
        thruster2_message.rps           = mu.saturate(rps_2, self.min_rps_2, self.max_rps_2)
        thruster2_message.pitch         = 0.0
        thruster2_message.azimuth_deg   = 0.0
        thruster2_message.active        = True
        thruster2_message.error         = False


        ######## TAU_MAX ########
        if self.force(self.max_rps_1, self.Kt0_1, self.propellerDiameter_1) <= self.force(self.max_rps_2, self.Kt0_2, self.propellerDiameter_2):
            max_surge   = self.force(self.max_rps_1, self.Kt0_1, self.propellerDiameter_1)
            max_yaw     = max_surge * abs(self.position_1[1])
        else:
            max_surge   = self.force(self.max_rps_2, self.Kt0_2, self.propellerDiameter_2)
            max_yaw     = max_surge * (-abs(self.position_2[1]))

        tau_max_message                 = Tau()
        tau_max_message.surge_x         = 2 * max_surge # 2* pga 2 thrustere med 1/2 av oters totale thrust
        tau_max_message.sway_y          = 0.0
        tau_max_message.heave_z         = 0.0
        tau_max_message.roll_k          = 0.0
        tau_max_message.pitch_m         = 0.0
        tau_max_message.yaw_n           = max_yaw

        self.thruster1_pub.publish(thruster1_message)
        self.thruster2_pub.publish(thruster2_message)
        #self.tau_max_pub.publish(tau_max_message)


        ########### DEBUGGING ###########
        if self.debug == True:

            self.get_logger().info(f"thruster1_message: {thruster1_message}")
            self.get_logger().info(f"thruster2_message: {thruster2_message}")
            self.get_logger().info(f"tau_max_message: {tau_max_message}")

            self.get_logger().info(f'Te: {Te}')
            self.get_logger().info(f'Twt: {Twt}')
            self.get_logger().info(f'fe: {fe}')
            self.get_logger().info(f'********tau: {self.tau}')

            self.get_logger().info(f'********Tefe: {Te @ fe}')
            self.get_logger().info(f'Thruster 1 - rps: {thruster1_message.rps} ... deg: {thruster1_message.azimuth_deg} ... type: {self.type_1}')
            self.get_logger().info(f'Thruster 2 - rps: {thruster2_message.rps} ... deg: {thruster2_message.azimuth_deg} ... type: {self.type_2}')




def main(args=None):
    rclpy.init(args=args)
    node = Allokering()
    
    rclpy.spin(node)
    
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

