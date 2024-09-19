# Importerer nødvendige biblioteker og moduler for ROS2
import rclpy
from rclpy.node import Node
import numpy as np
import os
import yaml
from ngc_interfaces.msg import Eta, Nu, Tau
from ament_index_python.packages import get_package_share_directory
from ngc_utils.vessel_model import VesselModel
from ngc_utils.qos_profiles import default_qos_profile
import time
import ngc_utils.math_utils as mu
import ngc_utils.ngc_utils.geo_utils as geo
from std_msgs.msg import String

# Klassen Kontroller definerer en ROS2-node
class Kontroller(Node):
    # Initialiserer kontrolleren og setter opp abonnementer og publiseringer
    def __init__(self):
        # Kaller på superklassen Node for å initialisere noden med navnet "kontroller"
        super().__init__('kontroller')
        
        # Deklarerer og laster konfigurasjonsparametere fra YAML-filer
        self.declare_parameter('yaml_package_name', 'ngc_bringup')
        self.declare_parameter('vessel_config_file', 'config/vessel_config.yaml')
        self.declare_parameter('simulation_config_file', 'config/simulator_config.yaml')
        self.declare_parameter('control_config_file', 'config/control_config.yaml')

        # Henter konfigurasjonsfilenes stier ved hjelp av pakkenavnet
        yaml_package_name        = self.get_parameter('yaml_package_name').get_parameter_value().string_value
        yaml_package_path        = get_package_share_directory(yaml_package_name)
        vessel_config_path       = os.path.join(yaml_package_path, self.get_parameter('vessel_config_file').get_parameter_value().string_value)
        simulation_config_path   = os.path.join(yaml_package_path, self.get_parameter('simulation_config_file').get_parameter_value().string_value)
        self.control_config_path = os.path.join(yaml_package_path, self.get_parameter('control_config_file').get_parameter_value().string_value)

        # Laster YAML-konfigurasjonsfiler som inneholder informasjon om fartøyet og simuleringen
        self.vessel_config     = self.load_yaml_file(vessel_config_path)
        self.simulation_config = self.load_yaml_file(simulation_config_path)
        self.control_config    = self.load_yaml_file(self.control_config_path)

        # Initialiserer fartøymodellen basert på konfigurasjonen
        self.vessel_model = VesselModel(self.vessel_config)
        
        # Henter simulasjonens tidssteg fra konfigurasjonsfilen
        self.step_size = self.simulation_config['simulation_settings']['step_size']

        # Setter opp abonnenter for sensor data for heading og gnss (position)
        self.head_measurement       = self.create_subscription(HeadingDevice, 'heading_measurement', self.head_measurement_callback, default_qos_profile)
        self.gnss_measurement       = self.create_subscription(GNSS, 'gnss_measurement', self.gnss_measurement_callback, default_qos_profile)
        self.tau_sub                = self.create_subscription(Tau, 'tau_propulsion', default_qos_profile)

        
        # Setter opp en publisher der sender de estimerede værdier for eta og nu som kontrolleren skal bruge
        self.eta_hat                = self.create_publisher(Eta_hat, 'eta_hat', default_qos_profile)
        self.nu_hat                 = self.create_publisher(Nu_hat, 'nu_hat', default_qos_profile)
        
        
        # Initialiserer variabler for å lagre data
        self.head_measurement       = np.zeros(3)
        self.gnss_measurement       = np.zeros(3)
        self.tau_propulsion         = np.zeros(6)

        # Initialiserer variabler brugt i estimator
        self.previous_position      = np.zeros(2)
        self.velocity_estimate      = 0.0
        self.velocity_estimate      = 0.0
        self.W_error                = 1
        self.L1                     = 1
        self.L2                     = self.vessel_config['vessel']['mass'] * self.W_error ** 2
        self.L3                     = self.L2 / 10


        # Starter kontroll-løkken som kjører med samme tidssteg som simulatoren
        self.timer = self.create_timer(self.step_size, self.step_control)

        self.get_logger().info("Kontroller-node er initialisert.")

    # Funksjon for å laste inn YAML-konfigurasjonsfiler
    def load_yaml_file(self, file_path):
        
        with open(file_path, 'r') as file:
            return yaml.safe_load(file)

    def reload_configs_callback(self, msg: String):

        self.control_config = self.load_yaml_file(self.control_config_path)
        self.get_logger().info("Kontroller-node har lastet in config!")

    # Callback-funksjon for at modtage GNSS data fra sensor
    def gnss_measurement_callback(self, msg: GNSS):
        
        # Henter ind data fra GNSS
        self.gnss = np.array([msg.lat, msg.lon, msg.valid_signal])

    # Callback-funksjon for at modtage heading data fra sensor
    def head_measurement_callback(self, msg: HeadingDevice):
        
        # Modtager data fra heading sensor
        self.heading = np.array([msg.heading, msg.rot, msg.valid_signal])

    # Callback-funktion for at modtage tau-propul data fra kontroller
    def tau_propulsion (self, msg: Tau):

        #Modtager data fra kontroller
        self.tau_propulsion = np.array([msg.surge_x, msg.sway_y, msg.heave_z, msg.roll_k, msg.pitch_m, msg.yaw_n])

    # Funksjon som kjøres på hver simuleringstidssteg og implementerer kontrollalgoritmen
    def step_control(self):
        
        # Heading config
        omega                   = self.control_config['heading_control']['omega']
        zeta                    = self.control_config['heading_control']['zeta']
        ki_scale                = self.control_config['heading_control']['ki_scale']
        ki_sat_limit            = self.control_config['heading_control']['ki_saturation_limit']
        N_rr                    = self.control_config['heading_control']['N_rr']            # 
        linerearization_point   = self.control_config['heading_control']['linearization_point']
        dt                      = self.step_size

        # Vessel config
        mass                    = self.vessel_config['vessel']['mass']

        d_lokal                 = N_rr

        calculate_distance      = geo.calculate_distance_north_east(self.gnss[0], self.gnss[1], self.previous_position[0],self.previous_position[1])

        velocity_measurement    =  calculate_distance / dt

        self.previous_position  = np.array(self.gnss[0], self.gnss[1])

        self.velocity_tilde     = velocity_measurement - self.velocity_estimate

        self.velocity_estimate  = self.velocity_estimate + (dt * (self.velocity_estimate + (self.L1 * self.velocity_tilde)))




       

        # Opprett en Tau-melding for å sende de beregnede kreftene
        tau_message = Tau()
        tau_message.surge_x = tau_X
        tau_message.sway_y  = 0.0
        tau_message.heave_z = 0.0
        tau_message.roll_k  = 0.0
        tau_message.pitch_m = 0.0
        tau_message.yaw_n   = tau_N

        # Publiser kontrollkreftene på tau_propulsion-topic
        self.tau_pub.publish(tau_message)
        #self.get_logger().info("Kontrollkrefter publisert på tau_propulsion.")

# Hovedfunksjonen som starter ROS2-noden
def main(args=None):
    # Initialiserer ROS2-kommunikasjon
    rclpy.init(args=args)
    node = Kontroller()
    
    # Kjører noden til den stoppes
    rclpy.spin(node)
    
    # Når noden avsluttes, frigjør ressurser
    node.destroy_node()
    rclpy.shutdown()

# Starter hovedfunksjonen hvis denne filen kjøres som et skript
if __name__ == '__main__':
    main()

