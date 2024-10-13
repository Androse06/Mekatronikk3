import sys
import subprocess
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PySide6.QtGui import QWindow
import time
import os

class MainApp(QMainWindow):
    def __init__(self):
        super(MainApp, self).__init__()

        self.setWindowTitle("OpenCPN Embedded in PyQt")

        # Create a placeholder widget
        self.container = QWidget(self)
        self.setCentralWidget(self.container)

        layout = QVBoxLayout()
        self.container.setLayout(layout)

        # Launch OpenCPN
        self.process = subprocess.Popen(["opencpn"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        # Wait a bit for OpenCPN to launch and get the window ID
        time.sleep(5)  # Adjust this time if OpenCPN takes longer to start
        window_id = self.get_window_id()

        if window_id:
            print(f"OpenCPN window ID: {window_id}")
            # Embed the OpenCPN window into the PyQt application
            self.embed_opencpn(window_id)
        else:
            print("Failed to get OpenCPN window ID")

    def get_window_id(self):
        # Use `xdotool` to get the OpenCPN window ID
        try:
            result = subprocess.run(["xdotool", "search", "--name", "OpenCPN"], stdout=subprocess.PIPE)
            window_id = result.stdout.decode().strip()
            return window_id if window_id else None
        except Exception as e:
            print(f"Error fetching OpenCPN window ID: {e}")
            return None

    def embed_opencpn(self, window_id):
        # Create a QWindow from the OpenCPN window ID
        try:
            window = QWindow.fromWinId(int(window_id))
            window.setFlags(Qt.FramelessWindowHint)

            # Create a QWidget container to embed the QWindow
            widget = QWidget.createWindowContainer(window, self)
            widget.setMinimumSize(800, 600)
            widget.setFocusPolicy(Qt.StrongFocus)

            # Add the widget to the layout
            self.container.layout().addWidget(widget)
        except Exception as e:
            print(f"Error embedding OpenCPN window: {e}")

    def closeEvent(self, event):
        # Make sure to terminate OpenCPN when the application is closed
        try:
            self.process.terminate()
        except Exception as e:
            print(f"Error terminating OpenCPN process: {e}")
        event.accept()


def main():
    app = QApplication(sys.argv)
    main_window = MainApp()
    main_window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
