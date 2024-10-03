
import numpy as np
import rclpy
from rclpy.node import Node
import os
import yaml
from ngc_interfaces.msg import Eta, Nu, Tau, GNSS, HeadingDevice
from ament_index_python.packages import get_package_share_directory
from ngc_utils.vessel_model import VesselModel
from ngc_utils.qos_profiles import default_qos_profile
import time
import ngc_utils.math_utils as mu
import ngc_utils.geo_utils as geos
from std_msgs.msg import String


# Klassen Estimator definerer en ROS2-node
class Estimator(Node):
    # Initialiserer Estimator og setter opp abonnementer og publiseringer
    def __init__(self):
        # Kaller på superklassen Node for å initialisere noden med navnet "Estimator"
        super().__init__('estimator')
        
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

        # Setter opp abonnenter for (position_measurement, heading_measurement, tau_propultion)
        self.gnss_sub       = self.create_subscription(GNSS, 'gnss_measurement', self.gnss_callback, default_qos_profile)
        self.heading_sub    = self.create_subscription(HeadingDevice, 'heading_measurement', self.heading_callback, default_qos_profile)
        self.tau_sub        = self.create_subscription(Tau, 'tau_propulsion', self.tau_callback, default_qos_profile)
        self.reload_config_sub  = self.create_subscription(String, 'reload_configs', self.reload_configs_callback, default_qos_profile)

        # Setter opp en publisher for å publisere kontrollsignalene (tau_propulsion)
        self.eta_hat_pub = self.create_publisher(Eta, 'eta_hat', default_qos_profile)
        self.nu_hat_pub = self.create_publisher(Nu, 'nu_hat', default_qos_profile)
        
        # Initialiserer variabler
        self.tau        = np.zeros(3)
        self.eta_hat    = np.zeros(3)
        self.nu_hat     = np.zeros(3)
        self.bias       = np.zeros(3)
        
        self.estimator_pos_initialized = False
        self.estimator_hdg_initialized = False
        self.lat_hat = 0
        self.lon_hat = 0

        self.lat_measured        = 0
        self.lon_measured        = 0
        self.gnss_valid          = 0
        self.heading_measurement = 0
        self.rot_measured        = 0
        self.heading_valid       = False

        self.id                  = 0
        
        # Starter kontroll-løkken som kjører med samme tidssteg som simulatoren
        self.timer = self.create_timer(self.step_size, self.setp_estimator)

        self.get_logger().info("Estimator-node er initialisert.")


    # Funksjon for å laste inn YAML-konfigurasjonsfiler
    def load_yaml_file(self, file_path):
        
        with open(file_path, 'r') as file:
            return yaml.safe_load(file)

    def reload_configs_callback(self, msg: String):

        self.control_config = self.load_yaml_file(self.control_config_path)
        self.get_logger().info("estimator-node har lastet in config!")

    # Callback-funksjon for å motta eta_sim-data fra simulator
    def gnss_callback(self, msg: GNSS):

        self.lat_measured = msg.lat
        self.lon_measured = msg.lon
        self.gnss_valid   = msg.valid_signal

        if self.estimator_pos_initialized == False and msg.valid_signal == True:
            self.lat_hat = msg.lat
            self.lon_hat = msg.lon
            self.estimator_pos_initialized = True

    # Callback-funksjon for å mota nu_sim-data fra simulator
    def heading_callback(self, msg: Nu):

        self.heading_measurement = msg.heading
        self.rot_measured        = msg.rot
        self.heading_valid       = msg.valid_signal
        self.id                  = msg.id

        if self.estimator_hdg_initialized == False and msg.valid_signal == True:
            self.eta_hat[2]                 = mu.mapToPiPi(msg.heading)
            self.nu_hat[2]                  = msg.rot
            self.estimator_hdg_initialized  = True

    # Callback-funksjon for å mota propulsjons-data
    def tau_callback(self, msg: Eta):

        # Mota settpunktdata for posisjon og orientering
        self.tau = np.array([msg.surge_x, msg.sway_y, msg.yaw_n])



    # Funksjon som kjøres på hver simuleringstidssteg og implementerer kontrollalgoriten
    def setp_estimator(self):

        #Oppretter denne med null og endrer om det er gyldige målinger
        eta_tilde = np.zeros(3)

        if self.gnss_valid:
            # Rekner omfra lat/lon til avstand i meter i NED kordinatsystemet for bruk i estimatoren
            eta_tilde[0], eta_tilde[1] = geos.calculate_distance_north_east(self.lat_hat, self.lon_hat, self.lat_measured, self.lon_measured)
            self.gnss_valid = False

        if self.heading_valid:
            eta_tilde[2] = mu.mapToPiPi(self.heading_measurement - self.eta_hat[2])
            self.heading_valid = False
        
        self.get_logger().info(f"Tilde {eta_tilde[0], {eta_tilde[1]}}")
        
        # Input fra yaml fil i hmi
        l1          = self.control_config['estimator']['L1']
        omega_e     = self.control_config['estimator']['omega_e']
        bias_gain   = self.control_config['estimator']['bias_gain']
        X_uu        = self.control_config['estimator']['X_uu']
        Y_vv        = self.control_config['estimator']['Y_vv']
        N_rr        = self.control_config['estimator']['N_rr']

        L1 = l1 * np.diag([1,1,1])
        L2 = omega_e**2 * np.diag([self.vessel_model.M[0][0],self.vessel_model.M[1][1], self.vessel_model.M[5][5]])
        L3 = bias_gain * L2

        Q = np.diag([0.5 * self.vessel_model.dimensions['width'], self.vessel_model.dimensions['length'], 1])

        # Integrerer bias/forstyrrelse med Euler
        self.bias += self.step_size * L3 @ self.bias

        # Rekner ut rotasjonsmatrisen
        R = mu.RotationMatrix(0,0,self.eta_hat[2])

        M_inv = np.linalg.inv(np.diag([self.vessel_model.M[0][0], self.vessel_model.M[1][1], self.vessel_model.M[5][5]]))
        bias = Q @ R.T @ eta_tilde
        drag = np.zeros(3)
        drag[0] = -X_uu * abs(self.nu_hat[0] * self.nu_hat[0])
        drag[1] = -Y_vv * abs(self.nu_hat[1] * self.nu_hat[1])
        drag[2] = -N_rr * abs(self.nu_hat[2] * self.nu_hat[2])

        # Reset endring i NED kordinatsystem siden vi ønsker bare forflytning siste tidssted og posisjon lagres i lat_hat og lon_hat
        self.eta_hat[0] = 0
        self.eta_hat[1] = 0

        # Integrerer hastigheter og posisjoner med Euler
        self.nu_hat += self.step_size * M_inv @ (drag + self.tau + bias + L2 @ R.T @ eta_tilde)
        self.eta_hat += self.step_size * (R @ self.nu_hat + L1 @ eta_tilde)

        # Passe på at headingtilstanden vår er innenfor +/- 180 grader
        self.eta_hat[2] = mu.mapToPiPi(self.eta_hat[2])

        inj = L2 @ R.T @ eta_tilde

        # Legg estimert forflytning i meter til lat/lon estimatet vårt
        self.lat_hat, self.lon_hat = geos.add_distance_to_lat_lon(self.lat_hat, self.lon_hat, self.eta_hat[0], self.eta_hat[1])

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



# Hovedfunksjonen som starter ROS2-noden
def main(args=None):
    # Initialiserer ROS2-kommunikasjon
    rclpy.init(args=args)
    node = Estimator()
    
    # Kjører noden til den stoppes
    rclpy.spin(node)
    
    # Når noden avsluttes, frigjør ressurser
    node.destroy_node()
    rclpy.shutdown()

# Starter hovedfunksjonen hvis denne filen kjøres som et skript
if __name__ == '__main__':
    main()
