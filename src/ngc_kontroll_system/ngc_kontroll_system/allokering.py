import rclpy
from rclpy.node import Node
import numpy as np
import os
import yaml
from ngc_interfaces.msg import HeadingDevice, GNSS, Eta, Nu, Tau, ThrusterSignals
from ament_index_python.packages import get_package_share_directory
from ngc_utils.vessel_model import VesselModel
from ngc_utils.qos_profiles import default_qos_profile
import time
import ngc_utils.math_utils as mu
from std_msgs.msg import String
import ngc_utils.geo_utils as geos


class allokering(Node):
    def __init__(self):
        super().__init__("allokering")

        ##### YAML CONFIGURATION #####

        # Deklarerer og laster konfigurasjonsparametere fra YAML-filer
        self.declare_parameter('yaml_package_name', 'ngc_bringup')
        self.declare_parameter('propulsion_config', 'config/propulsion_config.yaml')
        
        # Henter konfigurasjonsfilenes stier ved hjelp av pakkenavnet
        yaml_package_name        = self.get_parameter('yaml_package_name').get_parameter_value().string_value
        yaml_package_path        = get_package_share_directory(yaml_package_name)
        propulsion_config_path   = os.path.join(yaml_package_path, self.get_parameter('propulsion_config').get_parameter_value().string_value)
        
        # Laster YAML-konfigurasjonsfiler som inneholder informasjon om fartøyet og simuleringen
        self.propulsion_config  = self.load_yaml_file(propulsion_config_path)

        ##### SUBSCRIBER AND PUBLISHER #####

        # Abonnenter
        self.tau_control_sub    = self.create_subscription(Tau, 'tau_control', self.tau_control_callback, default_qos_profile)

        # Publisher to eta_hat and nu_hat
        self.thruster_1_pub     = self.create_publisher(ThrusterSignals, 'thruster_1_setpoints', default_qos_profile)
        self.thruster_2_pub     = self.create_publisher(ThrusterSignals, 'thruster_2_setpoints', default_qos_profile)
        self.tau_max_pub        = self.create_publisher(Tau, 'tau_max', default_qos_profile)

        # Variabler:
        self.X = 0
        self.Y = 0
        self.N = 0

        # Laster in thruster data
        self.load_thruster_data()
        # Rekner ut max thrust og moment fra yaml
        self.Maxpower()


    def tau_control_callback(self, msg: Tau):
        self.X = msg.surge_x
        self.Y = msg.sway_y
        self.N = msg.yaw_n

        self.Allokering()
        # Rekner ut max thrust og moment fra yaml
        self.Maxpower()


    def load_yaml_file(self, file_path):
        with open(file_path, 'r') as file:
            return yaml.safe_load(file)
        
    def load_thruster_data(self):
        main_propulsion_1   = self.propulsion_config['main_propulsion_1']
        self.T1_id          = main_propulsion_1['id']
        self.T1_position    = main_propulsion_1['position']
        self.T1_type        = main_propulsion_1['type']
        self.T1_Kt0         = main_propulsion_1['propeller']['Kt0']
        self.T1_diameter    = main_propulsion_1['propeller']['diameter']
        self.T1_max_rpm     = main_propulsion_1['propeller']['max_rpm']
        self.T1_min_rpm     = main_propulsion_1['propeller']['min_rpm']
        self.T1_max_rps     = (self.T1_max_rpm) / 60
        self.T1_min_rps     = (self.T1_min_rpm) / 60

        main_propulsion_2   = self.propulsion_config['main_propulsion_2']
        self.T2_id          = main_propulsion_2['id']
        self.T2_position    = main_propulsion_2['position']
        self.T2_type        = main_propulsion_2['type']
        self.T2_Kt0         = main_propulsion_2['propeller']['Kt0']
        self.T2_diameter    = main_propulsion_2['propeller']['diameter']
        self.T2_max_rpm     = main_propulsion_2['propeller']['max_rpm']
        self.T2_min_rpm     = main_propulsion_2['propeller']['min_rpm']
        self.T2_max_rps     = (self.T2_max_rpm) / 60
        self.T2_min_rps     = (self.T2_min_rpm) / 60


    def Maxpower(self):
        ##### THRUST UTREKNING #####
        T1_max_thrust_fram      = (0.5) * (1025 * self.T1_Kt0 * (self.T1_diameter**4) * (self.T1_max_rps**2))
        T2_max_thrust_fram      = (0.5) * (1025 * self.T2_Kt0 * (self.T2_diameter**4) * (self.T2_max_rps**2))

        self.fram_max_thrust    = T1_max_thrust_fram + T2_max_thrust_fram

        T1_max_thrust_bak       = (0.5) * (1025 * self.T1_Kt0 * (self.T1_diameter**4) * (self.T1_min_rps**2))
        T2_max_thrust_bak       = (0.5) * (1025 * self.T2_Kt0 * (self.T2_diameter**4) * (self.T2_min_rps**2))

        self.bak_max_thrust     = T1_max_thrust_bak + T2_max_thrust_bak

        ##### MOMENT UTREKNING #####
        T2_L                    = abs(self.T2_position[1])
        T1_L                    = abs(self.T1_position[1])
        T1_Moment               = T1_max_thrust_fram * T1_L
        T2_Moment               = T2_max_thrust_bak  * T2_L

        self.totalt_max_moment  = T1_Moment + T2_Moment

        tau_max_msg = Tau()
        tau_max_msg.surge_x = self.fram_max_thrust
        tau_max_msg.sway_y  = self.bak_max_thrust
        tau_max_msg.heave_z = 0.0
        tau_max_msg.roll_k  = 0.0
        tau_max_msg.pitch_m  = 0.0
        tau_max_msg.yaw_n   = self.totalt_max_moment
        self.tau_max_pub.publish(tau_max_msg)

    def Allokering(self):
        ####### FRA ALLOKERING PROGRAM ######

        ##### Variabler for thruster #####
        #Thruster 1
        T1_S    = 1
    
        #Thruster 2
        T2_S    = 1
        
        rho = 1025

        ##### Simulerings U verdier #####
        X = self.X
        Y = self.Y
        N = self.N

        u = np.array([X, Y, N])

        ### Funksjon for konvertering fra kraft til rps, Di er prop diameter ###
        def rpskalk(x, y, thruster):

            if thruster == 'T1':
                Di      = self.T1_diameter
                KT      = self.T1_Kt0
                max_rps = self.T1_max_rps
                min_rps = self.T1_min_rps
            
            elif thruster == 'T2':
                Di      = self.T2_diameter
                KT      = self.T2_Kt0
                max_rps = self.T2_max_rps
                min_rps = self.T2_min_rps
            
            else:
                return 0
            
            kraft = np.sqrt(x**2 + y**2)
            rps = np.sign(kraft) * np.sqrt((abs(kraft) * 2) / (rho * KT * Di**4))

            if rps > max_rps:
                rps = max_rps

            elif rps < min_rps:
                rps = min_rps

            return rps

        ### Funksjon for å rekne ut vinkel til thruster ###
        def rot(x, y):
            if x == 0:
                vinkel = 0
            else:
                vinkel = np.arctan(y / x)
            return vinkel

        ##### Te matrise "Thrustmatrise" #####
        TE = np.array([[1,   0,  1,   0],
                       [0,   1,  0,   1],
                       [abs(self.T1_position[1]), 0, -abs(self.T2_position[1]), 0]])

        ##### W matrise for aktive thruster #####
        W = np.array([[T1_S, 0, 0, 0],
                      [0, T1_S, 0, 0],
                      [0, 0, T2_S, 0],
                      [0, 0, 0, T2_S]])

        T_W = np.linalg.inv(W) @ TE.T @ np.linalg.inv(TE @ np.linalg.inv(W) @ TE.T)

        f_e = T_W @ u

        rps = np.array([rpskalk(f_e[0], f_e[1], 'T1'), rpskalk(f_e[2], f_e[3], 'T2')])
        vinkel = np.array([rot(f_e[0], f_e[1]), rot(f_e[2], f_e[3])])

        u_rekna = TE @ f_e

        thruster_1_msg  = ThrusterSignals()
        thruster_1_msg.thruster_id  = self.T1_id
        thruster_1_msg.rps          = rps[0]
        thruster_1_msg.pitch        = 0.0 #Fast propell
        thruster_1_msg.azimuth_deg  = 0.0 #np.degrees(vinkel[0])
        thruster_1_msg.active       = True
        thruster_1_msg.error        = False

        thruster_2_msg  = ThrusterSignals()
        thruster_2_msg.thruster_id  = self.T2_id
        thruster_2_msg.rps          = rps[1]
        thruster_2_msg.pitch        = 0.0 #Fast propell
        thruster_2_msg.azimuth_deg  = 0.0 #np.degrees(vinkel[1])
        thruster_2_msg.active       = True
        thruster_2_msg.error        = False

        self.thruster_1_pub.publish(thruster_1_msg)
        self.thruster_2_pub.publish(thruster_2_msg)



      

# Hovedfunksjonen som starter ROS2-noden
def main(args=None):
    # Initialiserer ROS2-kommunikasjon
    rclpy.init(args=args)
    node = allokering()

    # Kjører noden til den stoppes
    rclpy.spin(node)

    # Når noden avsluttes, frigjør ressurser
    node.destroy_node()
    rclpy.shutdown()

# Starter hovedfunksjonen hvis denne filen kjøres som et skript
if __name__ == '__main__':
    main()



