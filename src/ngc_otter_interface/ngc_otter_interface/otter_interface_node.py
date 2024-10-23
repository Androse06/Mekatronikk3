import rclpy
from rclpy.node import Node
from std_msgs.msg import Bool
from ngc_interfaces.msg import ThrusterSignals, SystemMode, GNSS, HeadingDevice
from ngc_utils.qos_profiles import default_qos_profile
import copy

class OtterUSVNode(Node):
    def __init__(self):
        super().__init__('otter_usv_node')
        
        self.simulation = True  # Set this to control simulation mode

        # Thrusters
        self.thruster_1_sub = self.create_subscription(ThrusterSignals, 'thruster_1_setpoints', self.thruster_1_setpoints_callback, default_qos_profile)
        self.thruster_2_sub = self.create_subscription(ThrusterSignals, 'thruster_2_setpoints', self.thruster_2_setpoints_callback, default_qos_profile)
        self.thruster_1_pub = self.create_publisher(ThrusterSignals, 'thruster_1_feedback', default_qos_profile)
        self.thruster_2_pub = self.create_publisher(ThrusterSignals, 'thruster_2_feedback', default_qos_profile)

        # Sensors
        self.gnss_pub    = self.create_publisher(GNSS, 'gnss_measurement', default_qos_profile)
        self.heading_pub = self.create_publisher(HeadingDevice, 'heading_measurement', default_qos_profile)
        
        # Mode
        self.system_mode_sub = self.create_subscription(SystemMode, 'system_mode', self.system_mode_callback, default_qos_profile)
        
        # Subscribers for simulated data if in simulation mode
        if self.simulation:

            # Thrusters
            self.thruster_1_sim_sub = self.create_subscription(ThrusterSignals, 'thruster_1_feedback_sim', self.thruster_1_sim_callback, default_qos_profile)
            self.thruster_2_sim_sub = self.create_subscription(ThrusterSignals, 'thruster_2_feedback_sim', self.thruster_2_sim_callback, default_qos_profile)
            self.thruster_1_sim_pub = self.create_publisher(ThrusterSignals, 'thruster_1_setpoints_sim', default_qos_profile)
            self.thruster_2_sim_pub = self.create_publisher(ThrusterSignals, 'thruster_2_setpoints_sim', default_qos_profile)

            # Sensors
            self.sim_gnss_sub    = self.create_subscription(GNSS, 'gnss_measurement_sim', self.gnss_sim_callback, default_qos_profile)
            self.sim_heading_sub = self.create_subscription(HeadingDevice, 'heading_measurement_sim', self.heading_sim_callback, default_qos_profile)


        # Timer to publish data at 10Hz
        self.timer = self.create_timer(0.1, self.publish_measurements)

        # Store the latest messages
        self.latest_thruster_1_setpoints = None
        self.latest_thruster_2_setpoints = None
        self.latest_thruster_1_feedback  = None
        self.latest_thruster_2_feedback  = None
        self.latest_system_mode          = None
        self.latest_gnss_data            = None
        self.latest_heading_data         = None

    def thruster_1_setpoints_callback(self, msg):
        self.latest_thruster_1_setpoints = msg

    def thruster_2_setpoints_callback(self, msg):
        self.latest_thruster_2_setpoints = msg 
    
    def system_mode_callback(self, msg):
        self.latest_system_mode = msg

    def thruster_1_sim_callback(self, msg):
        self.latest_thruster_1_feedback = msg

    def thruster_2_sim_callback(self, msg):
        self.latest_thruster_2_feedback = msg 

    def gnss_sim_callback(self, msg):
        self.latest_gnss_data = msg

    def heading_sim_callback(self, msg):
        self.latest_heading_data = msg
        
    def publish_measurements(self):
        
        if self.latest_system_mode is None:
            return 
       
        if self.latest_system_mode.auto_mode == True and self.latest_system_mode.standby_mode == False:
            # From interface to control system 
            if self.latest_thruster_1_feedback:
                self.thruster_1_pub.publish(self.latest_thruster_1_feedback)
                self.latest_thruster_1_feedback = None

            # From interface to control system 
            if self.latest_thruster_2_feedback:
                self.thruster_2_pub.publish(self.latest_thruster_2_feedback)
                self.latest_thruster_2_feedback = None

        elif self.latest_system_mode.standby_mode == True:
            self.latest_thruster_1_setpoints.active = False
            self.latest_thruster_1_setpoints.active = False

        # From interface to control system 
        if self.latest_gnss_data:
            self.gnss_pub.publish(self.latest_gnss_data)
            self.latest_gnss_data = None

        # From interface to control system 
        if self.latest_heading_data:
            self.heading_pub.publish(self.latest_heading_data)
            self.latest_heading_data = None

        if self.simulation:
            
            # From allocator setpoints to simulator
            if self.latest_thruster_1_setpoints:
                self.thruster_1_sim_pub.publish(self.latest_thruster_1_setpoints)
                self.latest_thruster_1_setpoints = None

            # From allocator setpoints to simulator
            if self.latest_thruster_2_setpoints:
                self.thruster_2_sim_pub.publish(self.latest_thruster_2_setpoints)
                self.latest_thruster_2_setpoints = None
            
        else:
            
            # Push into data over tcp/ip to Otter
            pass
        

def main(args=None):
    rclpy.init(args=args)
    node = OtterUSVNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
