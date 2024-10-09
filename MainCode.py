import os
import folium
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWebEngineCore import QWebEngineSettings
from PySide6.QtCore import QRect
from PySide6.QtWidgets import QApplication, QMainWindow
from ui_DesignerDemo import Ui_MainWindow

class DashboardDemo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Replace the placeholder QWidget with QWebEngineView for displaying the map
        self.webview = QWebEngineView(self.ui.centralwidget)
        self.webview.setGeometry(QRect(330, 140, 361, 281))  # Recreate the geometry of the placeholder

        # Enable JavaScript and adjust security settings
        self.webview.settings().setAttribute(QWebEngineSettings.JavascriptEnabled, True)
        self.webview.settings().setAttribute(QWebEngineSettings.LocalContentCanAccessFileUrls, True)
        self.webview.settings().setAttribute(QWebEngineSettings.LocalContentCanAccessRemoteUrls, True)

        # Generate the map HTML and set it directly
        map_html = self.generate_map_embed()
        self.webview.setHtml(map_html)

        # Connect sliders to update label values
        self.ui.HorisontalSlider1.valueChanged.connect(self.update_horizontal_slider)
        self.ui.VerticalSlider1.valueChanged.connect(self.update_vertical_slider1)
        self.ui.VerticalSlider2.valueChanged.connect(self.update_vertical_slider2)

    def generate_map_embed(self):
        """Generate a Folium map and return the HTML representation."""
        m = folium.Map(location=[59.91, 10.75], zoom_start=12, control_scale=True)
        folium.Marker([59.91, 10.75], popup="Marker in Oslo").add_to(m)

        # Get the HTML representation of the map (includes embedded resources)
        map_html = m._repr_html_()
        return map_html

    # Update the horizontal slider label
    def update_horizontal_slider(self, value):
        self.ui.HorisontalLabel1.setText(f'H1: {value}')

    # Update the first vertical slider label
    def update_vertical_slider1(self, value):
        self.ui.VerticalSliderLabel1.setText(f'V1: {value}')

    # Update the second vertical slider label
    def update_vertical_slider2(self, value):
        self.ui.VerticalSlideLabel2.setText(f'V2: {value}')

if __name__ == '__main__':
    app = QApplication([])

    window = DashboardDemo()
    window.show()
    app.exec()
