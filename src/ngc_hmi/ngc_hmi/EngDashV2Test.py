from PyQt6.QtWidgets import QApplication, QMainWindow
from .EngineeringDashboard import Ui_MainWindow  # Replace with the correct import path
from Xlib import display
import ctypes
import sys

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Apply the UI setup to MainWindow
        self.embed_opencpn()

    def embed_opencpn(self):
        display_instance = display.Display()

        # Replace '0xYourOpenCPNWindowID' with the actual window ID obtained from xwininfo
        window_id = 0xYourOpenCPNWindowID  # Use the actual ID
        
        # Use ctypes to reparent the window
        xlib = ctypes.cdll.LoadLibrary('libX11.so')
        xlib.XReparentWindow(
            display_instance,  # Display instance
            window_id,         # OpenCPN window ID
            self.MapPlaceHolder.winId().__int__(),  # ID of MapPlaceHolder widget
            0, 0               # Position within the widget
        )
        display_instance.sync()

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
