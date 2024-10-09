import sys
import os
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWebChannel import QWebChannel
from PySide6.QtCore import QObject, Slot, QTimer, QUrl
from ui_DesignerDemo import Ui_MainWindow  # Replace with your actual UI module

class Bridge(QObject):
    @Slot(float, float)
    def updatePosition(self, lat, lng):
        pass  # This method can be empty; it's used for communication

class DashboardDemo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Set up the web view
        self.webview = QWebEngineView()
        layout = QVBoxLayout(self.ui.mapPlaceholder)
        layout.addWidget(self.webview)
        self.ui.mapPlaceholder.setLayout(layout)

        # Set up the web channel
        self.channel = QWebChannel()
        self.bridge = Bridge()
        self.channel.registerObject('bridge', self.bridge)
        self.webview.page().setWebChannel(self.channel)

        # Load the HTML file
        current_dir = os.path.dirname(os.path.abspath(__file__))
        html_file = os.path.join(current_dir, 'index.html')
        self.webview.load(QUrl.fromLocalFile(html_file))

        # Initialize the boat's position
        self.boat_position = [59.91, 10.75]

        # Set up a timer to update the boat's position
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_boat_position)
        self.timer.start(1000)  # Update every second

        # Connect sliders to update label values (if you have sliders)
        # self.ui.HorisontalSlider1.valueChanged.connect(self.update_horizontal_slider)
        # self.ui.VerticalSlider1.valueChanged.connect(self.update_vertical_slider1)
        # self.ui.VerticalSlider2.valueChanged.connect(self.update_vertical_slider2)

    def update_boat_position(self):
        # Simulate boat movement
        self.boat_position[0] += 0.001  # Move north by 0.001 degrees

        # Call the JavaScript function to update the boat's position
        lat, lng = self.boat_position
        js_code = f"updateBoatPosition({lat}, {lng});"
        self.webview.page().runJavaScript(js_code)

    # Uncomment and implement these methods if you have sliders
    # def update_horizontal_slider(self, value):
    #     self.ui.HorisontalLabel1.setText(f'H1: {value}')
    #     # Update logic as needed

    # def update_vertical_slider1(self, value):
    #     self.ui.VerticalSliderLabel1.setText(f'V1: {value}')
    #     # Update logic as needed

    # def update_vertical_slider2(self, value):
    #     self.ui.VerticalSlideLabel2.setText(f'V2: {value}')
    #     # Update logic as needed

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DashboardDemo()
    window.show()
    sys.exit(app.exec())
