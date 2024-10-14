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
        try:
            self.process = subprocess.Popen(["opencpn"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        except FileNotFoundError:
            print("OpenCPN not found. Please ensure OpenCPN is installed and in your PATH.")
            self.process = None
            return

        # Poll for OpenCPN window ID
        window_id = self.get_window_id()

        if window_id:
            print(f"OpenCPN window ID: {window_id}")
            # Embed the OpenCPN window into the PyQt application
            self.embed_opencpn(window_id)
        else:
            print("Failed to get OpenCPN window ID. Is OpenCPN running?")

    def get_window_id(self, max_retries=10, wait_time=1):
        # Use `xdotool` to get the OpenCPN window ID with retries
        for _ in range(max_retries):
            try:
                result = subprocess.run(["xdotool", "search", "--name", "OpenCPN"], stdout=subprocess.PIPE)
                window_id = result.stdout.decode().strip()
                if window_id:
                    return window_id
            except Exception as e:
                print(f"Error fetching OpenCPN window ID: {e}")
            time.sleep(wait_time)  # Wait and retry
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
        # Ensure OpenCPN is terminated when the application is closed
        if self.process:
            try:
                self.process.terminate()
                self.process.wait()  # Wait for OpenCPN to exit cleanly
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
