# Importerer nødvendige biblioteker og moduler for ROS2
import rclpy
from rclpy.node import Node
import numpy as np
import os
import math
import yaml
from ngc_interfaces.msg import Eta, Nu, Tau, GNSS, HeadingDevice, ThrusterSignals
from ament_index_python.packages import get_package_share_directory
from ngc_utils.vessel_model import VesselModel
from ngc_utils.qos_profiles import default_qos_profile
import time
import ngc_utils.math_utils as mu
import ngc_utils.geo_utils as geo
from std_msgs.msg import String

# Klassen Allocator definerer en ROS2-node
class allocator(Node):
    # Initialiserer estimatoren og setter opp abonnementer og publiseringer
    def __init__(self):
        # Kaller på superklassen Node for å initialisere noden
        super().__init__('allocator')
        
        # Deklarerer og laster konfigurasjonsparametere fra YAML-filer
        self.declare_parameter('yaml_package_name', 'ngc_bringup')
        self.declare_parameter('vessel_config_file', 'config/vessel_config.yaml')
        self.declare_parameter('simulation_config_file', 'config/simulator_config.yaml')
        self.declare_parameter('control_config_file', 'config/control_config.yaml')
        self.declare_parameter('propulsion_config_file', 'config/propulsion_config.yaml')

        # Henter konfigurasjonsfilenes stier ved hjelp av pakkenavnet
        yaml_package_name        = self.get_parameter('yaml_package_name').get_parameter_value().string_value
        yaml_package_path        = get_package_share_directory(yaml_package_name)
        vessel_config_path       = os.path.join(yaml_package_path, self.get_parameter('vessel_config_file').get_parameter_value().string_value)
        simulation_config_path   = os.path.join(yaml_package_path, self.get_parameter('simulation_config_file').get_parameter_value().string_value)
        self.control_config_path = os.path.join(yaml_package_path, self.get_parameter('control_config_file').get_parameter_value().string_value)
        propulsion_config_path   = os.path.join(yaml_package_path, self.get_parameter('propulsion_config_file').get_parameter_value().string_value)

        # Laster YAML-konfigurasjonsfiler som inneholder informasjon om fartøyet og simuleringen
        self.vessel_config     = self.load_yaml_file(vessel_config_path)
        self.simulation_config = self.load_yaml_file(simulation_config_path)
        self.control_config    = self.load_yaml_file(self.control_config_path)
        self.propulsion_config = self.load_yaml_file(propulsion_config_path)

        # Initialiserer fartøymodellen basert på konfigurasjonen
        self.vessel_model = VesselModel(self.vessel_config)
        
        # Henter simulasjonens tidssteg fra konfigurasjonsfilen
        self.step_size = self.simulation_config['simulation_settings']['step_size']

        # Setter opp abonnenter for tau kræfter for omregning til RPS
        self.tau_sub                = self.create_subscription(Tau, 'tau_control',self.tau_control_callback, default_qos_profile)
        self.reload_config_sub      = self.create_subscription(String, 'reload_configs', self.reload_configs_callback, default_qos_profile)
        
        # Setter opp en publisher der sender de estimerede værdier for eta og nu som kontrolleren skal bruge
        self.thruster_1_setpoints_pub   = self.create_publisher(ThrusterSignals, 'thruster_1_setpoints', default_qos_profile)
        self.thruster_2_setpoints_pub   = self.create_publisher(ThrusterSignals, 'thruster_2_setpoints', default_qos_profile)
        self.tau_max_pub                = self.create_publisher(Tau,'tau_max', default_qos_profile)

        # Initialiser værdier
        self.tau_control    = np.array([0.0, 0.0])
        self.rps            = np.zeros(2)

        # Henter thruster

        # Starter kontroll-løkken som kjører med samme tidssteg som simulatoren
        self.timer = self.create_timer(self.step_size, self.step_allocator)

        # Initialiserer thruster parametre
        self.diameter_1     = self.propulsion_config['main_propulsion_1']['propeller']['diameter']
        self.diameter_2     = self.propulsion_config['main_propulsion_2']['propeller']['diameter']
        self.Kt0_1          = self.propulsion_config['main_propulsion_1']['propeller']['Kt0']
        self.Kt0_2          = self.propulsion_config['main_propulsion_2']['propeller']['Kt0']
        #self.x_position_1   = self.propulsion_config['main_propulsion_1']['position'][0]
        #self.x_position_2   = self.propulsion_config['main_propulsion_2']['position'][0]
        self.y_position_1   = self.propulsion_config['main_propulsion_1']['position'][1]
        self.y_position_2   = self.propulsion_config['main_propulsion_2']['position'][1]
        self.rps_max        = self.propulsion_config['main_propulsion_1']['propeller']['max_rpm'] / 60
        self.rps_min        = self.propulsion_config['main_propulsion_1']['propeller']['min_rpm'] / 60
        self.thruster_id_1  = self.propulsion_config['main_propulsion_1']['id']
        self.thruster_id_2  = self.propulsion_config['main_propulsion_2']['id']

        self.get_logger().info("Kontroller-node er initialisert.")

    # Funksjon for å laste inn YAML-konfigurasjonsfiler
    def load_yaml_file(self, file_path):
        
        with open(file_path, 'r') as file:
            return yaml.safe_load(file)

    def reload_configs_callback(self, msg: String):

        self.control_config = self.load_yaml_file(self.control_config_path)
        self.get_logger().info("Estimator-node har lastet in config!")

    # Callback-funktion for at modtage tau-propul data fra kontroller
    def tau_control_callback (self, msg: Tau):

        #Modtager data fra kontroller
        self.tau_control[0] = msg.surge_x
        self.tau_control[1] = msg.yaw_n


    # Funksjon som kjøres på hver simuleringstidssteg
    def step_allocator(self):

            # Calculate maximum thrust for each thruster using RPM
            
            #def calculate_max_thrust(Kt0, diameter, rps_max, rps_min):
            #    return 0.5 * 1025 * Kt0 * diameter**4 * abs(rps_min * 60) * rps_max * 60
    
            #self.max_thrust_1 = calculate_max_thrust(self.Kt0_1, self.diameter_1, self.rps_max, self.rps_min)
            #self.max_thrust_2 = calculate_max_thrust(self.Kt0_2, self.diameter_2, self.rps_max, self.rps_min)

            # Thrust Matrix
            self.thrust_matrix = np.array([
                [1,1], # X - direction
                [-self.y_position_1, -self.y_position_2], # Moment
                     ])

            thrust_matrix_product = self.thrust_matrix @ self.thrust_matrix.T
            
            # K Faktor
            self.K_1        = 1
            self.K_2        = 1
            
            self.K_list     = np.array([self.K_1, self.K_2])
            self.K_matrix   = np.diag(self.K_list)

            ### Inverse ###
            thrust_matrix_product_inv = np.linalg.inv(thrust_matrix_product)

            ### Pseudoinverse ###

            self.thrust_matrix_pseudo_inv = self.thrust_matrix.T @ thrust_matrix_product_inv

            ### Calculate thruster force ###

            self.thruster_forces = self.thrust_matrix_pseudo_inv @ self.tau_control

            self.u_1x = self.thruster_forces[0]
            self.u_2x = self.thruster_forces[1]


            ### Verifying inversion ###
            verify_thrust = self.thrust_matrix @ self.thruster_forces
            error = abs(verify_thrust - self.tau_control)
            if error[0] > 1 or error[1] > 1:
                self.get_logger().info(f"Errors pre saturation: {error[0]} {error[1]}")


            ### RPS Calculation ###     
            self.rps[0] = np.sign(self.u_1x) * np.sqrt((2*abs(self.u_1x)) / (self.Kt0_1 * 1025 * (self.diameter_1**4)))
            self.rps[1] = np.sign(self.u_2x) * np.sqrt((2*abs(self.u_2x)) / (self.Kt0_2 * 1025 * (self.diameter_2**4)))

            ### RPS Saturate ###
            self.rps[0] = mu.saturate(self.rps[0], self.rps_min, self.rps_max)
            self.rps[1] = mu.saturate(self.rps[1], self.rps_min, self.rps_max)
                        

            # Messages to publish
            thruster_1_setpoints_msg = ThrusterSignals()
            thruster_1_setpoints_msg.thruster_id = self.thruster_id_1
            thruster_1_setpoints_msg.rps = float(self.rps[0])
            thruster_1_setpoints_msg.pitch = float(0)
            thruster_1_setpoints_msg.azimuth_deg = float(0)
            thruster_1_setpoints_msg.active = True
            thruster_1_setpoints_msg.error  = False

            thruster_2_setpoints_msg = ThrusterSignals()
            thruster_2_setpoints_msg.thruster_id = self.thruster_id_2
            thruster_2_setpoints_msg.rps = float(self.rps[1])
            thruster_2_setpoints_msg.pitch = float(0)
            thruster_2_setpoints_msg.azimuth_deg = float(0)
            thruster_2_setpoints_msg.active = True
            thruster_2_setpoints_msg.error  = False

            fx_1 = 0.5 * self.Kt0_1 * 1025 * self.diameter_1 ** 4 * abs(self.rps[0])*self.rps[0]
            fx_2 = 0.5 * self.Kt0_1 * 1025 * self.diameter_1 ** 4 * abs(self.rps[1])*self.rps[1]

            ### Tau max ###
            tau_control_max = self.thrust_matrix @ np.array([fx_1, fx_2])

            # Create and publish the tau_max message
            tau_max_msg = Tau()
            tau_max_msg.surge_x = tau_control_max[0]
            tau_max_msg.surge_y = 0.0
            tau_max_msg.yaw_n = tau_control_max[1]
            
            # Publish tau_max
            self.tau_max_pub.publish(tau_max_msg)
       

            self.thruster_1_setpoints_pub.publish(thruster_1_setpoints_msg)
            self.thruster_2_setpoints_pub.publish(thruster_2_setpoints_msg)


# Hovedfunksjonen som starter ROS2-noden
def main(args=None):
    # Initialiserer ROS2-kommunikasjon
    rclpy.init(args=args)
    node = allocator()
    
    # Kjører noden til den stoppes
    rclpy.spin(node)
    
    # Når noden avsluttes, frigjør ressurser
    node.destroy_node()
    rclpy.shutdown()

# Starter hovedfunksjonen hvis denne filen kjøres som et skript
if __name__ == '__main__':
    main()

    ### GIT TEST CODE ###
    ### shared test ###