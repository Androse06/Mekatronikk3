#Importerer nødvendige biblioteker og moduler for ROS2
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


class kontroller(Node):
    def __init__(self):
        super().__init__("kontroller")

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
        self.vessel_mass = self.vessel_config['vessel']['mass']
        
        # Henter simulasjonens tidssteg fra konfigurasjonsfilen
        self.step_size = self.simulation_config['simulation_settings']['step_size']

        # Setter opp abonnenter for å lytte på data fra simulatoren (eta og nu) og settpunkter (eta_setpoint, nu_setpoint)
        #self.eta_sub                = self.create_subscription(Eta, 'eta_sim', self.eta_callback, default_qos_profile)
        #self.nu_sub                 = self.create_subscription(Nu, 'nu_sim', self.nu_callback, default_qos_profile)
        self.eta_hat_sub            = self.create_subscription(Eta, 'eta_hat', self.eta_callback, default_qos_profile)
        self.nu_hat_sub             = self.create_subscription(Nu, 'nu_hat', self.nu_callback, default_qos_profile)
        self.eta_setpoint_sub       = self.create_subscription(Eta, 'eta_setpoint', self.eta_setpoint_callback, default_qos_profile)
        self.nu_setpoint_sub        = self.create_subscription(Nu, 'nu_setpoint', self.nu_setpoint_callback, default_qos_profile)
        self.reload_configs_sub     = self.create_subscription(String, 'reload_configs', self.reload_configs_callback, default_qos_profile)
        self.tau_max_sub            = self.create_subscription(Tau, 'tau_max', self.tau_max_callback, default_qos_profile)
        
        # Setter opp en publisher for å publisere kontrollsignalene (tau_propulsion)
        #self.tau_pub                = self.create_publisher(Tau, 'tau_propulsion', default_qos_profile)
        self.tau_control_pub       = self.create_publisher(Tau, 'tau_control', default_qos_profile)

        # Initialiserer variabler for å lagre data fra simulatoren og settpunkter
        self.eta          = np.zeros(6)
        self.nu           = np.zeros(6)
        self.eta_setpoint = np.zeros(6)
        self.nu_setpoint  = np.zeros(6)

        # Integraltilstander i PID kontroll
        self.qi_psi = 0.0
        self.qi_u   = 0.0

        # Starter kontroll-løkken som kjører med samme tidssteg som simulatoren
        # Her må du starte kontrolløkken

        # Heading variabler fra config fila
        self.omega_heading                  = self.control_config['heading_control']['omega']
        self.zeta_heading                   = self.control_config['heading_control']['zeta']
        self.ki_scale_heading               = self.control_config['heading_control']['ki_scale']
        self.ki_saturation_limit_heading    = np.radians(self.control_config['heading_control']['ki_saturation_limit'])
        self.N_rr_heading                   = self.control_config['heading_control']['N_rr']
        self.linearization_point_heading    = self.control_config['heading_control']['linearization_point']
        self.heading_eps                    = self.control_config['heading_control']['eps'] 

        # Hastighets variabler fra config fila
        self.K_p_speed                      = self.control_config['speed_control']['K_p']
        self.ki_scale_speed                 = self.control_config['speed_control']['ki_scale']
        self.ki_saturation_limit_speed      = self.control_config['speed_control']['ki_saturation_limit']
        self.X_uu_speed                     = self.control_config['speed_control']['X_uu']
        self.speed_eps                      = self.control_config['speed_control']['eps'] 


        # Variabler
        self.fram_max_thrust    = 0
        self.bak_max_thrust     = 0
        self.total_max_moment   = 0

        self.get_logger().info("Kontroller-node er initialisert.")

        # Start the control loop that runs at the same timestep as the simulator
        self.timer = self.create_timer(self.step_size, self.step_control)


    # Funksjon for å laste inn YAML-konfigurasjonsfiler
    def load_yaml_file(self, file_path):
        
        with open(file_path, 'r') as file:
            return yaml.safe_load(file)

    def tau_max_callback(self, msg: Tau):
        self.fram_max_thrust    = msg.surge_x
        self.bak_max_thrust     = msg.sway_y
        self.total_max_moment   = msg.yaw_n

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

    # Funksjon som kjøres på hver simuleringstidssteg og implementerer kontrollalgoritmen
    def step_control(self):
        
        ################## PID Heading #####################
        # Beregn avvik (feil) mellom settpunkt og faktisk verdi for både posisjon (eta) og hastighet (nu)
        e_psi     = mu.mapToPiPi(self.eta_setpoint[5] - self.eta[5])
        e_psi_dot = self.nu_setpoint[5] - self.nu[5]

        # PID Controller for heading (yaw)
        d_s = self.N_rr_heading * self.linearization_point_heading

        kp_psi = self.vessel_mass * (self.omega_heading ** 2)
        ki_psi = (kp_psi) / (self.ki_scale_heading + np.rad2deg(e_psi)**2)
        kd_psi = 2 * self.zeta_heading * self.omega_heading * self.vessel_mass - d_s

        # Calculate integral term for heading
        #self.qi_psi += self.step_size * mu.saturate(e_psi, -self.ki_saturation_limit_heading, self.ki_saturation_limit_heading)

         # Your integral windup handling for heading
        if e_psi > 1:
            self.sat_e_psi = 1
        elif e_psi < -1:
            self.sat_e_psi = -1
        else:
            self.sat_e_psi = e_psi

        if ((self.qi_psi > self.heading_eps * self.total_max_moment) and (e_psi > 0)) or ((self.qi_psi < -self.heading_eps * self.total_max_moment) and (e_psi < 0)):
            self.qi_psi += 0
        else:
            self.qi_psi += self.step_size * ki_psi * self.sat_e_psi

        # Compute control action (PID formula)
        tau_N = kp_psi * e_psi + ki_psi * self.qi_psi + kd_psi * e_psi_dot 


        ################## PI Fart #####################
        e_u = self.nu_setpoint[0] - self.nu[0]

        # PI Controller for surge (forward speed)
        kp_u = self.K_p_speed
        ki_u = kp_u / (self.ki_scale_speed + (e_u ** 2))

        # Calculate integral term for speed
        #self.qi_u += self.step_size * mu.saturate(e_u, -self.ki_saturation_limit_speed, self.ki_saturation_limit_speed)

        # Your integral windup handling for speed
        if e_u > 1:
            self.sat_e_u = 1
        elif e_u < -1:
            self.sat_e_u = -1
        else:
            self.sat_e_u = e_u

        if ((self.qi_u > self.speed_eps * self.fram_max_thrust) and (e_u > 0)) or ((self.qi_u < -self.speed_eps * self.bak_max_thrust) and (e_u < 0)):
            self.qi_u += 0
        else:
            self.qi_u += self.step_size * ki_u * self.sat_e_u

        # Compute control action (PI formula)
        tau_X = (self.X_uu_speed * abs(self.nu_setpoint[0]) * self.nu[0]) + (kp_u * e_u) + (ki_u * self.qi_u)


        ################## Publisering #####################
        
        # Opprett en Tau-melding for å sende de beregnede kreftene
        tau_message = Tau()
        tau_message.surge_x = tau_X
        tau_message.sway_y  = 0.0
        tau_message.heave_z = 0.0
        tau_message.roll_k  = 0.0
        tau_message.pitch_m = 0.0
        tau_message.yaw_n   = tau_N

        # Publiser kontrollkreftene på tau_propulsion-topic
        #self.get_logger().info("Kontrollkrefter publisert på tau_propulsion.")
        #self.get_logger().info(f"Controller: e_psi={e_psi}, e_u={e_u}")
        #self.get_logger().info(f"PID Heading Output: tau_N={tau_N}")
        #self.get_logger().info(f"PI Speed Output: tau_X={tau_X}")

        #self.tau_pub.publish(tau_message)
        self.tau_control_pub.publish(tau_message)
    
# Hovedfunksjonen som starter ROS2-noden
def main(args=None):
    
    # Initialiserer ROS2-kommunikasjon
    rclpy.init(args=args)
    node = kontroller()
    
    # Kjører noden til den stoppes
    rclpy.spin(node)
    
    # Når noden avsluttes, frigjør ressurser
    node.destroy_node()
    rclpy.shutdown()

# Starter hovedfunksjonen hvis denne filen kjøres som et skript
# Main funksjon
if __name__ == '__main__':
    main()


