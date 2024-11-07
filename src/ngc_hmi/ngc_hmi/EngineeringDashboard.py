# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'EngineeringDashboardAImlwZ.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDial, QDoubleSpinBox, QGraphicsView,
    QGridLayout, QHBoxLayout, QLCDNumber, QLabel,
    QLineEdit, QListView, QMainWindow, QMenuBar,
    QProgressBar, QPushButton, QSizePolicy, QSlider,
    QSpacerItem, QStatusBar, QTimeEdit, QVBoxLayout,
    QWidget)

class CompassDial(QDial):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        # Load the original image
        self.original_image = QPixmap('pictures/compass_2.png')  
        
        # Initial scaling of the compass image for the widget size
        self.compass_image = self.original_image.scaled(
            self.size(), 
            Qt.KeepAspectRatio, 
            Qt.SmoothTransformation  # Provide smooth transformation as positional argument
        )

        # Hide the default dial appearance
        self.setStyleSheet("QDial { background-color: transparent; border: none; }")
        self.setNotchesVisible(False)

    def resizeEvent(self, event):
        # Rescale the image when the widget is resized
        self.compass_image = self.original_image.scaled(
            self.size(), 
            Qt.KeepAspectRatio, 
            Qt.SmoothTransformation
        )
        super().resizeEvent(event)

    def paintEvent(self, event):
        painter = QPainter(self)

        # Center and fit the compass image on the dial
        rect = self.rect()
        compass_size = min(rect.width(), rect.height())
        compass_rect = QRect(
            (rect.width() - compass_size) // 2,
            (rect.height() - compass_size) // 2,
            compass_size, compass_size
        )

        # Apply rotation based on the dial value
        painter.translate(rect.center())
        painter.rotate(self.value())
        painter.translate(-rect.center())

        # Draw the rotated compass image only
        painter.drawPixmap(compass_rect, self.compass_image)



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")

        MainWindow.resize(1082, 836)
        MainWindow.setAnimated(True)

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")

        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")

        self.Global_Heading_Label = QLabel(self.centralwidget)
        self.Global_Heading_Label.setObjectName(u"Global_Heading_Label")

        self.verticalLayout_9.addWidget(self.Global_Heading_Label)

        self.Global_Heading_LCD = QLCDNumber(self.centralwidget)
        self.Global_Heading_LCD.setObjectName(u"Global_Heading_LCD")

        self.verticalLayout_9.addWidget(self.Global_Heading_LCD)

        self.Global_Speed_Label = QLabel(self.centralwidget)
        self.Global_Speed_Label.setObjectName(u"Global_Speed_Label")

        self.verticalLayout_9.addWidget(self.Global_Speed_Label)

        self.Global_Speed_LCD = QLCDNumber(self.centralwidget)
        self.Global_Speed_LCD.setObjectName(u"Global_Speed_LCD")

        self.verticalLayout_9.addWidget(self.Global_Speed_LCD)

        self.Global_Timer = QTimeEdit(self.centralwidget)
        self.Global_Timer.setObjectName(u"Global_Timer")

        self.verticalLayout_9.addWidget(self.Global_Timer)

        self.Gloabl_Throttle1_Label = QLabel(self.centralwidget)
        self.Gloabl_Throttle1_Label.setObjectName(u"Gloabl_Throttle1_Label")

        self.verticalLayout_9.addWidget(self.Gloabl_Throttle1_Label)

        self.Global_Throttle1_Status = QProgressBar(self.centralwidget)
        self.Global_Throttle1_Status.setObjectName(u"Global_Throttle1_Status")
        self.Global_Throttle1_Status.setMinimum(0)
        self.Global_Throttle1_Status.setMaximum(2000)
        self.Global_Throttle1_Status.setValue(0)

        self.verticalLayout_9.addWidget(self.Global_Throttle1_Status)

        self.Global_Throttle2_Label = QLabel(self.centralwidget)
        self.Global_Throttle2_Label.setObjectName(u"Global_Throttle2_Label")

        self.verticalLayout_9.addWidget(self.Global_Throttle2_Label)

        self.Global_Throttle2_Status = QProgressBar(self.centralwidget)
        self.Global_Throttle2_Status.setObjectName(u"Global_Throttle2_Status")
        self.Global_Throttle2_Status.setMinimum(0)
        self.Global_Throttle2_Status.setMaximum(2000)
        self.Global_Throttle2_Status.setValue(0)

        self.verticalLayout_9.addWidget(self.Global_Throttle2_Status)


        self.horizontalLayout_2.addLayout(self.verticalLayout_9)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalSpacer = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer)

        self.MapPlaceHolder = QGraphicsView(self.centralwidget)
        self.MapPlaceHolder.setObjectName(u"MapPlaceHolder")

        self.verticalLayout_10.addWidget(self.MapPlaceHolder)

        self.verticalLayout_10.setStretch(0, 1)
        self.verticalLayout_10.setStretch(1, 20)

        self.horizontalLayout_2.addLayout(self.verticalLayout_10)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.Extra_Input_2_Label = QLabel(self.centralwidget)
        self.Extra_Input_2_Label.setObjectName(u"Extra_Input_2_Label")

        self.gridLayout_4.addWidget(self.Extra_Input_2_Label, 4, 2, 1, 1)

        self.Extra_Slider_2 = QSlider(self.centralwidget)
        self.Extra_Slider_2.setObjectName(u"Extra_Slider_2")
        self.Extra_Slider_2.setOrientation(Qt.Horizontal)

        self.gridLayout_4.addWidget(self.Extra_Slider_2, 3, 0, 1, 2)

        self.Exit_Button = QPushButton(self.centralwidget)
        self.Exit_Button.setObjectName(u"Exit_Button")

        self.Exit_Button.setStyleSheet("""
            QPushButton {
                background-color: red;
                color: white;
                border-radius: 20px;  /* Adjust radius for roundness */
                padding: 10px;
            }
        """)
        self.gridLayout_4.addWidget(self.Exit_Button, 0, 2, 1, 1)

        self.Extra_Slider_1 = QSlider(self.centralwidget)
        self.Extra_Slider_1.setObjectName(u"Extra_Slider_1")
        self.Extra_Slider_1.setOrientation(Qt.Horizontal)

        self.gridLayout_4.addWidget(self.Extra_Slider_1, 1, 0, 1, 2)

        self.Extra_Input_1 = QLineEdit(self.centralwidget)
        self.Extra_Input_1.setObjectName(u"Extra_Input_1")

        self.gridLayout_4.addWidget(self.Extra_Input_1, 5, 0, 1, 1)

        self.Extra_LCD_1 = QLCDNumber(self.centralwidget)
        self.Extra_LCD_1.setObjectName(u"Extra_LCD_1")

        self.gridLayout_4.addWidget(self.Extra_LCD_1, 1, 2, 1, 1)

        self.Extra_S2_Label = QLabel(self.centralwidget)
        self.Extra_S2_Label.setObjectName(u"Extra_S2_Label")

        self.gridLayout_4.addWidget(self.Extra_S2_Label, 2, 0, 1, 1)

        self.SpinBox2 = QDoubleSpinBox(self.centralwidget)
        self.SpinBox2.setObjectName(u"SpinBox2")

        self.gridLayout_4.addWidget(self.SpinBox2, 7, 2, 1, 1)

        self.SpinBox1 = QDoubleSpinBox(self.centralwidget)
        self.SpinBox1.setObjectName(u"SpinBox1")

        self.gridLayout_4.addWidget(self.SpinBox1, 7, 0, 1, 1)

        self.Extra_LCD_2 = QLCDNumber(self.centralwidget)
        self.Extra_LCD_2.setObjectName(u"Extra_LCD_2")

        self.gridLayout_4.addWidget(self.Extra_LCD_2, 3, 2, 1, 1)

        self.Extra_Input_1_Label = QLabel(self.centralwidget)
        self.Extra_Input_1_Label.setObjectName(u"Extra_Input_1_Label")

        self.gridLayout_4.addWidget(self.Extra_Input_1_Label, 4, 0, 1, 1)

        self.Extra_Input_2 = QLineEdit(self.centralwidget)
        self.Extra_Input_2.setObjectName(u"Extra_Input_2")

        self.gridLayout_4.addWidget(self.Extra_Input_2, 5, 1, 1, 2)

        self.Extra_S1_Label = QLabel(self.centralwidget)
        self.Extra_S1_Label.setObjectName(u"Extra_S1_Label")

        self.gridLayout_4.addWidget(self.Extra_S1_Label, 6, 2, 1, 1)

        self.Extra_Button_1 = QPushButton(self.centralwidget)
        self.Extra_Button_1.setObjectName(u"Extra_Button_1")

        self.gridLayout_4.addWidget(self.Extra_Button_1, 0, 0, 1, 1)


        self.horizontalLayout_2.addLayout(self.gridLayout_4)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 5)
        self.horizontalLayout_2.setStretch(2, 1)

        self.verticalLayout_11.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.Standby_Label = QLabel(self.centralwidget)
        self.Standby_Label.setObjectName(u"Standby_Label")
        self.Standby_Label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.Standby_Label)

        self.Enable_Standby_Button = QPushButton(self.centralwidget)
        self.Enable_Standby_Button.setObjectName(u"Enable_Standby_Button")

        self.verticalLayout_7.addWidget(self.Enable_Standby_Button)

        self.Standby_Status_Icon = QProgressBar(self.centralwidget)
        self.Standby_Status_Icon.setObjectName(u"Standby_Status_Icon")
        self.Standby_Status_Icon.setValue(100)
        self.Standby_Status_Icon.setTextVisible(False)

        self.verticalLayout_7.addWidget(self.Standby_Status_Icon)

        self.Compass_Label = QLabel(self.centralwidget)
        self.Compass_Label.setObjectName(u"Compass_Label")
        self.Compass_Label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.Compass_Label)


        self.verticalLayout_8.addLayout(self.verticalLayout_7)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")

        self.Compass_Dial = CompassDial(self.centralwidget)
        self.Compass_Dial.setObjectName(u"Compass_Dial")
        self.Compass_Dial.setMaximum(360)
        self.Compass_Dial.setWrapping(True)
        self.Compass_Dial.setNotchesVisible(True)

        self.gridLayout_3.addWidget(self.Compass_Dial, 1, 1, 1, 1)

        self.West_Label = QLabel(self.centralwidget)
        self.West_Label.setObjectName(u"West_Label")
        self.West_Label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.West_Label, 1, 0, 1, 1)

        self.North_Label = QLabel(self.centralwidget)
        self.North_Label.setObjectName(u"North_Label")
        self.North_Label.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.North_Label, 0, 1, 1, 1)

        self.S_Label = QLabel(self.centralwidget)
        self.S_Label.setObjectName(u"S_Label")
        self.S_Label.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.S_Label, 2, 1, 1, 1)

        self.East_Label = QLabel(self.centralwidget)
        self.East_Label.setObjectName(u"East_Label")

        self.gridLayout_3.addWidget(self.East_Label, 1, 2, 1, 1)


        self.verticalLayout_8.addLayout(self.gridLayout_3)


        self.horizontalLayout_5.addLayout(self.verticalLayout_8)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.Sail_Heading_Dial = QDial(self.centralwidget)
        self.Sail_Heading_Dial.setObjectName(u"Sail_Heading_Dial")
        self.Sail_Heading_Dial.setMaximum(360)
        self.Sail_Heading_Dial.setWrapping(True)
        self.Sail_Heading_Dial.setNotchesVisible(True)

        self.verticalLayout_4.addWidget(self.Sail_Heading_Dial)

        self.Sail_Heading_LCD = QLCDNumber(self.centralwidget)
        self.Sail_Heading_LCD.setObjectName(u"Sail_Heading_LCD")

        self.verticalLayout_4.addWidget(self.Sail_Heading_LCD)


        self.gridLayout.addLayout(self.verticalLayout_4, 1, 0, 1, 1)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.Sail_Label = QLabel(self.centralwidget)
        self.Sail_Label.setObjectName(u"Sail_Label")
        self.Sail_Label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.Sail_Label)

        self.Enable_Sail_Button = QPushButton(self.centralwidget)
        self.Enable_Sail_Button.setObjectName(u"Enable_Sail_Button")

        self.verticalLayout_6.addWidget(self.Enable_Sail_Button)

        self.Sail_Status_Icon = QProgressBar(self.centralwidget)
        self.Sail_Status_Icon.setObjectName(u"Sail_Status_Icon")
        self.Sail_Status_Icon.setValue(100)
        self.Sail_Status_Icon.setTextVisible(False)

        self.verticalLayout_6.addWidget(self.Sail_Status_Icon)


        self.gridLayout.addLayout(self.verticalLayout_6, 0, 0, 1, 4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.Sail_Throttle_Slider = QSlider(self.centralwidget)
        self.Sail_Throttle_Slider.setObjectName(u"Sail_Throttle_Slider")
        self.Sail_Throttle_Slider.setMaximum(25)
        self.Sail_Throttle_Slider.setOrientation(Qt.Vertical)

        self.verticalLayout_5.addWidget(self.Sail_Throttle_Slider)

        self.Sail_Throttle_LCD = QLCDNumber(self.centralwidget)
        self.Sail_Throttle_LCD.setObjectName(u"Sail_Throttle_LCD")

        self.verticalLayout_5.addWidget(self.Sail_Throttle_LCD)


        self.gridLayout.addLayout(self.verticalLayout_5, 1, 3, 1, 1)


        self.horizontalLayout_5.addLayout(self.gridLayout)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.Dp_Label = QLabel(self.centralwidget)
        self.Dp_Label.setObjectName(u"Dp_Label")
        self.Dp_Label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.Dp_Label)

        self.Enable_Dp_Button = QPushButton(self.centralwidget)
        self.Enable_Dp_Button.setObjectName(u"Enable_Dp_Button")

        self.verticalLayout_3.addWidget(self.Enable_Dp_Button)

        self.Dp_Status_Icon = QProgressBar(self.centralwidget)
        self.Dp_Status_Icon.setObjectName(u"Dp_Status_Icon")
        self.Dp_Status_Icon.setValue(100)
        self.Dp_Status_Icon.setTextVisible(False)

        self.verticalLayout_3.addWidget(self.Dp_Status_Icon)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.Dp_Load_Button = QPushButton(self.centralwidget)
        self.Dp_Load_Button.setObjectName(u"Dp_Load_Button")

        self.horizontalLayout.addWidget(self.Dp_Load_Button)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.Lat_Dp_Label = QLabel(self.centralwidget)
        self.Lat_Dp_Label.setObjectName(u"Lat_Dp_Label")
        self.Lat_Dp_Label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.Lat_Dp_Label)

        self.Lat_Input_Dp = QLineEdit(self.centralwidget)
        self.Lat_Input_Dp.setObjectName(u"Lat_Input_Dp")

        self.verticalLayout_3.addWidget(self.Lat_Input_Dp)

        self.Lon_Dp_Label = QLabel(self.centralwidget)
        self.Lon_Dp_Label.setObjectName(u"Lon_Dp_Label")
        self.Lon_Dp_Label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.Lon_Dp_Label)

        self.Lon_Input_Dp = QLineEdit(self.centralwidget)
        self.Lon_Input_Dp.setObjectName(u"Lon_Input_Dp")

        self.verticalLayout_3.addWidget(self.Lon_Input_Dp)

        self.Deviation_Dp_Label = QLabel(self.centralwidget)
        self.Deviation_Dp_Label.setObjectName(u"Deviation_Dp_Label")
        self.Deviation_Dp_Label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.Deviation_Dp_Label)

        self.Deviation_Dp_LCD = QLCDNumber(self.centralwidget)
        self.Deviation_Dp_LCD.setObjectName(u"Deviation_Dp_LCD")

        self.verticalLayout_3.addWidget(self.Deviation_Dp_LCD)


        self.horizontalLayout_5.addLayout(self.verticalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.Track_Label = QLabel(self.centralwidget)
        self.Track_Label.setObjectName(u"Track_Label")
        self.Track_Label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.Track_Label)

        self.Enable_Track_Button = QPushButton(self.centralwidget)
        self.Enable_Track_Button.setObjectName(u"Enable_Track_Button")

        self.verticalLayout.addWidget(self.Enable_Track_Button)

        self.Track_Status_Icon = QProgressBar(self.centralwidget)
        self.Track_Status_Icon.setObjectName(u"Track_Status_Icon")
        self.Track_Status_Icon.setValue(100)
        self.Track_Status_Icon.setTextVisible(False)

        self.verticalLayout.addWidget(self.Track_Status_Icon)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.Track_Load_Button = QPushButton(self.centralwidget)
        self.Track_Load_Button.setObjectName(u"Track_Load_Button")

        self.horizontalLayout_3.addWidget(self.Track_Load_Button)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.Lat_Label_Track = QLabel(self.centralwidget)
        self.Lat_Label_Track.setObjectName(u"Lat_Label_Track")
        self.Lat_Label_Track.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.Lat_Label_Track)

        self.Lat_Input_Track = QLineEdit(self.centralwidget)
        self.Lat_Input_Track.setObjectName(u"Lat_Input_Track")

        self.verticalLayout.addWidget(self.Lat_Input_Track)

        self.Lon_Label_Track = QLabel(self.centralwidget)
        self.Lon_Label_Track.setObjectName(u"Lon_Label_Track")
        self.Lon_Label_Track.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.Lon_Label_Track)

        self.Lon_Input_Track = QLineEdit(self.centralwidget)
        self.Lon_Input_Track.setObjectName(u"Lon_Input_Track")

        self.verticalLayout.addWidget(self.Lon_Input_Track)

        self.Add_WayPoint_Button = QPushButton(self.centralwidget)
        self.Add_WayPoint_Button.setObjectName(u"Add_WayPoint_Button")

        self.verticalLayout.addWidget(self.Add_WayPoint_Button)

        self.Clear_Waypoint_Button = QPushButton(self.centralwidget)
        self.Clear_Waypoint_Button.setObjectName(u"Clear_Waypoint_Button")

        self.verticalLayout.addWidget(self.Clear_Waypoint_Button)


        self.horizontalLayout_4.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.Waypoints_Label = QLabel(self.centralwidget)
        self.Waypoints_Label.setObjectName(u"Waypoints_Label")
        self.Waypoints_Label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.Waypoints_Label)

        self.WayPoint_ListView = QListView(self.centralwidget)
        self.WayPoint_ListView.setObjectName(u"WayPoint_ListView")

        self.verticalLayout_2.addWidget(self.WayPoint_ListView)


        self.horizontalLayout_4.addLayout(self.verticalLayout_2)


        self.horizontalLayout_5.addLayout(self.horizontalLayout_4)


        self.verticalLayout_11.addLayout(self.horizontalLayout_5)

        self.verticalLayout_11.setStretch(0, 5)
        self.verticalLayout_11.setStretch(1, 1)

        self.gridLayout_2.addLayout(self.verticalLayout_11, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1082, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Global_Heading_Label.setText(QCoreApplication.translate("MainWindow", u"Heading", None))
        self.Global_Speed_Label.setText(QCoreApplication.translate("MainWindow", u"Speed", None))
        self.Gloabl_Throttle1_Label.setText(QCoreApplication.translate("MainWindow", u"TH1 RPS", None))
        self.Global_Throttle2_Label.setText(QCoreApplication.translate("MainWindow", u"TH2 RPS", None))
        self.Extra_Input_2_Label.setText(QCoreApplication.translate("MainWindow", u"Extra I2", None))
        self.Exit_Button.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.Extra_S2_Label.setText(QCoreApplication.translate("MainWindow", u"Extra S2", None))
        self.Extra_Input_1_Label.setText(QCoreApplication.translate("MainWindow", u"Extra I1", None))
        self.Extra_S1_Label.setText(QCoreApplication.translate("MainWindow", u"Extra S1", None))
        self.Extra_Button_1.setText(QCoreApplication.translate("MainWindow", u"ExtraB1", None))
        self.Standby_Label.setText(QCoreApplication.translate("MainWindow", u"STANDBY", None))
        self.Enable_Standby_Button.setText(QCoreApplication.translate("MainWindow", u"Enable", None))
        self.Compass_Label.setText(QCoreApplication.translate("MainWindow", u"COMPASS", None))
        self.West_Label.setText(QCoreApplication.translate("MainWindow", u"W", None))
        self.North_Label.setText(QCoreApplication.translate("MainWindow", u"N", None))
        self.S_Label.setText(QCoreApplication.translate("MainWindow", u"S", None))
        self.East_Label.setText(QCoreApplication.translate("MainWindow", u"E", None))
        self.Sail_Label.setText(QCoreApplication.translate("MainWindow", u"SAIL", None))
        self.Enable_Sail_Button.setText(QCoreApplication.translate("MainWindow", u"Enable", None))
        self.Dp_Label.setText(QCoreApplication.translate("MainWindow", u"DP", None))
        self.Enable_Dp_Button.setText(QCoreApplication.translate("MainWindow", u"Enable", None))
        self.Dp_Load_Button.setText(QCoreApplication.translate("MainWindow", u"Load Position", None))
        self.Lat_Dp_Label.setText(QCoreApplication.translate("MainWindow", u"LAT", None))
        self.Lon_Dp_Label.setText(QCoreApplication.translate("MainWindow", u"LON", None))
        self.Deviation_Dp_Label.setText(QCoreApplication.translate("MainWindow", u"DEVIATION", None))
        self.Track_Label.setText(QCoreApplication.translate("MainWindow", u"TRACK", None))
        self.Enable_Track_Button.setText(QCoreApplication.translate("MainWindow", u"Enable", None))
        self.Track_Load_Button.setText(QCoreApplication.translate("MainWindow", u"Load Route", None))
        self.Lat_Label_Track.setText(QCoreApplication.translate("MainWindow", u"LAT", None))
        self.Lon_Label_Track.setText(QCoreApplication.translate("MainWindow", u"LON", None))
        self.Add_WayPoint_Button.setText(QCoreApplication.translate("MainWindow", u"Add waypoint", None))
        self.Clear_Waypoint_Button.setText(QCoreApplication.translate("MainWindow", u"Clear waypoints", None))
        self.Waypoints_Label.setText(QCoreApplication.translate("MainWindow", u"Waypoints", None))
    # retranslateUi


