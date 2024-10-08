# Importerer nødvendige biblioteker og moduler for ROS2
import rclpy
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
import ngc_utils.geo_utils as geo
from std_msgs.msg import String

# Klassen Estimator definerer en ROS2-node
class Estimator(Node):
    # Initialiserer estimatoren og setter opp abonnementer og publiseringer
    def __init__(self):
        # Kaller på superklassen Node for å initialisere noden med navnet "estimator"
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

        # Setter opp abonnenter for sensor data for heading og gnss (position)
        self.heading_measurement    = self.create_subscription(HeadingDevice, 'heading_measurement', self.head_measurement_callback, default_qos_profile)
        self.gnss_measurement       = self.create_subscription(GNSS, 'gnss_measurement', self.gnss_measurement_callback, default_qos_profile)
        #self.tau_sub               = self.create_subscription(Tau, 'tau_propulsion',self.tau_propulsion_callback, default_qos_profile)
        self.tau_sub                = self.create_subscription(Tau, 'tau_max',self.tau_propulsion_callback, default_qos_profile)
        self.reload_config_sub      = self.create_subscription(String, 'reload_configs', self.reload_configs_callback, default_qos_profile)
        
        # Setter opp en publisher der sender de estimerede værdier for eta og nu som kontrolleren skal bruge
        self.eta_hat_pub            = self.create_publisher(Eta, 'eta_hat', default_qos_profile)
        self.nu_hat_pub             = self.create_publisher(Nu, 'nu_hat', default_qos_profile)

        # Initialiserer hastighedsvektor og positionsvektor
        self.tau_propulsion         = np.zeros(3)
        self.bias                   = np.zeros(3)
        self.eta_hat                = np.zeros(3)
        self.nu_hat                 = np.zeros(3)
        
        
        # Initialiserer variabler for å lagre data
        self.pos_meas_init          = False
        self.heading_meas_init      = False
        self.lat_hat                = 0
        self.lon_hat                = 0

       

        self.lat_measured           = 0
        self.lon_measured           = 0
        self.gnss_valid             = False
        self.heading_measurement    = 0
        self.rot_measured           = 0
        self.heading_valid          = False

        self.id                     = False

        # Starter kontroll-løkken som kjører med samme tidssteg som simulatoren
        self.timer = self.create_timer(self.step_size, self.step_estimator)

        self.get_logger().info("Kontroller-node er initialisert.")

    # Funksjon for å laste inn YAML-konfigurasjonsfiler
    def load_yaml_file(self, file_path):
        
        with open(file_path, 'r') as file:
            return yaml.safe_load(file)

    def reload_configs_callback(self, msg: String):

        self.control_config = self.load_yaml_file(self.control_config_path)
        self.get_logger().info("Estimator-node har lastet in config!")

    # Callback-funksjon for at modtage GNSS data fra sensor
    def gnss_measurement_callback(self, msg: GNSS):

        self.lat_measured = msg.lat
        self.lon_measured = msg.lon
        self.gnss_valid = msg.valid_signal
        
        # Henter ind data fra GNSS

        if self.pos_meas_init == False and msg.valid_signal == True:
            self.lat_hat =  msg.lat
            self.lon_hat = msg.lon
            self.pos_meas_init = True

    # Callback-funksjon for at modtage heading data fra sensor
    def head_measurement_callback(self, msg: HeadingDevice):
        
        # Modtager data fra heading sensor
        self.heading_measurement = msg.heading
        self.rot_measured        = msg.rot
        self.heading_valid       = msg.valid_signal
        self.id                  = msg.id

        if self.heading_meas_init == False and msg.valid_signal == True:
            self.eta_hat[2]      = mu.mapToPiPi(msg.heading)
            self.nu_hat[2]       = msg.rot
            self.heading_meas_init = True

    # Callback-funktion for at modtage tau-propul data fra kontroller
    def tau_propulsion_callback (self, msg: Tau):

        #Modtager data fra kontroller
        self.tau_propulsion = np.array([msg.surge_x, msg.sway_y, msg.yaw_n])

    # Funksjon som kjøres på hver simuleringstidssteg og implementerer kontrollalgoritmen
    def step_estimator(self):

        if self.pos_meas_init and self.heading_meas_init:
            
            eta_tilde = np.zeros(3)

            if self.gnss_valid:
                # Rekner om fra lat/lon til avstand i meter i NED koordinatsystem for bruk i estimatoren
                eta_tilde[0], eta_tilde[1] = geo.calculate_distance_north_east(self.lat_hat, self.lon_hat, self.lat_measured, self.lon_measured)
                self.gnss_valid = False
            
            if self.heading_valid:
                eta_tilde[2] = mu.mapToPiPi(self.heading_measurement - self.eta_hat[2])
                self.heading_valid = False

        
            # Input fra yaml fil i hnul
            L1                  = self.control_config['estimator']['L1']
            omega_e             = self.control_config['estimator']['omega_e']
            bias_gain           = self.control_config['estimator']['bias_gain']
            X_uu                = self.control_config['estimator']['X_uu']
            Y_vv                = self.control_config['estimator']['Y_vv']
            N_rr                = self.control_config['estimator']['N_rr']

            L1                  = L1 * np.diag([1,1,1])
            L2                  = omega_e ** 2 * np.diag([self.vessel_model.M[0][0], self.vessel_model.M[1][1], self.vessel_model.M[5][5]])
            L3                  = bias_gain * L2

            Q                   = np.diag([0.5+self.vessel_model.dimensions['width'], self.vessel_model.dimensions['length'], 1])

            # Integrer bias/forstyrrelse med Euler
            self.bias           += self.step_size * L3 @ eta_tilde

            # Omregn hastigheter til kroppsnatursystem
            R                   = mu.RotationMatrix(0,0,self.eta_hat[2])

            M_inv               = np.linalg.inv(np.diag([self.vessel_model.M[0][0], self.vessel_model.M[1][1], self.vessel_model.M[5][5]]))
            bias                = Q @ R.T @ self.bias
            drag                = np.zeros(3)
            drag[0]             = - X_uu*abs(self.nu_hat[0])*self.nu_hat[0]
            drag[1]             = - Y_vv*abs(self.nu_hat[1])*self.nu_hat[1]
            drag[2]             = - N_rr*abs(self.nu_hat[2])*self.nu_hat[2]

            # Reset endringer i NED koordinatsystemet siden vi ønsker bare forflyttning siste tidssedd og posisjon lagres i lat_hat og lon_hat
            self.eta_hat[0]     = 0
            self.eta_hat[1]     = 0

            # Integrer hastigheter og posisjoner med Euler
            self.nu_hat         += self.step_size * M_inv @ (drag + self.tau_propulsion + bias + L2 @ R.T @ eta_tilde)
            self.eta_hat        += self.step_size * (R @ self.nu_hat + L1 @ eta_tilde)

            # Passe på at headingtilstanden er var innenfor +/- 180 grader
            self.eta_hat[2] = mu.mapToPiPi(self.eta_hat[2])

            inj = L2 @ R.T @ eta_tilde

            # Legg estimert forflyttning i meter til Lat/Lon estimatet vårt
            self.lat_hat, self.lon_hat = geo.add_distance_to_lat_lon(self.lat_hat, self.lon_hat, self.eta_hat[0], self.eta_hat[1])

            # Eta_hat beskeder
            eta_hat_message = Eta()
            eta_hat_message.lat = float(self.lat_hat)
            eta_hat_message.lon = float(self.lon_hat)
            eta_hat_message.z = float(inj[2])
            eta_hat_message.phi = float(eta_tilde[2])
            eta_hat_message.theta = float(0)
            eta_hat_message.psi = float(self.eta_hat[2])
            
            # Nu_hat beskeder
            nu_hat_message = Nu()
            nu_hat_message.u = float(self.nu_hat[0])
            nu_hat_message.v = float(self.nu_hat[1])
            nu_hat_message.w = float(0)
            nu_hat_message.p = float(0)
            nu_hat_message.q = float(0)
            nu_hat_message.r = float(self.nu_hat[2])

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

