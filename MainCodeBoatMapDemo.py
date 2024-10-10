import sys
import os
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtWebEngineCore import QWebEngineSettings
from PyQt6.QtWebChannel import QWebChannel
from PyQt6.QtCore import QObject, pyqtSlot, QUrl, QTimer

class Bridge(QObject):
    # This class serves as a communication bridge between Python and JavaScript
    pass  # No methods are needed unless you require callbacks from JavaScript

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set the window title and size
        self.setWindowTitle("Boat Tracker")
        self.resize(800, 600)

        # Set up the web view
        self.webview = QWebEngineView(self)
        self.setCentralWidget(self.webview)

        # Set up the web channel
        self.channel = QWebChannel()
        self.bridge = Bridge()
        self.channel.registerObject('bridge', self.bridge)
        self.webview.page().setWebChannel(self.channel)

        # Load the HTML file
        current_dir = os.path.dirname(os.path.abspath(__file__))
        html_file = os.path.join(current_dir, 'index.html')
        self.webview.load(QUrl.fromLocalFile(html_file))

        # Enable JavaScript and remote content
        settings = self.webview.settings()
        settings.setAttribute(QWebEngineSettings.WebAttribute.JavascriptEnabled, True)
        settings.setAttribute(QWebEngineSettings.WebAttribute.LocalContentCanAccessRemoteUrls, True)
        settings.setAttribute(QWebEngineSettings.WebAttribute.LocalContentCanAccessFileUrls, True)
        settings.setAttribute(QWebEngineSettings.WebAttribute.PluginsEnabled, True)

        # Initialize boat position
        self.boat_position = [59.91, 10.75]  # Starting coordinates (latitude, longitude)

        # Set up a timer to update the boat's position
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_boat_position)
        self.timer.start(1000)  # Update every second

    def update_boat_position(self):
        # Simulate boat movement (move north by 0.001 degrees latitude)
        self.boat_position[0] += 0.001

        # Update the boat's position on the map
        lat, lng = self.boat_position
        js_code = f"updateBoatPosition({lat}, {lng});"
        self.webview.page().runJavaScript(js_code)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
