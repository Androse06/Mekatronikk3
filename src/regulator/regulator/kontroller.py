import rclpy
from rclpy.node import Node
import numpy as np
import os
import yaml
from ngc_interfaces.msg import Eta, Nu, Tau, HMI
from ament_index_python.packages import get_package_share_directory
from ngc_utils.vessel_model import VesselModel
from ngc_utils.qos_profiles import default_qos_profile
import time
import ngc_utils.math_utils as mu
from std_msgs.msg import String

class Kontroller(Node):
    def __init__(self):
        super().__init__('kontroller')
        
        self.declare_parameter('yaml_package_name', 'ngc_bringup')
        self.declare_parameter('vessel_config_file', 'config/vessel_config.yaml')
        self.declare_parameter('simulation_config_file', 'config/simulator_config.yaml')
        self.declare_parameter('control_config_file', 'config/control_config.yaml')

        yaml_package_name        = self.get_parameter('yaml_package_name').get_parameter_value().string_value
        yaml_package_path        = get_package_share_directory(yaml_package_name)
        vessel_config_path       = os.path.join(yaml_package_path, self.get_parameter('vessel_config_file').get_parameter_value().string_value)
        simulation_config_path   = os.path.join(yaml_package_path, self.get_parameter('simulation_config_file').get_parameter_value().string_value)
        self.control_config_path = os.path.join(yaml_package_path, self.get_parameter('control_config_file').get_parameter_value().string_value)

        self.vessel_config     = self.load_yaml_file(vessel_config_path)
        self.simulation_config = self.load_yaml_file(simulation_config_path)
        self.control_config    = self.load_yaml_file(self.control_config_path)

        self.vessel_model = VesselModel(self.vessel_config)
        
        self.step_size = self.simulation_config['simulation_settings']['step_size']

        #### SUB ####
        self.eta_setpoint_sub       = self.create_subscription(Eta, 'eta_setpoint', self.eta_setpoint_callback, default_qos_profile)
        #self.eta_sub                = self.create_subscription(Eta, 'eta_sim', self.eta_callback, default_qos_profile)
        self.nu_setpoint_sub        = self.create_subscription(Nu, 'nu_setpoint', self.nu_setpoint_callback, default_qos_profile)
        #self.nu_sub                 = self.create_subscription(Nu, 'nu_sim', self.nu_callback, default_qos_profile)
        self.reload_config_sub      = self.create_subscription(String, 'reload_configs', self.reload_configs_callback, default_qos_profile)
        self.mode_sub               = self.create_subscription(HMI, 'hmi', self.mode_callback, default_qos_profile)
        self.eta_hat_sub            = self.create_subscription(Eta, "eta_hat", self.eta_callback, default_qos_profile)
        self.nu_hat_sub             = self.create_subscription(Nu, "nu_hat", self.nu_callback, default_qos_profile)
        self.eta_waypoint_sub       = self.create_subscription(Eta, "eta_waypoint_setpoint", self.eta_waypoint_callback, default_qos_profile)
        #### PUB ####
        self.tau_pub = self.create_publisher(Tau, "tau_control", default_qos_profile)


        #### Variabler ####

        self.eta          = np.zeros(6)
        self.nu           = np.zeros(6)
        self.eta_setpoint = np.zeros(6)
        self.nu_setpoint  = np.zeros(6)
        
        self.qi_psi       = 0.0
        self.qi_u         = 0.0

        self.estimator_ready = False

        self.standby    = False
        self.position   = False 
        self.sail       = False
        self.track      = False

        ####################

        self.timer = self.create_timer(self.step_size, self.step_control)

        self.get_logger().info("Kontroller-node er initialisert.")

        self.debug = False

    def load_yaml_file(self, file_path):
        with open(file_path, 'r') as file:
            return yaml.safe_load(file)

    def reload_configs_callback(self, msg: String):
        self.control_config = self.load_yaml_file(self.control_config_path)
        self.get_logger().info("Kontroller-node har lastet in config!")

    def eta_callback(self, msg: Eta):
        self.eta = np.array([msg.lat, msg.lon, msg.z, msg.phi, msg.theta, msg.psi])
        self.estimator_ready = True

    def eta_waypoint_callback(self, msg: Eta):
        if self.track:
            self.eta_setpoint = np.array([msg.lat, msg.lon, msg.z, msg.phi, msg.theta, msg.psi])
        else:
            return

    def nu_callback(self, msg: Nu):
        self.nu = np.array([msg.u, msg.v, msg.w, msg.p, msg.q, msg.r])

    def eta_setpoint_callback(self, msg: Eta):
        if not self.track:
            self.eta_setpoint = np.array([msg.lat, msg.lon, msg.z, msg.phi, msg.theta, msg.psi])
        else:
            return
        
    def nu_setpoint_callback(self, msg: Nu):
        self.nu_setpoint = np.array([msg.u, msg.v, msg.w, msg.p, msg.q, msg.r])

    def mode_callback(self, msg: HMI): # I ngc_hmi_autopilot sendes det setpunkter. 1 er True, alle andre er False.
        if msg.mode == 0:
            self.standby = True
            self.position = False
            self.sail = False
            self.track = False
        if msg.mode == 1:
            self.standby = False
            self.position = False
            self.sail = True
            self.track = False
        if msg.mode == 2:
            self.standby = False
            self.position = True
            self.sail = False
            self.track = False
        if msg.mode == 3:
            self.standby = False
            self.position = False
            self.sail = False
            self.track = True


    def step_control(self):
        
        if self.estimator_ready:
        ################## PID Heading #####################
            e_psi       = mu.mapToPiPi(self.eta_setpoint[5] - self.eta[5])
            e_psi_dot   = self.nu_setpoint[5] - self.nu[5]

            omega       = self.control_config['heading_control']['omega']
            zeta        = self.control_config['heading_control']['zeta']
            ki_scale    = self.control_config['heading_control']['ki_scale']
            ki_limit    = self.control_config['heading_control']['ki_saturation_limit']

            d_stjerne   = self.control_config['heading_control']['N_rr'] * self.control_config['heading_control']['linearization_point']

            K_p_psi = self.vessel_model.M[5][5]*omega**2
            K_d_psi = 2*zeta*omega*self.vessel_model.M[5][5] - d_stjerne
            K_i_psi = K_p_psi / (abs(ki_scale) + np.rad2deg(e_psi)**2)   

            self.qi_psi += self.step_size*K_i_psi*mu.saturate(e_psi,-np.deg2rad(ki_limit),np.deg2rad(ki_limit))

            P_ledd      = K_p_psi * e_psi
            I_ledd      = K_i_psi * self.qi_psi
            D_ledd      = K_d_psi * e_psi_dot

            tau_N       = P_ledd + I_ledd + D_ledd

            ################## PI Fart #####################
            e_u         = self.nu_setpoint[0] - self.nu[0]


            ki_scale_u  = self.control_config['speed_control']['ki_scale']
            ki_limit_u  = self.control_config['speed_control']['ki_saturation_limit']
            X_uu        = self.control_config['speed_control']['X_uu']

            K_p_u = self.vessel_model.M[0][0]*self.control_config['speed_control']['K_p']
            K_i_u = K_p_u / (abs(ki_scale_u) + e_u**2)

            self.qi_u += self.step_size*K_i_u*mu.saturate(e_u,-ki_limit_u,ki_limit_u)

            tau_X = X_uu*abs(self.nu_setpoint[0])*self.nu_setpoint[0] + K_p_u*e_u + self.qi_u
            
            ################## Publiser kontrollkrefter #####################

            tau_message         = Tau()
            tau_message.surge_x = tau_X
            tau_message.sway_y  = 0.0
            tau_message.heave_z = 0.0
            tau_message.roll_k  = 0.0
            tau_message.pitch_m = 0.0
            tau_message.yaw_n   = tau_N

            self.tau_pub.publish(tau_message)


        ################## Debugging #####################
        if self.debug == True:

            self.get_logger().info(f'tau_message: {tau_message}')

            self.get_logger().info(f'error psi: {e_psi}')
            self.get_logger().info(f'error u: {e_u}')
            self.get_logger().info(f'yaw: {tau_N}')
            self.get_logger().info(f'qi psi: {self.qi_psi}')
            self.get_logger().info(f'qi u: {self.qi_u}')
            self.get_logger().info(f'Eta: {self.eta[5]}')
            self.get_logger().info(f'Nu: {self.nu[0]}')

def main(args=None):
    rclpy.init(args=args)
    node = Kontroller()
    
    rclpy.spin(node)
    
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
