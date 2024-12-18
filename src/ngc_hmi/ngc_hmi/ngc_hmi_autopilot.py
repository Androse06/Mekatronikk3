import sys
import signal
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QFormLayout, QHBoxLayout, QPushButton, QLabel, QSpacerItem, QSizePolicy, QLCDNumber, QDial, QSlider
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QFont
import rclpy
from rclpy.node import Node
from ngc_interfaces.msg import Eta, Nu, HMI
from ngc_utils.qos_profiles import default_qos_profile
import numpy as np
import ngc_utils.math_utils as mu

class AutopilotHMI(Node):
    def __init__(self):
        super().__init__('ship_autopilot_hmi')

        # Initialize setpoints
        self.heading_setpoint = 0.5  # Initial heading setpoint
        self.surge_setpoint   = 0.0  # Initial surge speed setpoint in knots
        self.mode_label = 'init'
        self.mode = 0

        self.debug = False

        # Subscribers to eta_sim and nu_sim
        self.create_subscription(Eta, 'eta_sim', self.update_eta_feedback, default_qos_profile)
        self.create_subscription(Nu, 'nu_sim', self.update_nu_feedback, default_qos_profile)
        self.create_subscription(HMI, 'hmi', self.hmi_callback, default_qos_profile)
        # Publishers for eta_setpoint and nu_setpoint
        #self.eta_publisher = self.create_publisher(Eta, 'eta_setpoint', default_qos_profile)
        #self.nu_publisher = self.create_publisher(Nu, 'nu_setpoint', default_qos_profile)

        #### System mode publisher ####
        self.mode_publisher = self.create_publisher(HMI, 'hmi', default_qos_profile)

        # Initialize the UI
        self.init_ui()

    def init_ui(self):
        self.app = QApplication(sys.argv)
        self.window = QWidget()
        self.window.setWindowTitle("Ship Autopilot HMI")
        self.layout = QVBoxLayout()

        # Heading setpoint with a continuous wheel (QDial)
        self.add_wheel_layout('Heading', 0, 360, '°', self.update_heading_setpoint)

        # Surge speed setpoint with finer granularity in knots
        self.add_slider_layout('Surge Speed', 0, 6, 'knots', self.update_surge_setpoint, resolution=0.1)


        ##### Knapper: HMI #####

        gpx_recall_button = QHBoxLayout()

        self.reload_button = QPushButton('load route')
        self.reload_button.clicked.connect(self.parse_gpx_file)
        gpx_recall_button.addWidget(self.reload_button)

        button_layout = QHBoxLayout()
        
        self.label = QLabel(f'Mode: {self.mode_label}')

        self.standby_button = QPushButton('Standby')
        self.standby_button.clicked.connect(self.set_standby_mode)
        button_layout.addWidget(self.standby_button)

        self.position_button = QPushButton('Position')
        self.position_button.clicked.connect(self.set_position_mode)
        button_layout.addWidget(self.position_button)

        self.sail_button = QPushButton('Sail')
        self.sail_button.clicked.connect(self.set_sail_mode)
        button_layout.addWidget(self.sail_button)

        self.track_button = QPushButton('Track')
        self.track_button.clicked.connect(self.set_track_mode)
        button_layout.addWidget(self.track_button)

        self.layout.addLayout(gpx_recall_button)
        self.layout.addWidget(self.label)
        self.layout.addLayout(button_layout)

        ########################################
        
        
        self.window.setLayout(self.layout)
        self.window.show()

        # Timer to process ROS 2 callbacks and publish setpoints regularly
        self.timer = QTimer()
        self.timer.timeout.connect(self.ros_spin_and_publish_setpoints)
        self.timer.start(100)  # 100 ms interval (10 Hz)


    ####### Knapper: funksjon #######

    def parse_gpx_file(self):
        mode_message = HMI()
        mode_message.route = True
        self.mode_publisher.publish(mode_message)
        self.get_logger().info('gpx reload')

    def set_standby_mode(self):
        self.mode = 0
        self.publish_setpoints()
        self.get_logger().info('Standby mode activated')

    def set_sail_mode(self):
        self.mode = 1
        self.publish_setpoints()
        self.get_logger().info('Sail mode activated')

    def set_position_mode(self):
        self.mode = 2
        self.publish_setpoints()
        self.get_logger().info('Position mode activated')

    def set_track_mode(self):
        self.mode = 3
        self.publish_setpoints()
        self.get_logger().info('Track mode activated')

    ########################################


    def ros_spin_and_publish_setpoints(self):
        # Spin ROS 2 callbacks to handle incoming messages
        rclpy.spin_once(self, timeout_sec=0.1)

        if self.mode == 0:
            self.mode_label = 'Standby'
            self.label.setText(f'Mode: {self.mode_label}')
        elif self.mode == 1:
            self.mode_label = 'Sail'
            self.label.setText(f'Mode: {self.mode_label}')
        elif self.mode == 2:
            self.mode_label = 'Position'
            self.label.setText(f'Mode: {self.mode_label}')
        elif self.mode == 3:
            self.mode_label = 'Track'
            self.label.setText(f'Mode: {self.mode_label}')

        # Publish the current setpoints regularly
        #self.publish_setpoints() kommentert ut kontinuerlig publishing

    def add_wheel_layout(self, label_text, min_val, max_val, unit, update_method):
        wheel_layout = QVBoxLayout()

        label = QLabel(f'{label_text} ({unit})')
        label.setAlignment(Qt.AlignCenter)
        wheel_layout.addWidget(label)

        dial = QDial()
        dial.setMinimum(min_val)
        dial.setMaximum(max_val)
        dial.setWrapping(True)  # Enable wrapping to allow continuous rotation
        dial.setValue(180)  # Start at 180 degrees (which maps to north)
        dial.setNotchesVisible(True)
        dial.valueChanged.connect(lambda value: self.handle_heading_wraparound(self.remap_dial_value(value), update_method))
        wheel_layout.addWidget(dial)

        lcd_display = QLCDNumber()
        lcd_display.setSegmentStyle(QLCDNumber.Flat)
        lcd_display.setDigitCount(6)
        dial.valueChanged.connect(lambda value: lcd_display.display(self.remap_dial_value(value)))
        wheel_layout.addWidget(lcd_display)

        self.layout.addLayout(wheel_layout)
        self.layout.addItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))

        dial.valueChanged.connect(self.eta_dial) # publisher ved endret verdi

    def eta_dial(self):
        self.publish_setpoints()


    def remap_dial_value(self, value):
        # Remap the dial so that 0 at the top is north (0°)
        remapped_value = (value - 180) % 360
        return remapped_value

    def add_slider_layout(self, label_text, min_val, max_val, unit, update_method, resolution=1.0):
        slider_layout = QVBoxLayout()

        label = QLabel(f'{label_text} ({unit})')
        label.setAlignment(Qt.AlignCenter)
        slider_layout.addWidget(label)

        slider = QSlider(Qt.Horizontal)
        slider.setMinimum(int(min_val / resolution))
        slider.setMaximum(int(max_val / resolution))
        slider.setValue((min_val + max_val) // 2)
        slider.setTickPosition(QSlider.TicksBelow)
        slider.setTickInterval(int(1 / resolution))
        slider.valueChanged.connect(lambda value: update_method(value * resolution))
        slider_layout.addWidget(slider)

        lcd_display = QLCDNumber()
        lcd_display.setSegmentStyle(QLCDNumber.Flat)
        lcd_display.setDigitCount(6)
        lcd_display.display(slider.value() * resolution)
        slider.valueChanged.connect(lambda value: lcd_display.display(value * resolution))
        slider_layout.addWidget(lcd_display)

        self.layout.addLayout(slider_layout)
        self.layout.addItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))

        slider.valueChanged.connect(self.nu_slider) # publisher ved endret verdi

    def nu_slider(self):
        self.publish_setpoints()

    def handle_heading_wraparound(self, current_value, update_method):
        update_method(current_value)

    def update_eta_feedback(self, msg):
        # Handle the incoming Eta message from eta_sim
        pass  # Visualization of the feedback can be added here

    def update_nu_feedback(self, msg):
        # Handle the incoming Nu message from nu_sim
        pass  # Visualization of the feedback can be added here

    def hmi_callback(self, msg: HMI):
        self.mode = msg.mode

        if msg.mode == 0:
            self.get_logger().info('Standby mode activated')
        elif msg.mode == 1:
            self.get_logger().info('Sail mode activated')
        elif msg.mode == 2:
            self.get_logger().info('Position mode activated')
        elif msg.mode == 3:
            self.get_logger().info('Track mode activated')
        
        if self.debug:
            self.get_logger().info('hmi_callback active')
            self.get_logger().info(f'hmi_callback mode setpoint {msg.mode}')

    def update_heading_setpoint(self, value):
        # Update the heading setpoint value
        self.heading_setpoint = value

    def update_surge_setpoint(self, value):
        # Update the surge speed setpoint value (knots)
        self.surge_setpoint = value

    def publish_setpoints(self):
        # Convert heading to radians and publish Eta setpoint
        hmi_msg = HMI()
        hmi_msg.mode = self.mode
        hmi_msg.eta = float(mu.mapToPiPi(np.deg2rad(self.heading_setpoint)))  # Convert degrees to radians and map 2 plus minus pi
        hmi_msg.nu = float(self.surge_setpoint) * 0.514444
        self.mode_publisher.publish(hmi_msg)

        if self.debug:
            self.get_logger().info('hmi_publisher')
            self.get_logger().info(f'hmi_publisher, mode: {self.mode}')

def main(args=None):
    rclpy.init(args=args)

    # Create the AutopilotHMI node
    autopilot_hmi = AutopilotHMI()

    # Set up a QTimer to spin the ROS2 node and handle callbacks
    timer = QTimer()
    timer.timeout.connect(lambda: rclpy.spin_once(autopilot_hmi, timeout_sec=0.1))
    timer.start(100)  # Call every 100 ms

    # Handle signal for graceful shutdown
    def signal_handler(sig, frame):
        print("SIGINT received, shutting down...")
        autopilot_hmi.destroy_node()
        rclpy.shutdown()
        QApplication.quit()

    signal.signal(signal.SIGINT, signal_handler)

    # Start the PyQt5 application event loop
    sys.exit(autopilot_hmi.app.exec_())


if __name__ == '__main__':
    main()
