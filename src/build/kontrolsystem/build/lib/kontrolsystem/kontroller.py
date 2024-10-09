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

        # Setter opp abonnenter for å lytte på data fra simulatoren (eta og nu) og settpunkter (eta_setpoint, nu_setpoint)
        self.eta_hat_sub            = self.create_subscription(Eta, 'eta_hat', self.eta_hat_callback, default_qos_profile)
        self.nu_hat_sub             = self.create_subscription(Nu, 'nu_hat', self.nu_hat_callback, default_qos_profile)
        self.eta_setpoint_sub       = self.create_subscription(Eta, 'eta_setpoint', self.eta_setpoint_callback, default_qos_profile)
        #self.eta_sub                = self.create_subscription(Eta, 'eta_sim', self.eta_callback, default_qos_profile)
        self.nu_setpoint_sub        = self.create_subscription(Nu, 'nu_setpoint', self.nu_setpoint_callback, default_qos_profile)
        #self.nu_sub                 = self.create_subscription(Nu,'nu_sim', self.nu_callback, default_qos_profile)
        self.reload_config_sub      = self.create_subscription(String, 'reload_configs', self.reload_configs_callback, default_qos_profile)
        self.tau_max_sub            = self.create_subscription(Tau, 'tau_max', self.tau_max_callback, default_qos_profile)
        
        # Setter opp en publisher for å publisere kontrollsignalene (tau_propulsion)
        #self.tau_pub               = self.create_publisher(Tau,'tau_propulsion', default_qos_profile)
        self.tau_control_pub                = self.create_publisher(Tau, 'tau_control', default_qos_profile)
        
        # Initialiserer variabler for å lagre data fra simulatoren og settpunkter
        self.eta          = np.zeros(6)
        self.nu           = np.zeros(6)
        self.eta_setpoint = np.zeros(6)
        self.nu_setpoint  = np.zeros(6)
        self.eta_hat      = np.zeros(6)
        self.nu_hat       = np.zeros(6)

        # Integraltilstander i PID kontroll
        self.qi_psi = 0.0
        self.qi_u   = 0.0

        # Initialiserer max thrust og max moment
        self.max_surge    = 0
        self.max_thrust_tilbage = 0
        self.max_yaw         = 0

        # Starter kontroll-løkken som kjører med samme tidssteg som simulatoren
        self.timer = self.create_timer(self.step_size, self.step_control)
        self.last_print_time = time.time()  # Store the initial time

        self.get_logger().info("Kontroller-node er initialisert.")

    # Funksjon for å laste inn YAML-konfigurasjonsfiler
    def load_yaml_file(self, file_path):
        
        with open(file_path, 'r') as file:
            return yaml.safe_load(file)

    def reload_configs_callback(self, msg: String):

        self.control_config = self.load_yaml_file(self.control_config_path)
        self.get_logger().info("Kontroller-node har lastet in config!")

    # Callback-funksjon for å motta eta_sim-data fra simulatoren
    def eta_callback(self, msg: Eta):
        
        # Mottar posisjons- og orienteringsdata fra simulatoren
        self.eta = np.array([msg.lat, msg.lon, msg.z, msg.phi, msg.theta, msg.psi])

    # Callback-funksjon for å motta nu_sim-data fra simulatoren
    def nu_callback(self, msg: Nu):
        
        # Mottar hastighetsdata fra simulatoren
        self.nu = np.array([msg.u, msg.v, msg.w, msg.p, msg.q, msg.r])

    # Callback-funksjon for å motta eta_setpoint-data (settpunkt for posisjon og orientering)
    def eta_setpoint_callback(self, msg: Eta):
        
        # Mottar settpunktdata for posisjon og orientering
        self.eta_setpoint = np.array([msg.lat, msg.lon, msg.z, msg.phi, msg.theta, msg.psi])

    # Callback-funksjon for å motta nu_setpoint-data (settpunkt for hastighet)
    def nu_setpoint_callback(self, msg: Nu):
       
        # Mottar settpunktdata for hastigheter
        self.nu_setpoint = np.array([msg.u, msg.v, msg.w, msg.p, msg.q, msg.r])

    # Callback funktion til Eta estimation
    def eta_hat_callback(self, msg: Eta):
        self.eta_hat = np.array([msg.lat, msg.lon, msg.z, msg.phi, msg.theta, msg.psi])
    
    # Callback funktion til Nu estimation
    def nu_hat_callback(self, msg: Nu):
        self.nu_hat = np.array([msg.u, msg.v, msg.w, msg.p, msg.q, msg.r])
    
    # Callback funktion til Max thrust og moment
    def tau_max_callback(self,msg: Tau):
        self.max_surge    = msg.surge_x
        self.max_yaw      = msg.yaw_n

    # Funksjon som kjøres på hver simuleringstidssteg og implementerer kontrollalgoritmen
    def step_control(self):
        
        # Denne funksjonen vil inneholde kontrolllogikk for å beregne de nødvendige kreftene (tau)
        # Foreløpig brukes en enkel PD-kontroll (Propositional-Derivative) som eksempel

        ################## PID Heading #####################
        # Beregn avvik (feil) mellom settpunkt og faktisk verdi for både posisjon (eta) og hastighet (nu)
        e_psi     = mu.mapToPiPi(self.eta_setpoint[5] - self.eta_hat[5])
        e_psi_dot = self.nu_setpoint[5] - self.nu_hat[5]


        # Heading config
        omega                   = self.control_config['heading_control']['omega']
        zeta                    = self.control_config['heading_control']['zeta']
        ki_scale                = self.control_config['heading_control']['ki_scale']
        ki_sat_limit            = self.control_config['heading_control']['ki_saturation_limit']
        N_rr                    = self.control_config['heading_control']['N_rr']            # 
        linerearization_point   = self.control_config['heading_control']['linearization_point']
        self.heading_eps        = self.control_config['heading_control']['eps']
        dt                      = self.step_size

        # Vessel config
        mass                    = self.vessel_config['vessel']['mass']

        d_star                  = N_rr * linerearization_point

        kp_psi                  = mass * omega ** 2
        kd_psi                  = 2 * zeta * omega * mass - d_star
        ki_psi                  = kp_psi / (ki_scale + np.rad2deg(e_psi) ** 2)


        # Your integral windup handling for heading

        sat_e_psi               = mu.saturate(e_psi,-np.deg2rad(ki_sat_limit), np.deg2rad(ki_sat_limit))

        if (self.qi_psi >= self.heading_eps * self.max_yaw) and (sat_e_psi > 0) or (self.qi_psi <= self.heading_eps * self.max_yaw) and (sat_e_psi < 0):
            pass
        else:
            self.qi_psi += dt * sat_e_psi

        # PID Led
        P                       = kp_psi * e_psi
        I                       = ki_psi * self.qi_psi
        D                       = kd_psi * e_psi_dot

        # Heading kontroller
        tau_N                   = P + I + D
        sat_tau_N               = mu.saturate(tau_N, -self.heading_eps * self.max_yaw, self.heading_eps * self.max_yaw)


        ################## PI Fart #####################
        e_u = self.nu_setpoint[0] - self.nu[0]

        kp_u                    = self.control_config['speed_control']['K_p']
        ki_scale_u              = self.control_config['speed_control']['ki_scale']
        ki_sat_limit_u          = self.control_config['speed_control']['ki_saturation_limit']
        X_uu                    = self.control_config['speed_control']['X_uu']
        self.speed_eps          = self.control_config['speed_control']['eps']

        # Beregning af Ki_u
        ki_u                    = kp_u / (ki_scale_u + e_u ** 2)
        #self.qi_u              += dt * mu.saturate(e_u, -ki_sat_limit_u, ki_sat_limit_u)  
        sat_e_u                 = mu.saturate(e_u, -ki_sat_limit_u, ki_sat_limit_u) 

        if (self.qi_u >= self.speed_eps * self.max_surge) and (sat_e_u > 0) or (self.qi_u <= self.speed_eps * self.max_surge) and (sat_e_u < 0):
            pass
        else:
            self.qi_u += dt * sat_e_u

        # Kode for fartskontroller

        tau_X                   = X_uu * abs(self.nu_setpoint[0]) * self.nu[0] + kp_u * e_u + self.qi_u * ki_u
        sat_tau_X               = mu.saturate(tau_X, -self.speed_eps * self.max_surge, self.speed_eps * self.max_surge)

        
        current_time = time.time()
        if current_time - self.last_print_time >= 1.0:
                self.get_logger().info(f"Controller: Tau_X {tau_X}")
                self.get_logger().info(f"Controller: yaw_N {tau_N}")
                self.last_print_time = current_time  # Reset the timer

        # Opprett en Tau-melding for å sende de beregnede kreftene
        tau_message = Tau()
        tau_message.surge_x = tau_X
        tau_message.sway_y  = 0.0
        tau_message.heave_z = 0.0
        tau_message.roll_k  = 0.0
        tau_message.pitch_m = 0.0
        tau_message.yaw_n   = tau_N

        # Publiser kontrollkreftene på tau_propulsion-topic
        self.tau_control_pub.publish(tau_message)
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

