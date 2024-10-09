import os
import folium
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWebEngineCore import QWebEngineSettings
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout
from ui_DesignerDemo import Ui_MainWindow

class DashboardDemo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Replace the placeholder QWidget with QWebEngineView for displaying the map
        # Use 'mapPlaceholder' as per your UI file
        self.webview = QWebEngineView(self.ui.mapPlaceholder)

        # Set up a layout for mapPlaceholder if not set in Qt Designer
        layout = QVBoxLayout(self.ui.mapPlaceholder)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.webview)
        self.ui.mapPlaceholder.setLayout(layout)

        # Enable JavaScript and adjust security settings
        self.webview.settings().setAttribute(QWebEngineSettings.JavascriptEnabled, True)
        self.webview.settings().setAttribute(QWebEngineSettings.LocalContentCanAccessFileUrls, True)
        self.webview.settings().setAttribute(QWebEngineSettings.LocalContentCanAccessRemoteUrls, True)

        # Define your waypoints
        self.waypoints = [
            (59.91, 10.75),  # Oslo
            (59.92, 10.76),
            (59.93, 10.77),
            # Add more waypoints as needed
        ]

        # Generate the map HTML and set it directly
        map_html = self.generate_map_embed(self.waypoints)
        self.webview.setHtml(map_html)

        # Connect sliders to update label values
        self.ui.HorisontalSlider1.valueChanged.connect(self.update_horizontal_slider)
        self.ui.VerticalSlider1.valueChanged.connect(self.update_vertical_slider1)
        self.ui.VerticalSlider2.valueChanged.connect(self.update_vertical_slider2)

    def generate_map_embed(self, waypoints):
        """Generate a Folium map with waypoints and return the HTML representation."""
        if not waypoints:
            center_location = [59.91, 10.75]
        else:
            center_location = waypoints[0]

        m = folium.Map(location=center_location, zoom_start=12, control_scale=False, zoom_control=False)

        # Add markers for each waypoint
        for idx, point in enumerate(waypoints):
            folium.Marker(location=point, popup=f"Waypoint {idx + 1}").add_to(m)

        # Draw a line connecting the waypoints
        if len(waypoints) > 1:
            folium.PolyLine(locations=waypoints, color='blue', weight=5, opacity=0.8).add_to(m)

        # Get the HTML representation of the map
        map_html = m._repr_html_()
        return map_html

    # Update the horizontal slider label
    def update_horizontal_slider(self, value):
        self.ui.HorisontalLabel1.setText(f'H1: {value}')
        # Optionally, update waypoints or map based on slider value
        # self.update_map()

    # Update the first vertical slider label
    def update_vertical_slider1(self, value):
        self.ui.VerticalSliderLabel1.setText(f'V1: {value}')
        # Optionally, update waypoints or map based on slider value
        # self.update_map()

    # Update the second vertical slider label
    def update_vertical_slider2(self, value):
        self.ui.VerticalSlideLabel2.setText(f'V2: {value}')
        # Optionally, update waypoints or map based on slider value
        # self.update_map()

    # Optional method to update the map if waypoints change
    def update_map(self):
        map_html = self.generate_map_embed(self.waypoints)
        self.webview.setHtml(map_html)

if __name__ == '__main__':
    app = QApplication([])

    window = DashboardDemo()
    window.show()
    app.exec()
