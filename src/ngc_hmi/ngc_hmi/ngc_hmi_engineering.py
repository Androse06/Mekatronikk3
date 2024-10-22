### Import for PyQt ###
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout
from PySide6.QtCore import QStringListModel, QTimer, Qt, QProcess, QPoint
from PySide6.QtGui import QWindow
from .EngineeringDashboard import Ui_MainWindow  # Import your generated UI file
import sys
import sip
import subprocess  # For running commands like xdotool (Linux)
import time

### Import for Ros ###
import rclpy
from rclpy.node import Node
from ngc_interfaces.msg import HMI
from ngc_utils.qos_profiles import default_qos_profile
import numpy as np
import ngc_utils.math_utils as mu
import signal

class EngineeringHMI(Node):
    def __init__(self):
        super().__init__('ngc_engineering_hmi')

        #### HMI publisher ####
        self.hmi_publisher = self.create_publisher(HMI, 'hmi', default_qos_profile)

        ### HMI subscriber ####
        self.create_subscription(HMI, 'hmi', self.hmi_callback, default_qos_profile)

        # Embed the external OpenCPN application if a window ID is provided
        self.opencpn_window_id = "29360373"

        # Initialize the UI
        self.init_ui()

    def init_ui(self):

        self.ui = Ui_MainWindow()

        # Create an instance of the MainWindow and show it
        self.window = QMainWindow()
        self.ui.setupUi(self.window)
        self.window.show()


         # Embed the external OpenCPN application if a window ID is provided
        if self.opencpn_window_id:
            self.embed_external_application(self.opencpn_window_id)

        # Create a QTimer for continuous adjustments to the OpenCPN window
        self.update_timer = QTimer()
        self.update_timer.timeout.connect(self.adjust_opencpn_window)
        self.update_timer.start(100)  # Update every 100ms


        # Lager Variabler'
        self.mode   = 0
        self.route  = False
        self.point  = False
        self.nu     = 0
        self.eta    = 0

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
        self.ui.Dp_Load_Button.clicked.connect(self.load_dp)
        self.ui.Track_Load_Button.pressed.connect(self.load_track)       
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




    def embed_external_application(self, window_id):
        # Save the window ID for reuse in resizing or moving
        self.opencpn_window_id = str(window_id)
        # Adjust the window position initially
        self.adjust_opencpn_window()

    def adjust_opencpn_window(self):
        # Ensure the window ID is set
        if not self.opencpn_window_id:
            return

        #FUNKA FOR STØRRELSE
        # Get the geometry of the MapPlaceHolder relative to its parent (centralwidget)
        #map_placeholder_geometry = self.ui.MapPlaceHolder.frameGeometry()
        #map_placeholder_width = map_placeholder_geometry.width()
        #map_placeholder_height = map_placeholder_geometry.height()

        # Force the layouts to update
        self.window.layout().activate()
        QApplication.processEvents()

        # Get the MapPlaceHolder's position relative to the main window
        map_placeholder_pos = self.ui.MapPlaceHolder.mapTo(self.window, QPoint(0, 0))

        # Get the main window's global position
        main_window_global_pos = self.window.pos()

        # Calculate the MapPlaceHolder's global position
        map_placeholder_global_x = main_window_global_pos.x() + map_placeholder_pos.x()
        map_placeholder_global_y = main_window_global_pos.y() + map_placeholder_pos.y()

        # Get the MapPlaceHolder's size
        map_placeholder_width = self.ui.MapPlaceHolder.width()
        map_placeholder_height = self.ui.MapPlaceHolder.height()

        print(f"Adjusting OpenCPN window ID {self.opencpn_window_id} to x={map_placeholder_global_x}, y={map_placeholder_global_y}, "
            f"width={map_placeholder_width}, height={map_placeholder_height}")

        try:
            # Use xdotool to move and resize the identified window ID
            result = subprocess.run([
                "xdotool", "windowmove", self.opencpn_window_id, str(map_placeholder_global_x), str(map_placeholder_global_y),
                "windowsize", self.opencpn_window_id, str(map_placeholder_width), str(map_placeholder_height)
            ], capture_output=True, text=True)

            # Print the result of the xdotool command for debugging
            print("xdotool output:", result.stdout)
            print("xdotool errors:", result.stderr)

        except Exception as e:
            self.get_logger().error(f"Failed to adjust window position: {e}")




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
        
        self.nu = float(value)        
        # Update the LCD display to show the current throttle
        self.ui.Sail_Throttle_LCD.display(value)
        self.hmi_send_ros_message()

    # Method to programmatically set the sail throttle slider's value
    def set_sail_throttle_value(self, value):
        self.ui.Sail_Throttle_Slider.setValue(value)


    # Method to handle sail heading dial value changes
    def update_sail_heading(self, value):
        remapped_value = (value - 180) % 360
        self.eta = float(remapped_value)
        self.get_logger().info(f'eta = {self.eta}')
        # Update the LCD display to show the current heading
        self.ui.Sail_Heading_LCD.display(remapped_value)
        self.hmi_send_ros_message()

    # Method to programmatically set the sail heading dial's value
    def set_sail_heading_value(self, value):
        self.ui.Sail_Heading_Dial.setValue(value)


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


    def retrieve_track_input(self):
        self.Track_Lon_Input = self.ui.Lon_Input_Track.text()
        self.Track_Lat_Input = self.ui.Lat_Input_Track.text()



    # Method to handle the Enable Standby button click
    def enable_standby(self):
        self.mode = 0
    
        self.ui.Standby_Status_Icon.setValue(int(100))
        self.ui.Sail_Status_Icon.setValue(int(0))
        self.ui.Dp_Status_Icon.setValue(int(0))
        self.ui.Track_Status_Icon.setValue(int(0))
        self.hmi_send_ros_message()

    # Method to handle the Enable Sail button click
    def enable_sail(self):
        self.mode = 1

        self.ui.Standby_Status_Icon.setValue(int(0))
        self.ui.Sail_Status_Icon.setValue(int(100))
        self.ui.Dp_Status_Icon.setValue(int(0))
        self.ui.Track_Status_Icon.setValue(int(0))
        self.hmi_send_ros_message()

    # Method to handle the Enable Dp button click
    def enable_dp(self):
        self.mode = 2
        
        self.ui.Standby_Status_Icon.setValue(int(0))
        self.ui.Sail_Status_Icon.setValue(int(0))
        self.ui.Dp_Status_Icon.setValue(int(100))
        self.ui.Track_Status_Icon.setValue(int(0)) 
        self.hmi_send_ros_message() 
    
    # Method to handle the Track Sail button click
    def enable_track(self):
        self.mode = 3

        self.ui.Standby_Status_Icon.setValue(int(0))
        self.ui.Sail_Status_Icon.setValue(int(0))
        self.ui.Dp_Status_Icon.setValue(int(0))
        self.ui.Track_Status_Icon.setValue(int(100))
        self.hmi_send_ros_message()

    def load_dp(self):
        self.point = True
        self.hmi_send_ros_message()

    def load_track(self):
        self.route = True
        self.hmi_send_ros_message()

    def hmi_send_ros_message(self):
        hmi_message = HMI()
        hmi_message.mode    = self.mode
        hmi_message.route   = self.route 
        hmi_message.point   = self.point
        hmi_message.nu      = float(self.nu) * 0.514444
        hmi_message.eta     = float(mu.mapToPiPi(np.deg2rad(self.eta))) # Convert degrees to radians and map 2 plus minus pi
        self.hmi_publisher.publish(hmi_message)
        self.get_logger().info(f'etapub={hmi_message.eta}')
        self.get_logger().info(f'nupub={hmi_message.nu}')

    def hmi_callback(self, msg: HMI):
        self.route = msg.route
        self.point = msg.point

        if self.mode != msg.mode:
            self.mode = msg.mode
            if  self.mode == 0:
                self.enable_standby()
            elif self.mode == 1:
                self.enable_sail()
            elif self.mode == 2:
                self.enable_dp()
            elif self.mode == 3:
                self.enable_track()
        
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
    timer.start(200)  # Call every 200 ms

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
