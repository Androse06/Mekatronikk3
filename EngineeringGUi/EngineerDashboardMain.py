### Import for PyQt ###
from PySide6.QtWidgets import QApplication, QMainWindow
from EngineeringDashboard import Ui_MainWindow  # Import your generated UI file
import sys

### Import for ros ###
import signal
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QFormLayout, QHBoxLayout, QPushButton, QLabel, QSpacerItem, QSizePolicy, QLCDNumber, QDial, QSlider
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QFont
import rclpy
from rclpy.node import Node
from ngc_interfaces.msg import Eta, Nu, Mode
from ngc_utils.qos_profiles import default_qos_profile
import numpy as np
import ngc_utils.math_utils as mu


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()


        ##### ROS MILJØ #####

        # Initialize setpoints
        self.heading_setpoint = 0.5  # Initial heading setpoint
        self.surge_setpoint   = 0.0  # Initial surge speed setpoint in knots
        self.mode_label = 'init'

        # Subscribe to eta_sim and nu_sim
        self.create_subscription(Eta, 'eta_sim', self.update_eta_feedback, default_qos_profile)
        self.create_subscription(Nu, 'nu_sim', self.update_nu_feedback, default_qos_profile)

        # Publishers for eta_setpoint and nu_setpoint
        self.eta_publisher = self.create_publisher(Eta, 'eta_setpoint', default_qos_profile)
        self.nu_publisher = self.create_publisher(Nu, 'nu_setpoint', default_qos_profile)

        # System mode publisher
        self.mode_publisher = self.create_publisher(Mode, 'mode', default_qos_profile)



        ##### PyQt Dashboard #####

        # Create an instance of the Ui_MainWindow
        self.ui = Ui_MainWindow()

        # Set up the UI
        self.ui.setupUi(self)

        # Connect sliders/dials to methods
        self.ui.Sail_Throttle_Slider.valueChanged.connect(self.update_sail_throttle)
        self.ui.Sail_Heading_Dial.valueChanged.connect(self.update_sail_heading)

        # Set initial values (optional)
        self.set_sail_throttle_value(50)
        self.set_sail_heading_value(180)

        # Connect buttons to methods
        self.ui.Enable_Sail_Button.clicked.connect(self.enable_sail)
        self.ui.Enable_Standby_Button.clicked.connect(self.enable_standby)

    # Method to handle sail throttle slider value changes
    def update_sail_throttle(self, value):
        self.sail_throttle_value = value
        print(f"Sail Throttle Slider value updated to: {self.sail_throttle_value}")

        # Update the LCD display to show the current value
        self.ui.Sail_Throttle_LCD.display(self.sail_throttle_value)

    # Method to programmatically set the sail throttle slider's value
    def set_sail_throttle_value(self, value):
        self.ui.Sail_Throttle_Slider.setValue(value)
        print(f"Sail Throttle Slider set to: {value}")

    # Method to handle sail heading dial value changes
    def update_sail_heading(self, value):
        self.sail_heading_value = value
        print(f"Sail Heading Dial value updated to: {self.sail_heading_value}")

        # Update the LCD display to show the current heading
        self.ui.Sail_Heading_LCD.display(self.sail_heading_value)

    # Method to programmatically set the sail heading dial's value
    def set_sail_heading_value(self, value):
        self.ui.Sail_Heading_Dial.setValue(value)
        print(f"Sail Heading Dial set to: {value}")

    # Method to handle the Enable Sail button click
    def enable_sail(self):
        print("Enable Sail button clicked")
        # You can add logic here to enable sail functionality

    # Method to handle the Enable Standby button click
    def enable_standby(self):
        print("Enable Standby button clicked")
        # You can add logic here to enable standby functionality

    # You can add similar methods for other widgets as needed

if __name__ == "__main__":
    # Create the application object
    app = QApplication(sys.argv)

    # Create an instance of the MainWindow and show it
    window = MainWindow()
    window.show()

    # Start the application's event loop
    sys.exit(app.exec())
