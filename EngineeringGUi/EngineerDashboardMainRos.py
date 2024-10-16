### Import for PyQt ###
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QStringListModel, QTimer
from EngineeringDashboard import Ui_MainWindow  # Import your generated UI file
import sys

### Import for ros ###
import signal
import rclpy
from rclpy.node import Node
from ngc_interfaces.msg import Eta, Nu, Mode
from ngc_utils.qos_profiles import default_qos_profile
import numpy as np
import ngc_utils.math_utils as mu




class SharedData:
    def __init__(self):
        self.Operating_Mode         = 0 # 0 = standby  1 = sail  2 = dp  3 = track
        self.Track_Active           = False
        self.Dp_Active              = False
        self.sail_throttle_value    = 0
        self.sail_heading_value     = 0
        self.Global_Th1_Rps         = 0
        self.Global_Th2_Rps         = 0
        self.Global_Heading         = 0
        self.Global_Speed           = 0
        
        


class CustomHmi:
    def __init__(self, shared_data):
            
        ##### ROS MILJØ #####
        self.shared_data = shared_data
       

        self.Hmi_publsiher = self.create_publisher(Hmi, 'hmi', default_qos_profile)
        

    def update_eta_feedback(self, msg):
        ##

    def update_nu_feedback(self, msg):
        ###

    

class MainWindow(QMainWindow):
    def __init__(self, shared_data):
        super(MainWindow, self).__init__()


        ##### PyQt Dashboard #####
        self.shared_data = shared_data    

        # Create an instance of the Ui_MainWindow
        self.ui = Ui_MainWindow()

        # Set up the UI
        self.ui.setupUi(self)

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
        self.ui.Dp_Disable_Button.clicked.connect(self.disable_dp)
        self.ui.Track_Disable_Button.clicked.connect(self.disable_track)
        self.ui.Enable_Track_Button.clicked.connect(self.enable_track)
        self.ui.Track_Activate_Button.clicked.connect(self.activate_track)
        self.ui.Dp_Activate_Button.clicked.connect(self.activate_dp)
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
        self.shared_data.sail_throttle_value = value
      
        self.ui.Sail_Throttle_LCD.display(self.shared_data.sail_throttle_value)

    # Method to programmatically set the sail throttle slider's value
    def set_sail_throttle_value(self, value):
        self.ui.Sail_Throttle_Slider.setValue(value)
        print(f"Sail Throttle Slider set to: {value}")

    # Method to handle sail heading dial value changes
    def update_sail_heading(self, value):
        self.shared_data.sail_heading_value = value

        # Update the LCD display to show the current heading
        self.ui.Sail_Heading_LCD.display(self.shared_data.sail_heading_value)

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
        self.shared_data.Operating_Mode = 0
        self.ui.Standby_Status_Icon.setValue(int(100))
        self.ui.Sail_Status_Icon.setValue(int(0))
        self.ui.Dp_Status_Icon.setValue(int(0))
        self.ui.Track_Status_Icon.setValue(int(0))
        print(self.shared_data.Operating_Mode)

    # Method to handle the Enable Sail button click
    def enable_sail(self):
        self.shared_data.Operating_Mode = 1
        self.ui.Standby_Status_Icon.setValue(int(0))
        self.ui.Sail_Status_Icon.setValue(int(100))
        self.ui.Dp_Status_Icon.setValue(int(0))
        self.ui.Track_Status_Icon.setValue(int(0))
        print(self.shared_data.Operating_Mode)

    # Method to handle the Enable Dp button click
    def enable_dp(self):
        self.shared_data.Operating_Mode = 2
        self.ui.Standby_Status_Icon.setValue(int(0))
        self.ui.Sail_Status_Icon.setValue(int(0))
        self.ui.Dp_Status_Icon.setValue(int(100))
        self.ui.Track_Status_Icon.setValue(int(0))
        print(self.shared_data.Operating_Mode)
    
    # Method to handle the Track Sail button click
    def enable_track(self):
        self.shared_data.Operating_Mode = 3
        self.ui.Standby_Status_Icon.setValue(int(0))
        self.ui.Sail_Status_Icon.setValue(int(0))
        self.ui.Dp_Status_Icon.setValue(int(0))
        self.ui.Track_Status_Icon.setValue(int(100))
        print(self.shared_data.Operating_Mode)

    def activate_track(self):
        self.shared_data.Track_Active = True
        print(self.Track_Active)
    
    def activate_dp(self):
       self.shared_data.Dp_Active = True
       print(self.Dp_Active)
    
    def disable_dp(self):
        self.shared_data.Dp_Active = False
        print(self.Dp_Active)
    
    def disable_track(self):
        self.shared_data.Track_Active = False
        print(self.Track_Active)

       
    

if __name__ == "__main__":
    # Create the application object
    shared_data = SharedData()
    hmi_node = CustomHmi(shared_data)
    

    app = QApplication(sys.argv)

    # Create an instance of the MainWindow and show it
    window = MainWindow(shared_data)
    window.show()

    # Start the application's event loop
    sys.exit(app.exec())
