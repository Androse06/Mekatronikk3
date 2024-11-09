import rclpy
import csv
from rclpy.node import Node
import numpy as np
import os
import yaml
from ngc_interfaces.msg import Eta, Nu, Tau, GNSS, HeadingDevice
from ament_index_python.packages import get_package_share_directory
from ngc_utils.vessel_model import VesselModel
from ngc_utils.qos_profiles import default_qos_profile
import time
import ngc_utils.math_utils as mu
from std_msgs.msg import String
import ngc_utils.geo_utils as geo


class Estimator(Node):
    def __init__(self):
        super().__init__('estimator')
        
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

        self.csvfile    = open('estimator_data.csv', 'w', newline='')
        self.csv_writer = csv.writer(self.csvfile)
        self.csv_writer.writerow(['Latitude', 'Longitude'])

        filter_active = True

        #### SUB ####
        self.reload_config_sub  = self.create_subscription(String, 'reload_configs', self.reload_configs_callback, default_qos_profile)
        self.tau_sub            = self.create_subscription(Tau, "tau_control", self.tau_callback, default_qos_profile)
        if filter_active:
            self.heading_sub    = self.create_subscription(HeadingDevice, 'heading_measurement_filtered', self.heading_callback, default_qos_profile)  # Filtrert signal
            self.gnss_sub       = self.create_subscription(GNSS, 'gnss_measurement_filtered', self.gnss_callback, default_qos_profile)                 # Filtrert signal
        else:
            self.heading_sub    = self.create_subscription(HeadingDevice, 'heading_measurement', self.heading_callback, default_qos_profile)
            self.gnss_sub       = self.create_subscription(GNSS, "gnss_measurement", self.gnss_callback, default_qos_profile)   

        #### PUB ####
        self.eta_hat_pub    = self.create_publisher(Eta, "eta_hat", default_qos_profile)
        self.nu_hat_pub     = self.create_publisher(Nu, "nu_hat", default_qos_profile)

        #### Variabler ####
        self.heading_measured   = None
        self.rot                = None
        self.lat_measured       = 0
        self.lon_measured       = 0
        self.lat_hat            = 0
        self.lon_hat            = 0
        self.eta_hat            = np.zeros(3)
        self.nu_hat             = np.zeros(3)

        self.estimator_pos_initialized = False
        self.estimator_hdg_initialized = False

        self.gnss_valid     = False
        self.heading_valid  = False
        self.bias           = np.zeros(3)
        self.tau            = np.zeros(3)
        self.nu_hat         = np.zeros(3)
        self.eta_hat        = np.zeros(3)
        
        self.timer = self.create_timer(self.step_size, self.step_estimator)

        self.get_logger().info("Estimator-node er initialisert.")

        if filter_active:
            self.get_logger().info("Estimator-node bruker filtrert signaler.")
        else:
            self.get_logger().info("Estimator-node bruker u-filtrert signaler.")

        self.debug = self.control_config['debug']['estimator']

    def load_yaml_file(self, file_path):
        with open(file_path, 'r') as file:
            return yaml.safe_load(file)

    def reload_configs_callback(self, msg: String):
        self.control_config = self.load_yaml_file(self.control_config_path)

    def gnss_callback(self, msg: GNSS):
        self.lat_measured   = msg.lat
        self.lon_measured   = msg.lon
        self.gnss_valid     = msg.valid_signal
        if self.estimator_pos_initialized == False and msg.valid_signal == True:
            self.estimator_pos_initialized = True
            self.lat_hat    = msg.lat # Hvis den starter med 0 vil den første pos verdien være i senter av jorden
            self.lon_hat    = msg.lon # Hvis den starter med 0 vil den første pos verdien være i senter av jorden
            
    def heading_callback(self, msg: HeadingDevice):
        self.heading_measured   = msg.heading
        self.rot                = msg.rot
        self.heading_valid      = msg.valid_signal
        if self.estimator_hdg_initialized == False and msg.valid_signal == True:
            self.estimator_hdg_initialized = True
            self.eta_hat[2] = mu.mapToPiPi(msg.heading)
            self.nu_hat[2]  = msg.rot

    def tau_callback(self, msg: Tau):
        self.tau = np.array([msg.surge_x, 0.0, msg.yaw_n])


    def step_estimator(self):

        if self.estimator_pos_initialized and self.estimator_hdg_initialized:
                eta_tilde = np.zeros(3)

                if self.gnss_valid == True:
                    eta_tilde[0], eta_tilde[1] = geo.calculate_distance_north_east(self.lat_hat, self.lon_hat, self.lat_measured, self.lon_measured)
                    self.gnss_valid = False

                if self.heading_valid == True:
                    eta_tilde[2] = mu.mapToPiPi(self.heading_measured - self.eta_hat[2])
                    self.heading_valid = False

                l1          = self.control_config['estimator']['L1']
                omega_e     = self.control_config['estimator']['omega_e']
                bias_gain   = self.control_config['estimator']['bias_gain']
                X_uu        = self.control_config['estimator']['X_uu']
                Y_vv        = self.control_config['estimator']['Y_vv']
                N_rr        = self.control_config['estimator']['N_rr']

                L1 = l1 * np.diag([1, 1, 1])
                L2 = omega_e**2 * np.diag([self.vessel_model.M[0][0], self.vessel_model.M[1][1], self.vessel_model.M[5][5]])
                L3 = bias_gain * L2

                Q = np.diag([0.5 * self.vessel_model.dimensions['width'], self.vessel_model.dimensions['length'], 1])

                self.bias += self.step_size * L3 @ eta_tilde

                R = mu.RotationMatrix(0,0,self.eta_hat[2])

                M_inv   = np.linalg.inv(np.diag([self.vessel_model.M[0][0], self.vessel_model.M[1][1], self.vessel_model.M[5][5]]))
                bias    = Q @ R.T @ self.bias
                drag    = np.zeros(3)
                drag[0] = - X_uu * abs(self.nu_hat[0]) * self.nu_hat[0]
                drag[1] = - Y_vv * abs(self.nu_hat[1]) * self.nu_hat[1]
                drag[2] = - N_rr * abs(self.nu_hat[2]) * self.nu_hat[2]

                self.eta_hat[0] = 0
                self.eta_hat[1] = 0

                self.nu_hat     += self.step_size * M_inv @ (drag + self.tau + bias + L2 @ R.T @ eta_tilde)
                self.eta_hat    += self.step_size * (R @ self.nu_hat + L1 @ eta_tilde)

                self.eta_hat[2] = mu.mapToPiPi(self.eta_hat[2])

                inj = L2 @ R.T @ eta_tilde

                self.lat_hat, self.lon_hat = geo.add_distance_to_lat_lon(self.lat_hat, self.lon_hat, self.eta_hat[0], self.eta_hat[1])


                ###### PUBLISH ######
                eta_hat_message         = Eta()
                eta_hat_message.lat     = float(self.lat_hat)
                eta_hat_message.lon     = float(self.lon_hat)
                eta_hat_message.z       = float(inj[2])
                eta_hat_message.phi     = float(eta_tilde[2])
                eta_hat_message.theta   = float(0)
                eta_hat_message.psi     = float(self.eta_hat[2])

                nu_hat_message          = Nu()
                nu_hat_message.u        = float(self.nu_hat[0])
                nu_hat_message.v        = float(self.nu_hat[1])
                nu_hat_message.w        = float(0)
                nu_hat_message.p        = float(0)
                nu_hat_message.q        = float(0)
                nu_hat_message.r        = float(self.nu_hat[2])

                self.eta_hat_pub.publish(eta_hat_message)
                self.nu_hat_pub.publish(nu_hat_message)

                self.csv_logger() # printer ut lat og lon til en csv fil

                ####### DEBUG ########
                self.debug = self.control_config['debug']['estimator']
                if self.debug == True:
                    self.get_logger().info(
                        f"eta_hat_message: {eta_hat_message}\n"
                        f"nu_hat_message: {nu_hat_message}\n"
                        f"M_inv: {M_inv}\n"
                        f"drag: {drag}\n"
                        f"tau: {self.tau}\n"
                        f"bias: {bias}\n"
                        f"L2: {L2}\n"
                        f"R.T: {R.T}\n"
                        f"eta_tilde: {eta_tilde}\n"
                        f"R: {R}\n"
                        f"L1: {L1}\n"
                        f'nu_hat: {self.nu_hat}\n'
                        f'eta_hat: {self.eta_hat}'
                    )

    def csv_logger(self):
            with open('estimator_data.csv', 'a', newline='') as csvfile: # Den appender eksisterende csv
                csv_writer = csv.writer(csvfile)
                data = [self.lat_hat, self.lon_hat]
                csv_writer.writerow(data)

    def __del__(self): # lukker csv filen når programmet stopper
        self.csvfile.close()

def main(args=None):
    rclpy.init(args=args)
    node = Estimator()
    rclpy.spin(node)
    node.destroy_nrotode()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

