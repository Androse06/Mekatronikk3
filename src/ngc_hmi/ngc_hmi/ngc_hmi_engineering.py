### Import for PyQt ###
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QStringListModel, QTimer
from EngineeringDashboard import Ui_MainWindow  # Import your generated UI file
import sys

### Import for Ros ###
import rclpy
from rclpy.node import Node
from ngc_interfaces.msg import HMI
from ngc_utils.qos_profiles import default_qos_profile
import numpy as np
import ngc_utils.math_utils as mu
import signal


###


class EngineeringHMI(Node):
    def __init__(self):
        super().__init__('ngc_engineering_hmi')

        #### System mode publisher ####
        self.hmi_publisher = self.create_publisher(HMI, 'hmi', default_qos_profile)

        # Initialize the UI
        self.init_ui()

    def init_ui(self):

        self.ui = Ui_MainWindow()

        # Create an instance of the MainWindow and show it
        self.window = QMainWindow()
        self.ui.setupUi(self.window)
        self.window.show()


        # Start Values
        self.ui.Standby_Status_Icon.setValue(int(100))
        self.ui.Sail_Status_Icon.setValue(int(0))
        self.ui.Dp_Status_Icon.setValue(int(0))
        self.ui.Track_Status_Icon.setValue(int(0))
        
        # Set initial values (optional)
        self.set_sail_throttle_value(0)
        self.set_sail_heading_value(180)


        # Connect sliders/dials to methods
        self.ui.Sail_Throttle_Slider.valueChanged.connect(self.update_sail_throttle)
        self.ui.Sail_Heading_Dial.valueChanged.connect(self.update_sail_heading)
        


        # Connect buttons to methods
        self.ui.Enable_Standby_Button.clicked.connect(self.enable_standby)
        self.ui.Enable_Sail_Button.clicked.connect(self.enable_sail)
        self.ui.Enable_Dp_Button.clicked.connect(self.enable_dp)
        self.ui.Enable_Track_Button.clicked.connect(self.enable_track)
        self.ui.Dp_Load_Button.pressed.connect(self.load_dp)
        self.ui.Dp_Load_Button.released.connect(self.disable_dp_load)
        self.ui.Track_Load_Button.pressed.connect(self.load_track)
        self.ui.Track_Load_Button.released.connect(self.disable_track_load)
        self.ui.Clear_Waypoint_Button.clicked.connect(self.clear_waypoint)
       
        # Connect Inputs
        self.ui.Lon_Input_Dp.textChanged.connect(self.retrieve_dp_input)
        self.ui.Lat_Input_Dp.textChanged.connect(self.retrieve_dp_input)
        self.ui.Lat_Input_Track.textChanged.connect(self.retrieve_track_input)
        self.ui.Lon_Input_Track.textChanged.connect(self.retrieve_track_input)
        
        # Setter opp waypoint list
        self.waypoint_model = QStringListModel()
        self.ui.WayPoint_ListView.setModel(self.waypoint_model)
        self.ui.Add_WayPoint_Button.clicked.connect(self.add_waypoint)



    def add_waypoint(self):
        waypoint = f"Lat: {self.Track_Lat_Input}, Lon: {self.Track_Lon_Input}"
        current_waypoints = self.waypoint_model.stringList()
        current_waypoints.append(waypoint)
        self.waypoint_model.setStringList(current_waypoints)
        self.ui.Lat_Input_Track.clear()
        self.ui.Lon_Input_Track.clear()
    
    def clear_waypoint(self):
        self.waypoint_model.setStringList([])

    # Method to handle sail throttle slider value changes
    def update_sail_throttle(self, value):
        self.sail_throttle_value = value
      
        self.ui.Sail_Throttle_LCD.display(self.sail_throttle_value)

    # Method to programmatically set the sail throttle slider's value
    def set_sail_throttle_value(self, value):
        self.ui.Sail_Throttle_Slider.setValue(value)
        print(f"Sail Throttle Slider set to: {value}")

    # Method to handle sail heading dial value changes
    def update_sail_heading(self, value):
        self.sail_heading_value = value

        # Update the LCD display to show the current heading
        self.ui.Sail_Heading_LCD.display(self.sail_heading_value)

    # Method to programmatically set the sail heading dial's value
    def set_sail_heading_value(self, value):
        self.ui.Sail_Heading_Dial.setValue(value)
        print(f"Sail Heading Dial set to: {value}")


    def set_Th1_Icon(self, value):
        self.ui.Global_Throttle1_Status.setValue(int(value))

    def set_Th2_Icon(self, value):
        self.ui.Global_Throttle2_Status.setValue(int(value))
    
    def set_Heading_Lcd(self, value):
        self.ui.Global_Heading_LCD.display(value)
    
    def set_Speed_Lcd(self, value):
        self.ui.Global_Speed_LCD.display(value)

    def set_compass_value(self, value):
        self.ui.Compass_Dial.setValue(value)

    def retrieve_dp_input(self):
        self.Dp_Lon_Input = self.ui.Lon_Input_Dp.text()
        self.Dp_Lat_Input = self.ui.Lat_Input_Dp.text()
        print(self.Dp_Lat_Input, self.Dp_Lon_Input)

    def retrieve_track_input(self):
        self.Track_Lon_Input = self.ui.Lon_Input_Track.text()
        self.Track_Lat_Input = self.ui.Lat_Input_Track.text()
        print(self.Track_Lat_Input, self.Track_Lon_Input)


    # Method to handle the Enable Standby button click
    def enable_standby(self):

        mode_message = HMI()
        mode_message.mode = 0
        self.hmi_publisher.publish(mode_message)

        self.Operating_Mode = 0
        self.ui.Standby_Status_Icon.setValue(int(100))
        self.ui.Sail_Status_Icon.setValue(int(0))
        self.ui.Dp_Status_Icon.setValue(int(0))
        self.ui.Track_Status_Icon.setValue(int(0))
        print(self.Operating_Mode)

    # Method to handle the Enable Sail button click
    def enable_sail(self):

        mode_message = HMI()
        mode_message.mode = 1
        self.hmi_publisher.publish(mode_message)

        self.Operating_Mode = 1
        self.ui.Standby_Status_Icon.setValue(int(0))
        self.ui.Sail_Status_Icon.setValue(int(100))
        self.ui.Dp_Status_Icon.setValue(int(0))
        self.ui.Track_Status_Icon.setValue(int(0))
        print(self.Operating_Mode)

    # Method to handle the Enable Dp button click
    def enable_dp(self):

        mode_message = HMI()
        mode_message.mode = 2
        self.hmi_publisher.publish(mode_message)

        self.Operating_Mode = 2
        self.ui.Standby_Status_Icon.setValue(int(0))
        self.ui.Sail_Status_Icon.setValue(int(0))
        self.ui.Dp_Status_Icon.setValue(int(100))
        self.ui.Track_Status_Icon.setValue(int(0))
        print(self.Operating_Mode)
    
    # Method to handle the Track Sail button click
    def enable_track(self):
        self.Operating_Mode = 3

        mode_message = HMI()
        mode_message.mode = 3
        self.hmi_publisher.publish(mode_message)

        self.ui.Standby_Status_Icon.setValue(int(0))
        self.ui.Sail_Status_Icon.setValue(int(0))
        self.ui.Dp_Status_Icon.setValue(int(0))
        self.ui.Track_Status_Icon.setValue(int(100))
        print(self.Operating_Mode)

    def load_dp(self):
        self.dp_load = True
        print(self.dp_load)  

    def disable_dp_load(self):
        self.dp_load = False
        print(self.dp_load)      

    def load_track(self):
        self.track_Load = True
        print(self.track_Load)
        
    def disable_track_load(self):
        self.track_load = False
        print(self.track_load)   
       
    def spin_ros(self):
        rclpy.spin_once(self, timeout_sec=0.1)
    

def main(args=None):
    rclpy.init(args=args)

    # Create the application object
    app = QApplication(sys.argv)

    # Create the AutopilotHMI node
    engineering_hmi = EngineeringHMI()

    # Set up a QTimer to spin the ROS2 node and handle callbacks
    timer = QTimer()
    timer.timeout.connect(engineering_hmi.spin_ros)
    timer.start(100)  # Call every 100 ms

    # Handle signal for graceful shutdown
    def signal_handler(sig, frame):
        print("SIGINT received, shutting down...")
        engineering_hmi.destroy_node()
        rclpy.shutdown()
        app.quit()

    signal.signal(signal.SIGINT, signal_handler)

    # Start the application event loop
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
