### Import for PyQt ###
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QDial
from PySide6.QtCore import QStringListModel, QTimer, Qt, QProcess, QPoint, QPointF, QRect, QSize
from PySide6.QtGui import QWindow, QPainter, QPen, QColor, QPixmap
from .Darkmode_Dashboard import Ui_MainWindow  # Import your generated UI file
import sys
import sip
import subprocess  # For running commands like xdotool (Linux)
import time

### Import for Ros ###
import rclpy
from rclpy.node import Node
from ngc_interfaces.msg import HMI, TravelData, OtterStatus, ThrusterSignals, Eta, Nu
from ngc_utils.qos_profiles import default_qos_profile
import numpy as np
import ngc_utils.math_utils as mu
import signal

class CompassDial(QDial):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        # Load the rotating compass image (e.g., the boat)
        self.compass_image_original = QPixmap('pictures/Otter_Compass_v2.png')
        
        self.boat_scale_factor = 0.75  # Adjust as necessary

        # Scale the compass image initially
        self.updateImage()

        # Hide the default dial appearance but keep the notches
        self.setStyleSheet("QDial { background-color: transparent; border: none; }")
        self.setNotchesVisible(True)

    def resizeEvent(self, event):
        # Rescale the image on widget resize
        self.updateImage()
        super().resizeEvent(event)

    def updateImage(self):
        size = self.size()
        
        # Scale the compass image relative to the widget's dimensions
        boat_size = size * self.boat_scale_factor
        self.compass_image = self.compass_image_original.scaled(
            boat_size, 
            Qt.AspectRatioMode.KeepAspectRatio, 
            Qt.TransformationMode.SmoothTransformation
        )

    def paintEvent(self, event):
        painter = QPainter(self)
        
        rect = self.rect()
        center = rect.center()
        
        # Rotate and draw the compass image (replacing the dial's appearance)
        painter.translate(center)
        painter.rotate(round((self.value() + 180), 0))
        painter.translate(-center)
        
        # Draw the rotated compass image on top
        compass_rect = self.compass_image.rect()
        compass_rect.moveCenter(center)
        painter.drawPixmap(compass_rect, self.compass_image)
        
        # Draw the notches by calling the superclass paintEvent
        super().paintEvent(event)


class EngineeringHMI(Node):
    def __init__(self):
        super().__init__('ngc_engineering_hmi')

        #### HMI publisher ####
        self.hmi_publisher = self.create_publisher(HMI, 'hmi', default_qos_profile)

        ### HMI subscriber ####
        self.create_subscription(HMI, 'hmi', self.hmi_callback, default_qos_profile)

        # Endring for otter interface
        self.create_subscription(OtterStatus, 'otter_status', self.otter_status_callback, default_qos_profile)
        self.create_subscription(ThrusterSignals, 'thruster_1_setpoints', self.thruster_1_sim_callback, default_qos_profile)
        self.create_subscription(ThrusterSignals, 'thruster_2_setpoints', self.thruster_2_sim_callback, default_qos_profile)
        self.create_subscription(TravelData, 'traveldata', self.travel_data_callback, default_qos_profile)
        self.create_subscription(Eta, 'eta_hat', self.eta_hat_callback, default_qos_profile)
        self.create_subscription(Nu, 'nu_hat', self.nu_hat_callback, default_qos_profile)

        self.opencpn_process = QProcess()
        self.opencpn_process.started.connect(self.get_opencpn_window_id)
        self.opencpn_process.start("gnome-terminal", ["--", "opencpn"])

        # Embed the external OpenCPN application if a window ID is provided
        self.opencpn_window_id = ""

        # Initialize the UI
        self.init_ui()

    def get_opencpn_window_id(self):
        time.sleep(2)  # Wait briefly to allow OpenCPN to load and focus
        try:
            # Use xdotool to get the focused window ID with OpenCPN's name
            result = subprocess.run(
                ["xdotool", "search", "--onlyvisible", "--name", "OpenCPN", "getwindowfocus"],
                capture_output=True, text=True
            )
            self.opencpn_window_id = result.stdout.strip()

            if self.opencpn_window_id:
                print(f"OpenCPN Main Window ID: {self.opencpn_window_id}")
                self.embed_external_application(self.opencpn_window_id)
            else:
                self.get_logger().error("Failed to retrieve the OpenCPN window ID.")

        except subprocess.CalledProcessError as e:
            self.get_logger().error(f"Error finding OpenCPN window ID: {e}")


    def init_ui(self):

        self.ui = Ui_MainWindow()

        # Create an instance of the MainWindow and show it
        self.window = QMainWindow()
        self.ui.setupUi(self.window)

       # Replace Compass_Dial in the layout
        compass_dial = CompassDial(self.ui.centralwidget)  # use central widget as parent
        compass_dial.setGeometry(self.ui.Compass_Dial.geometry())
        compass_dial.setRange(0, 360)
        compass_dial.setValue(self.ui.Compass_Dial.value())

        # Remove the original Compass_Dial from the layout and add CompassDial instead
        layout = self.ui.Compass_Dial.parentWidget().layout()
        if layout is not None:
            layout.replaceWidget(self.ui.Compass_Dial, compass_dial)
        else:
            compass_dial.setGeometry(self.ui.Compass_Dial.geometry())  # fallback if no layout

        self.ui.Compass_Dial.deleteLater()  # remove original
        self.ui.Compass_Dial = compass_dial  # replace with custom
        
        self.window.showFullScreen()

        # Add a small delay to let the window finish loading and layout updating
        QTimer.singleShot(500, lambda: self.embed_external_application(self.opencpn_window_id))

        # Create a QTimer for continuous adjustments to the OpenCPN window
        self.update_timer = QTimer()
        self.update_timer.timeout.connect(self.adjust_opencpn_window)
        self.update_timer.start(100)  # Update every 100ms

        # Lager Variabler
        self.mode           = 0
        self.route          = False
        self.point          = False
        self.nu             = 0
        self.eta            = 0
        self.th1_rpm        = 0
        self.th2_rpm        = 0
        self.th1_pwr        = 0
        self.th2_pwr        = 0
        self.fuel_cap       = 0

        self.i              = 0
        self.coordinates    = []
        self.status         = False
        self.dp_status      = False
        self.dp_error       = False
        self.anchor         = False

        self.debug          = False
        self.simulator      = True


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
        self.ui.Track_Load_Button.pressed.connect(self.load_track)
        self.ui.Track_Load_Button.released.connect(self.load_track_reset) 
        self.ui.Dp_Load_Button.released.connect(self.load_dp_reset)      
        self.ui.Exit_Button.clicked.connect(self.exit_procedure)
        self.ui.Anchor_button.pressed.connect(self.load_anchor)
        self.ui.Anchor_button.released.connect(self.anchor_reset)

        if self.simulator:
            # Setter modus og fuel til simulator / demo
            self.ui.Mode.setText(f'Simulator')
            self.ui.Fuel.setText(f'420%')

    def exit_procedure(self):
        try:
            subprocess.run(['gnome-terminal', '--', 'bash', '-c', 'pkill -SIGTERM opencpn; pkill -SIGTERM -f ros2; exec bash'])
            rclpy.shutdown()
            
        except Exception as e:
            self.get_logger().error(f"Exit not exiting, plis try again {e}")


    def embed_external_application(self, window_id):
        # Save the window ID for reuse in resizing or moving
        self.opencpn_window_id = str(window_id)
        # Adjust the window position initially
        self.adjust_opencpn_window()

    def adjust_opencpn_window(self):
        if not self.opencpn_window_id:
            return

        # Ensure layout updates and geometry calculations
        self.ui.MapPlaceHolder.updateGeometry()
        self.window.layout().activate()
        QApplication.processEvents()

        # Calculate the MapPlaceHolder's global position and size
        rect = self.ui.MapPlaceHolder.rect()
        map_placeholder_global_pos = self.ui.MapPlaceHolder.mapToGlobal(QPoint(0, 0))

        # Extract global x, y, width, and height
        map_placeholder_global_x = map_placeholder_global_pos.x()
        map_placeholder_global_y = map_placeholder_global_pos.y()
        width = rect.width()
        height = rect.height() - 60

        try:
            # Use xdotool to move and resize the identified window ID
            subprocess.run([
                "xdotool", "windowmove", self.opencpn_window_id, str(map_placeholder_global_x), str(map_placeholder_global_y),
                "windowsize", self.opencpn_window_id, str(width), str(height)
            ], capture_output=True, text=True)
    
            subprocess.run([
                "wmctrl", "-i", "-r", self.opencpn_window_id, "-b", "add,above"
            ], capture_output=True, text=True)

        except Exception as e:
            self.get_logger().error(f"Failed to adjust OpenCPN window position: {e}")


    # Method to handle sail throttle slider value changes
    def update_sail_throttle(self, value):
        self.nu = float(value / 10)        
        # Update the LCD display to show the current throttle
        self.ui.Sail_Throttle_LCD.display(value / 10)

        self.hmi_send_ros_message()

    # Method to programmatically set the sail throttle slider's value
    def set_sail_throttle_value(self, value):
        self.ui.Sail_Throttle_Slider.setValue(value)


    # Method to handle sail heading dial value changes
    def update_sail_heading(self, value):
        remapped_value = (value - 180) % 360
        self.eta = float(remapped_value)

        # Update the LCD display to show the current heading
        self.ui.Sail_Heading_LCD.display(remapped_value)
        self.hmi_send_ros_message()

    # Method to programmatically set the sail heading dial's value
    def set_sail_heading_value(self, value):
        self.ui.Sail_Heading_Dial.setValue(value)


    def set_Th1_Icon(self, value):
        # Set the value of the progress bar
        if value > 0:
            self.ui.Global_Throttle1_Status.setValue(int(abs(value)))
            self.ui.Global_Throttle1rev_Status.setValue(int(0))
        else:
            self.ui.Global_Throttle1_Status.setValue(int(0))
            self.ui.Global_Throttle1rev_Status.setValue(int(abs(value)))


    def set_Th2_Icon(self, value):
        # Set the value of the progress bar
        if value > 0:
            self.ui.Global_Throttle2_Status.setValue(int(abs(value)))
            self.ui.Global_Throttle2rev_Status.setValue(int(0))
        else:
            self.ui.Global_Throttle2_Status.setValue(int(0))
            self.ui.Global_Throttle2rev_Status.setValue(int(abs(value)))


    def set_Heading_Lcd(self, value):
        self.ui.Global_Heading_LCD.display(value)
    
    def set_Speed_Lcd(self, value):
        self.ui.Global_Speed_LCD.display(value)

    def set_compass_value(self, value):
        self.ui.Compass_Dial.setValue(value)


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
    
    def load_track_reset(self):
        self.route = False
    
    def load_dp_reset(self):
        self.point = False

    def load_anchor(self):
        self.anchor = True
        self.hmi_send_ros_message()        

    def anchor_reset(self):
        self.anchor = False
        

    def hmi_send_ros_message(self):
        hmi_message = HMI()
        hmi_message.mode    = self.mode
        hmi_message.route   = self.route 
        hmi_message.point   = self.point
        hmi_message.nu      = float(self.nu) * 0.514444
        hmi_message.eta     = float(mu.mapToPiPi(np.deg2rad(self.eta))) # Convert degrees to radians and map 2 plus minus pi
        hmi_message.anchor  = self.anchor
        self.hmi_publisher.publish(hmi_message)


        if self.debug:
            self.get_logger().info(
                f'etapub={hmi_message.eta}\n'
                f'nupub={hmi_message.nu}'
            )

    def travel_data_callback(self, msg: TravelData):
        self.i = msg.i
        #self.coordinates = msg.coordinates
        self.coordinates = []

        for wp in msg.coordinates:
            latitude = wp.lat
            longitude = wp.lon
            coor = (latitude, longitude)
            self.coordinates.append(coor)

        self.status = msg.status

        if msg.dp != 0:
            self.dp_status = msg.dp
            self.dp_error  = msg.error
            self.ui.Deviation_Dp_LCD.display(round(self.dp_error, 2))

        if self.debug:
            self.get_logger().info(
                f'i: {msg.i}\n'
                f'coordinates: {self.coordinates}\n'
                f'status: {msg.status}\n'
                f'DP: {msg.dp}\n'
                f'DP error: {msg.error}'
            )

        if self.status:
            if self.i > 0:
                self.last_waypoint = self.coordinates[self.i - 1]
            else:
                self.last_waypoint = None
            
            self.current_waypoint   = self.coordinates[self.i]

            if self.i + 1 < len(self.coordinates):
                self.next_waypoint = self.coordinates[self.i + 1]
            else:
                self.next_waypoint = None

            self.waypoints = [wp for wp in [self.last_waypoint, self.current_waypoint, self.next_waypoint] if wp is not None]
            waypoint_strings = [f"Lat: {lat:.6f},   Lon:{lon:.6f}" for lat, lon in self.waypoints]

            model = QStringListModel()
            model.setStringList(waypoint_strings)
            self.ui.WayPoint_ListView.setModel(model)  
            

    def hmi_callback(self, msg: HMI):
        
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


    def otter_status_callback(self, msg:OtterStatus):
        self.th1_rpm        = msg.rpm_port
        self.th2_rpm        = msg.rpm_stb
        self.th1_pwr        = msg.power_port
        self.th2_pwr        = msg.power_stb
        self.current_mode   = msg.current_mode
        self.fuel_cap       = msg.current_fuel_capacity
        self.ui.Mode.setText(f'{self.current_mode}')
        self.ui.Fuel.setText(f'{self.fuel_cap}%')
        self.simulator = False
    
    
    def thruster_1_sim_callback(self, msg:ThrusterSignals):
        self.sim_th1_rpm = msg.rps * 60
        self.set_Th1_Icon(self.sim_th1_rpm)

    def thruster_2_sim_callback(self, msg:ThrusterSignals):
        self.sim_th2_rpm = msg.rps * 60
        self.set_Th2_Icon(self.sim_th2_rpm)

    def eta_hat_callback(self, msg:Eta):
        self.eta_hat = np.degrees(mu.mapToZero2Pi(msg.psi))
        self.ui.Global_Heading_LCD.display(round(self.eta_hat, 2))
        self.ui.Compass_Dial.setValue(self.eta_hat)

    def nu_hat_callback(self, msg:Nu):
        self.nu_hat = msg.u * 1.943844
        self.ui.Global_Speed_LCD.display(round(self.nu_hat, 2))



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
