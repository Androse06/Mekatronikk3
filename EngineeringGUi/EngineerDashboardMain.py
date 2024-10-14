# main.py
from PySide6.QtWidgets import QApplication, QMainWindow
from EngineeringDashboard import Ui_MainWindow  # Import your generated UI file
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # Create an instance of the Ui_MainWindow
        self.ui = Ui_MainWindow()

        # Set up the UI
        self.ui.setupUi(self)

        # Initialize variables to hold widget values
        self.sail_throttle_value = 0
        self.sail_heading_value = 0

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
