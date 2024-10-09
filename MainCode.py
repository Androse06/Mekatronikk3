import os
import folium
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtCore import QUrl, QRect, Qt
from PySide6.QtWidgets import QApplication, QMainWindow
from ui_DesignerDemo import Ui_MainWindow

class DashboardDemo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Check if map.html exists, and generate if it doesn't
        if not os.path.exists('map.html'):
            print("Map file does not exist. Generating a new one.")
            self.generate_map_embed()  # Generate map with embedded Leaflet.js
        else:
            print("Map file exists. Loading...")

        # Replace the placeholder QWidget with QWebEngineView for displaying the map
        self.webview = QWebEngineView(self.ui.centralwidget)
        self.webview.setGeometry(QRect(330, 140, 361, 281))  # Recreate the geometry of the placeholder

        # Load the generated map
        map_path = os.path.abspath('map.html')
        self.webview.setUrl(QUrl.fromLocalFile(map_path))

        # Connect sliders to update label values
        self.ui.HorisontalSlider1.valueChanged.connect(self.update_horizontal_slider)
        self.ui.VerticalSlider1.valueChanged.connect(self.update_vertical_slider1)
        self.ui.VerticalSlider2.valueChanged.connect(self.update_vertical_slider2)

    def generate_map_embed(self):
        """Generate a Folium map and embed Leaflet resources directly."""
        m = folium.Map(location=[59.91, 10.75], zoom_start=12, control_scale=True)

        # Optionally, you can add more features, like markers, etc.
        folium.Marker([59.91, 10.75], popup="Marker in Oslo").add_to(m)

        # Save the map with embedded Leaflet resources
        m.save('map.html')

    def generate_map_absolute(self):
        """Generate a Folium map and replace online Leaflet resources with local absolute paths."""
        m = folium.Map(location=[59.91, 10.75], zoom_start=12)

        # Save the map as HTML
        m.save('map.html')

        # Get absolute paths to the local Leaflet.js and Leaflet.css
        leaflet_js_path = 'file:///' + os.path.abspath('leaflet.js').replace("\\", "/")
        leaflet_css_path = 'file:///' + os.path.abspath('leaflet.css').replace("\\", "/")

        # Read the generated HTML file
        with open('map.html', 'r') as file:
            html_content = file.read()

        # Replace online paths with local absolute paths
        html_content = html_content.replace(
            'https://unpkg.com/leaflet@1.7.1/dist/leaflet.js',
            leaflet_js_path
        )
        html_content = html_content.replace(
            'https://unpkg.com/leaflet@1.7.1/dist/leaflet.css',
            leaflet_css_path
        )

        # Save the modified HTML file
        with open('map.html', 'w') as file:
            file.write(html_content)

    # Update the horizontal slider label
    def update_horizontal_slider(self, value):
        self.ui.HorisontalLabel1.setText(f'Horizontal Slider: {value}')

    # Update the first vertical slider label
    def update_vertical_slider1(self, value):
        self.ui.VerticalSliderLabel1.setText(f'Vertical Slider 1: {value}')

    # Update the second vertical slider label
    def update_vertical_slider2(self, value):
        self.ui.VerticalSlideLabel2.setText(f'Vertical Slider 2: {value}')


if __name__ == '__main__':
    app = QApplication([])

    window = DashboardDemo()
    window.show()
    app.exec()
