# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Darkmode V3wHIETd.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
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
    QWidget, QFrame, QLayout)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(2016, 1166)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet(u"background-color: rgb(69, 69, 69);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_8 = QGridLayout(self.centralwidget)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_21 = QGridLayout()
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.frame_7 = QFrame(self.centralwidget)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(300, 364))
        self.frame_7.setMaximumSize(QSize(300, 364))
        self.frame_7.setStyleSheet(u"background-color: rgb(39, 50, 50);\n"
"color: rgb(240, 240, 240);")
        self.frame_7.setFrameShape(QFrame.Panel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.frame_7.setLineWidth(3)
        self.gridLayout_24 = QGridLayout(self.frame_7)
        self.gridLayout_24.setObjectName(u"gridLayout_24")
        self.gridLayout_24.setContentsMargins(-1, 20, -1, -1)
        self.Waypoints_Label = QLabel(self.frame_7)
        self.Waypoints_Label.setObjectName(u"Waypoints_Label")
        font = QFont()
        font.setPointSize(10)
        self.Waypoints_Label.setFont(font)
        self.Waypoints_Label.setAlignment(Qt.AlignCenter)

        self.gridLayout_24.addWidget(self.Waypoints_Label, 10, 0, 1, 1)

        self.line_6 = QFrame(self.frame_7)
        self.line_6.setObjectName(u"line_6")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.line_6.sizePolicy().hasHeightForWidth())
        self.line_6.setSizePolicy(sizePolicy1)
        self.line_6.setFrameShadow(QFrame.Raised)
        self.line_6.setLineWidth(3)
        self.line_6.setFrameShape(QFrame.HLine)

        self.gridLayout_24.addWidget(self.line_6, 1, 0, 1, 1)

        self.verticalSpacer_9 = QSpacerItem(10, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_24.addItem(self.verticalSpacer_9, 9, 0, 1, 1)

        self.WayPoint_ListView = QListView(self.frame_7)
        self.WayPoint_ListView.setObjectName(u"WayPoint_ListView")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.WayPoint_ListView.sizePolicy().hasHeightForWidth())
        self.WayPoint_ListView.setSizePolicy(sizePolicy2)
        self.WayPoint_ListView.setMinimumSize(QSize(120, 70))
        self.WayPoint_ListView.setMaximumSize(QSize(200, 200))
        self.WayPoint_ListView.setStyleSheet(u"border-color: rgb(240, 240, 240);")

        self.gridLayout_24.addWidget(self.WayPoint_ListView, 11, 0, 1, 1, Qt.AlignHCenter)

        self.Track_Load_Button = QPushButton(self.frame_7)
        self.Track_Load_Button.setObjectName(u"Track_Load_Button")
        sizePolicy.setHeightForWidth(self.Track_Load_Button.sizePolicy().hasHeightForWidth())
        self.Track_Load_Button.setSizePolicy(sizePolicy)
        self.Track_Load_Button.setMinimumSize(QSize(70, 25))
        self.Track_Load_Button.setMaximumSize(QSize(70, 25))
        self.Track_Load_Button.setFont(font)
        self.Track_Load_Button.setStyleSheet(u"background-color: rgb(116, 116, 116);\n"
"color: rgb(240, 240, 240);\n"
"\n"
"")

        self.gridLayout_24.addWidget(self.Track_Load_Button, 6, 0, 1, 1, Qt.AlignHCenter)

        self.Track_Status_Icon = QProgressBar(self.frame_7)
        self.Track_Status_Icon.setObjectName(u"Track_Status_Icon")
        sizePolicy.setHeightForWidth(self.Track_Status_Icon.sizePolicy().hasHeightForWidth())
        self.Track_Status_Icon.setSizePolicy(sizePolicy)
        self.Track_Status_Icon.setMinimumSize(QSize(70, 15))
        self.Track_Status_Icon.setMaximumSize(QSize(70, 15))
        self.Track_Status_Icon.setStyleSheet(u" QProgressBar::chunk {\n"
"     background-color: #f97f55;\n"
" }")
        self.Track_Status_Icon.setValue(100)
        self.Track_Status_Icon.setTextVisible(False)

        self.gridLayout_24.addWidget(self.Track_Status_Icon, 4, 0, 1, 1, Qt.AlignHCenter)

        self.Track_Label = QLabel(self.frame_7)
        self.Track_Label.setObjectName(u"Track_Label")
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(True)
        font1.setWeight(QFont.Weight.Bold)
        self.Track_Label.setFont(font1)
        self.Track_Label.setAlignment(Qt.AlignCenter)

        self.gridLayout_24.addWidget(self.Track_Label, 0, 0, 1, 1)

        self.verticalSpacer_19 = QSpacerItem(20, 15, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_24.addItem(self.verticalSpacer_19, 5, 0, 1, 1)

        self.verticalSpacer_16 = QSpacerItem(15, 15, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_24.addItem(self.verticalSpacer_16, 2, 0, 1, 1)

        self.Enable_Track_Button = QPushButton(self.frame_7)
        self.Enable_Track_Button.setObjectName(u"Enable_Track_Button")
        sizePolicy.setHeightForWidth(self.Enable_Track_Button.sizePolicy().hasHeightForWidth())
        self.Enable_Track_Button.setSizePolicy(sizePolicy)
        self.Enable_Track_Button.setMinimumSize(QSize(70, 25))
        self.Enable_Track_Button.setMaximumSize(QSize(70, 25))
        self.Enable_Track_Button.setFont(font)
        self.Enable_Track_Button.setStyleSheet(u"background-color: rgb(116, 116, 116);\n"
"color: rgb(240, 240, 240);\n"
"\n"
"")

        self.gridLayout_24.addWidget(self.Enable_Track_Button, 3, 0, 1, 1, Qt.AlignHCenter)

        self.Clear_Waypoint_Button = QPushButton(self.frame_7)
        self.Clear_Waypoint_Button.setObjectName(u"Clear_Waypoint_Button")
        sizePolicy.setHeightForWidth(self.Clear_Waypoint_Button.sizePolicy().hasHeightForWidth())
        self.Clear_Waypoint_Button.setSizePolicy(sizePolicy)
        self.Clear_Waypoint_Button.setMinimumSize(QSize(70, 25))
        self.Clear_Waypoint_Button.setMaximumSize(QSize(70, 25))
        self.Clear_Waypoint_Button.setFont(font)
        self.Clear_Waypoint_Button.setStyleSheet(u"background-color: rgb(116, 116, 116);\n"
"color: rgb(240, 240, 240);\n"
"\n"
"")

        self.gridLayout_24.addWidget(self.Clear_Waypoint_Button, 7, 0, 1, 1, Qt.AlignHCenter)


        self.gridLayout_21.addWidget(self.frame_7, 0, 0, 1, 1, Qt.AlignRight)


        self.gridLayout_6.addLayout(self.gridLayout_21, 0, 0, 1, 1)


        self.gridLayout_8.addLayout(self.gridLayout_6, 4, 12, 1, 1)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_17 = QGridLayout()
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.frame_4 = QFrame(self.centralwidget)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy3)
        self.frame_4.setMinimumSize(QSize(0, 364))
        self.frame_4.setMaximumSize(QSize(16777215, 364))
        self.frame_4.setStyleSheet(u"/*background-color: rgb(66, 36, 36);*/\n"
"/*background-color: rgb(55, 41, 41);*/\n"
"background-color: rgb(55, 38, 38);\n"
"\n"
"color: rgb(240, 240, 240);  /*background-color: rgb(44, 44, 44);")
        self.frame_4.setFrameShape(QFrame.Panel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.frame_4.setLineWidth(3)
        self.gridLayout_18 = QGridLayout(self.frame_4)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.gridLayout_18.setContentsMargins(-1, 20, -1, -1)
        self.Enable_Standby_Button = QPushButton(self.frame_4)
        self.Enable_Standby_Button.setObjectName(u"Enable_Standby_Button")
        sizePolicy.setHeightForWidth(self.Enable_Standby_Button.sizePolicy().hasHeightForWidth())
        self.Enable_Standby_Button.setSizePolicy(sizePolicy)
        self.Enable_Standby_Button.setMinimumSize(QSize(70, 25))
        self.Enable_Standby_Button.setMaximumSize(QSize(70, 25))
        self.Enable_Standby_Button.setFont(font)
        self.Enable_Standby_Button.setStyleSheet(u"background-color: rgb(116, 116, 116);\n"
"color: rgb(240, 240, 240);\n"
"\n"
"")

        self.gridLayout_18.addWidget(self.Enable_Standby_Button, 3, 0, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)

        self.verticalSpacer_13 = QSpacerItem(15, 15, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_18.addItem(self.verticalSpacer_13, 2, 0, 1, 1)

        self.Standby_Status_Icon = QProgressBar(self.frame_4)
        self.Standby_Status_Icon.setObjectName(u"Standby_Status_Icon")
        sizePolicy.setHeightForWidth(self.Standby_Status_Icon.sizePolicy().hasHeightForWidth())
        self.Standby_Status_Icon.setSizePolicy(sizePolicy)
        self.Standby_Status_Icon.setMinimumSize(QSize(70, 15))
        self.Standby_Status_Icon.setMaximumSize(QSize(70, 15))
        palette = QPalette()
        brush = QBrush(QColor(240, 240, 240, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(55, 38, 38, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush2 = QBrush(QColor(240, 240, 240, 128))
        brush2.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        brush3 = QBrush(QColor(240, 240, 240, 128))
        brush3.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush3)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        brush4 = QBrush(QColor(240, 240, 240, 128))
        brush4.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.Standby_Status_Icon.setPalette(palette)
        self.Standby_Status_Icon.setAutoFillBackground(False)
        self.Standby_Status_Icon.setStyleSheet(u" QProgressBar::chunk {\n"
"     background-color: #f97f55;\n"
" }")
        self.Standby_Status_Icon.setValue(100)
        self.Standby_Status_Icon.setTextVisible(False)

        self.gridLayout_18.addWidget(self.Standby_Status_Icon, 4, 0, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_18.addItem(self.verticalSpacer, 5, 0, 1, 1)

        self.Standby_Label = QLabel(self.frame_4)
        self.Standby_Label.setObjectName(u"Standby_Label")
        self.Standby_Label.setFont(font1)
        self.Standby_Label.setAlignment(Qt.AlignCenter)

        self.gridLayout_18.addWidget(self.Standby_Label, 0, 0, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)

        self.line_3 = QFrame(self.frame_4)
        self.line_3.setObjectName(u"line_3")
        sizePolicy1.setHeightForWidth(self.line_3.sizePolicy().hasHeightForWidth())
        self.line_3.setSizePolicy(sizePolicy1)
        self.line_3.setFrameShadow(QFrame.Raised)
        self.line_3.setLineWidth(3)
        self.line_3.setFrameShape(QFrame.HLine)

        self.gridLayout_18.addWidget(self.line_3, 1, 0, 1, 1)


        self.gridLayout_17.addWidget(self.frame_4, 0, 0, 1, 1)


        self.gridLayout_4.addLayout(self.gridLayout_17, 0, 0, 1, 1)


        self.gridLayout_8.addLayout(self.gridLayout_4, 4, 5, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(10, 10, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_5, 2, 0, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_3, 4, 8, 1, 1)

        self.gridLayout_13 = QGridLayout()
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.gridLayout_20 = QGridLayout()
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.frame_6 = QFrame(self.centralwidget)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(0, 364))
        self.frame_6.setMaximumSize(QSize(16777215, 364))
        self.frame_6.setStyleSheet(u"background-color: rgb(39, 50, 50);\n"
"color: rgb(240, 240, 240);")
        self.frame_6.setFrameShape(QFrame.Panel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.frame_6.setLineWidth(3)
        self.gridLayout_23 = QGridLayout(self.frame_6)
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.gridLayout_23.setContentsMargins(-1, 20, -1, -1)
        self.Enable_Dp_Button = QPushButton(self.frame_6)
        self.Enable_Dp_Button.setObjectName(u"Enable_Dp_Button")
        sizePolicy.setHeightForWidth(self.Enable_Dp_Button.sizePolicy().hasHeightForWidth())
        self.Enable_Dp_Button.setSizePolicy(sizePolicy)
        self.Enable_Dp_Button.setMinimumSize(QSize(70, 25))
        self.Enable_Dp_Button.setMaximumSize(QSize(70, 25))
        self.Enable_Dp_Button.setFont(font)
        self.Enable_Dp_Button.setStyleSheet(u"background-color: rgb(116, 116, 116);\n"
"color: rgb(240, 240, 240);\n"
"\n"
"")

        self.gridLayout_23.addWidget(self.Enable_Dp_Button, 3, 0, 1, 1, Qt.AlignHCenter)

        self.Dp_Label = QLabel(self.frame_6)
        self.Dp_Label.setObjectName(u"Dp_Label")
        self.Dp_Label.setFont(font1)
        self.Dp_Label.setAlignment(Qt.AlignCenter)

        self.gridLayout_23.addWidget(self.Dp_Label, 0, 0, 1, 1)

        self.Dp_Status_Icon = QProgressBar(self.frame_6)
        self.Dp_Status_Icon.setObjectName(u"Dp_Status_Icon")
        sizePolicy.setHeightForWidth(self.Dp_Status_Icon.sizePolicy().hasHeightForWidth())
        self.Dp_Status_Icon.setSizePolicy(sizePolicy)
        self.Dp_Status_Icon.setMinimumSize(QSize(70, 15))
        self.Dp_Status_Icon.setMaximumSize(QSize(70, 15))
        self.Dp_Status_Icon.setStyleSheet(u" QProgressBar::chunk {\n"
"     background-color: #f97f55;\n"
" }")
        self.Dp_Status_Icon.setValue(100)
        self.Dp_Status_Icon.setTextVisible(False)

        self.gridLayout_23.addWidget(self.Dp_Status_Icon, 4, 0, 1, 1, Qt.AlignHCenter)

        self.verticalSpacer_15 = QSpacerItem(20, 15, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_23.addItem(self.verticalSpacer_15, 2, 0, 1, 1)

        self.line_5 = QFrame(self.frame_6)
        self.line_5.setObjectName(u"line_5")
        sizePolicy1.setHeightForWidth(self.line_5.sizePolicy().hasHeightForWidth())
        self.line_5.setSizePolicy(sizePolicy1)
        self.line_5.setFrameShadow(QFrame.Raised)
        self.line_5.setLineWidth(3)
        self.line_5.setFrameShape(QFrame.HLine)

        self.gridLayout_23.addWidget(self.line_5, 1, 0, 1, 1)

        self.verticalSpacer_18 = QSpacerItem(20, 15, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_23.addItem(self.verticalSpacer_18, 5, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_23.addItem(self.verticalSpacer_2, 8, 0, 1, 1)

        self.Dp_Load_Button = QPushButton(self.frame_6)
        self.Dp_Load_Button.setObjectName(u"Dp_Load_Button")
        sizePolicy.setHeightForWidth(self.Dp_Load_Button.sizePolicy().hasHeightForWidth())
        self.Dp_Load_Button.setSizePolicy(sizePolicy)
        self.Dp_Load_Button.setMinimumSize(QSize(70, 25))
        self.Dp_Load_Button.setMaximumSize(QSize(70, 25))
        self.Dp_Load_Button.setFont(font)
        self.Dp_Load_Button.setStyleSheet(u"background-color: rgb(116, 116, 116);\n"
"color: rgb(240, 240, 240);\n"
"\n"
"")

        self.gridLayout_23.addWidget(self.Dp_Load_Button, 6, 0, 1, 1, Qt.AlignHCenter)

        self.verticalSpacer_20 = QSpacerItem(10, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_23.addItem(self.verticalSpacer_20, 12, 0, 1, 1)

        self.Deviation_Dp_LCD = QLCDNumber(self.frame_6)
        self.Deviation_Dp_LCD.setObjectName(u"Deviation_Dp_LCD")
        sizePolicy.setHeightForWidth(self.Deviation_Dp_LCD.sizePolicy().hasHeightForWidth())
        self.Deviation_Dp_LCD.setSizePolicy(sizePolicy)
        self.Deviation_Dp_LCD.setMinimumSize(QSize(80, 40))
        self.Deviation_Dp_LCD.setAcceptDrops(False)
        self.Deviation_Dp_LCD.setLayoutDirection(Qt.LeftToRight)
        self.Deviation_Dp_LCD.setAutoFillBackground(False)
        self.Deviation_Dp_LCD.setStyleSheet(u"QLCDNumber {\n"
"    border: 1px solid #f0f0f0;         /* Border color and width */\n"
"    border-radius: 4px;                /* Rounded corners */\n"
"    padding: 5px;                      /* Optional padding inside border */\n"
"    background-color: transparent;         /* Background color inside the border */\n"
"    color: #f0f0f0;                    /* Color for the LCD digits */\n"
"}\n"
"")
        self.Deviation_Dp_LCD.setFrameShape(QFrame.Box)
        self.Deviation_Dp_LCD.setFrameShadow(QFrame.Raised)
        self.Deviation_Dp_LCD.setMidLineWidth(0)
        self.Deviation_Dp_LCD.setSmallDecimalPoint(False)
        self.Deviation_Dp_LCD.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout_23.addWidget(self.Deviation_Dp_LCD, 11, 0, 1, 1, Qt.AlignHCenter)

        self.verticalSpacer_22 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_23.addItem(self.verticalSpacer_22, 10, 0, 1, 1)

        self.Deviation_Dp_Label = QLabel(self.frame_6)
        self.Deviation_Dp_Label.setObjectName(u"Deviation_Dp_Label")
        self.Deviation_Dp_Label.setFont(font)
        self.Deviation_Dp_Label.setAlignment(Qt.AlignCenter)

        self.gridLayout_23.addWidget(self.Deviation_Dp_Label, 9, 0, 1, 1)


        self.gridLayout_20.addWidget(self.frame_6, 0, 0, 1, 1)


        self.gridLayout_13.addLayout(self.gridLayout_20, 0, 0, 1, 1)


        self.gridLayout_8.addLayout(self.gridLayout_13, 4, 9, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(80, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_4, 4, 10, 1, 1)

        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_19 = QGridLayout()
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.frame_5 = QFrame(self.centralwidget)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(0, 364))
        self.frame_5.setMaximumSize(QSize(16777215, 364))
        self.frame_5.setStyleSheet(u"/*background-color: rgb(44, 44, 44); */\n"
"/*background-color: rgb(34, 47, 47); */\n"
"background-color: rgb(39, 50, 50);\n"
"color: rgb(240, 240, 240);")
        self.frame_5.setFrameShape(QFrame.Panel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.frame_5.setLineWidth(3)
        self.gridLayout_22 = QGridLayout(self.frame_5)
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.gridLayout_22.setContentsMargins(-1, 20, -1, -1)
        self.Sail_Status_Icon = QProgressBar(self.frame_5)
        self.Sail_Status_Icon.setObjectName(u"Sail_Status_Icon")
        sizePolicy.setHeightForWidth(self.Sail_Status_Icon.sizePolicy().hasHeightForWidth())
        self.Sail_Status_Icon.setSizePolicy(sizePolicy)
        self.Sail_Status_Icon.setMinimumSize(QSize(70, 15))
        self.Sail_Status_Icon.setMaximumSize(QSize(70, 15))
        self.Sail_Status_Icon.setStyleSheet(u" QProgressBar::chunk {\n"
"     background-color: #f97f55;\n"
" }")
        self.Sail_Status_Icon.setValue(100)
        self.Sail_Status_Icon.setTextVisible(False)

        self.gridLayout_22.addWidget(self.Sail_Status_Icon, 8, 1, 1, 2, Qt.AlignHCenter)

        self.Sail_Throttle_LCD = QLCDNumber(self.frame_5)
        self.Sail_Throttle_LCD.setObjectName(u"Sail_Throttle_LCD")
        sizePolicy.setHeightForWidth(self.Sail_Throttle_LCD.sizePolicy().hasHeightForWidth())
        self.Sail_Throttle_LCD.setSizePolicy(sizePolicy)
        self.Sail_Throttle_LCD.setMinimumSize(QSize(80, 40))
        self.Sail_Throttle_LCD.setStyleSheet(u"QLCDNumber {\n"
"    border: 1px solid #f0f0f0;         /* Border color and width */\n"
"    border-radius: 4px;                /* Rounded corners */\n"
"    padding: 5px;                      /* Optional padding inside border */\n"
"    background-color: transparent;         /* Background color inside the border */\n"
"    color: #f0f0f0;                    /* Color for the LCD digits */\n"
"}\n"
"")
        self.Sail_Throttle_LCD.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout_22.addWidget(self.Sail_Throttle_LCD, 14, 2, 1, 1)

        self.Sail_Label = QLabel(self.frame_5)
        self.Sail_Label.setObjectName(u"Sail_Label")
        self.Sail_Label.setFont(font1)
        self.Sail_Label.setAlignment(Qt.AlignCenter)

        self.gridLayout_22.addWidget(self.Sail_Label, 0, 1, 1, 2)

        self.Sail_Heading_Dial = QDial(self.frame_5)
        self.Sail_Heading_Dial.setObjectName(u"Sail_Heading_Dial")
        sizePolicy.setHeightForWidth(self.Sail_Heading_Dial.sizePolicy().hasHeightForWidth())
        self.Sail_Heading_Dial.setSizePolicy(sizePolicy)
        self.Sail_Heading_Dial.setMinimumSize(QSize(120, 120))
        font2 = QFont()
        font2.setStyleStrategy(QFont.PreferDefault)
        self.Sail_Heading_Dial.setFont(font2)
        self.Sail_Heading_Dial.setFocusPolicy(Qt.WheelFocus)
        self.Sail_Heading_Dial.setStyleSheet(u"background-color: rgb(202, 202, 202);")
        self.Sail_Heading_Dial.setMaximum(360)
        self.Sail_Heading_Dial.setSliderPosition(180)
        self.Sail_Heading_Dial.setWrapping(True)
        self.Sail_Heading_Dial.setNotchesVisible(True)

        self.gridLayout_22.addWidget(self.Sail_Heading_Dial, 12, 1, 1, 1)

        self.label_4 = QLabel(self.frame_5)
        self.label_4.setObjectName(u"label_4")
        font3 = QFont()
        font3.setPointSize(8)
        self.label_4.setFont(font3)

        self.gridLayout_22.addWidget(self.label_4, 10, 1, 1, 1)

        self.horizontalSpacer_18 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_22.addItem(self.horizontalSpacer_18, 12, 3, 1, 1)

        self.verticalSpacer_21 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_22.addItem(self.verticalSpacer_21, 15, 1, 1, 1)

        self.line_4 = QFrame(self.frame_5)
        self.line_4.setObjectName(u"line_4")
        sizePolicy1.setHeightForWidth(self.line_4.sizePolicy().hasHeightForWidth())
        self.line_4.setSizePolicy(sizePolicy1)
        self.line_4.setMinimumSize(QSize(500, 0))
        self.line_4.setFrameShadow(QFrame.Raised)
        self.line_4.setLineWidth(3)
        self.line_4.setFrameShape(QFrame.HLine)

        self.gridLayout_22.addWidget(self.line_4, 1, 1, 1, 2, Qt.AlignHCenter)

        self.Sail_Throttle_Slider = QSlider(self.frame_5)
        self.Sail_Throttle_Slider.setObjectName(u"Sail_Throttle_Slider")
        self.Sail_Throttle_Slider.setStyleSheet(u"QSlider::handle:vertical {\n"
"    height: 10px;\n"
"    background: rgb(249, 127, 85);\n"
"    margin: 0 -4px; /* expand outside the groove */\n"
"}")
        self.Sail_Throttle_Slider.setOrientation(Qt.Vertical)

        self.gridLayout_22.addWidget(self.Sail_Throttle_Slider, 12, 2, 1, 1, Qt.AlignHCenter)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_22.addItem(self.verticalSpacer_7, 9, 1, 1, 1)

        self.label_5 = QLabel(self.frame_5)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font3)

        self.gridLayout_22.addWidget(self.label_5, 10, 2, 1, 1)

        self.verticalSpacer_14 = QSpacerItem(20, 15, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_22.addItem(self.verticalSpacer_14, 5, 1, 1, 1)

        self.Sail_Heading_LCD = QLCDNumber(self.frame_5)
        self.Sail_Heading_LCD.setObjectName(u"Sail_Heading_LCD")
        sizePolicy.setHeightForWidth(self.Sail_Heading_LCD.sizePolicy().hasHeightForWidth())
        self.Sail_Heading_LCD.setSizePolicy(sizePolicy)
        self.Sail_Heading_LCD.setMinimumSize(QSize(80, 40))
        self.Sail_Heading_LCD.setStyleSheet(u"QLCDNumber {\n"
"    border: 1px solid #f0f0f0;         /* Border color and width */\n"
"    border-radius: 4px;                /* Rounded corners */\n"
"    padding: 5px;                      /* Optional padding inside border */\n"
"    background-color: transparent;         /* Background color inside the border */\n"
"    color: #f0f0f0;                    /* Color for the LCD digits */\n"
"}\n"
"")
        self.Sail_Heading_LCD.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout_22.addWidget(self.Sail_Heading_LCD, 14, 1, 1, 1)

        self.verticalSpacer_12 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_22.addItem(self.verticalSpacer_12, 13, 1, 1, 1)

        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_22.addItem(self.horizontalSpacer_17, 12, 0, 1, 1)

        self.Enable_Sail_Button = QPushButton(self.frame_5)
        self.Enable_Sail_Button.setObjectName(u"Enable_Sail_Button")
        sizePolicy.setHeightForWidth(self.Enable_Sail_Button.sizePolicy().hasHeightForWidth())
        self.Enable_Sail_Button.setSizePolicy(sizePolicy)
        self.Enable_Sail_Button.setMinimumSize(QSize(70, 25))
        self.Enable_Sail_Button.setMaximumSize(QSize(70, 25))
        self.Enable_Sail_Button.setFont(font)
        self.Enable_Sail_Button.setStyleSheet(u"background-color: rgb(116, 116, 116);\n"
"color: rgb(240, 240, 240);\n"
"\n"
"")

        self.gridLayout_22.addWidget(self.Enable_Sail_Button, 7, 1, 1, 2, Qt.AlignHCenter|Qt.AlignVCenter)

        self.verticalSpacer_4 = QSpacerItem(20, 15, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_22.addItem(self.verticalSpacer_4, 11, 1, 1, 1)

        self.Sail_Heading_LCD.raise_()
        self.Sail_Throttle_Slider.raise_()
        self.Sail_Throttle_LCD.raise_()
        self.Sail_Label.raise_()
        self.Enable_Sail_Button.raise_()
        self.Sail_Status_Icon.raise_()
        self.Sail_Heading_Dial.raise_()
        self.line_4.raise_()
        self.label_4.raise_()
        self.label_5.raise_()

        self.gridLayout_19.addWidget(self.frame_5, 0, 0, 1, 1)


        self.gridLayout_5.addLayout(self.gridLayout_19, 0, 0, 1, 1)


        self.gridLayout_8.addLayout(self.gridLayout_5, 4, 7, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy4)
        self.frame.setMaximumSize(QSize(400, 16777215))
        self.frame.setStyleSheet(u"background-color: rgb(44, 44, 44);\n"
"color: rgb(240, 240, 240);")
        self.frame.setFrameShape(QFrame.Panel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setLineWidth(3)
        self.gridLayout_9 = QGridLayout(self.frame)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(-1, 30, -1, -1)
        self.Global_Speed_LCD = QLCDNumber(self.frame)
        self.Global_Speed_LCD.setObjectName(u"Global_Speed_LCD")
        sizePolicy3.setHeightForWidth(self.Global_Speed_LCD.sizePolicy().hasHeightForWidth())
        self.Global_Speed_LCD.setSizePolicy(sizePolicy3)
        self.Global_Speed_LCD.setMinimumSize(QSize(120, 60))
        self.Global_Speed_LCD.setMaximumSize(QSize(400, 200))
        font4 = QFont()
        font4.setPointSize(6)
        self.Global_Speed_LCD.setFont(font4)
        self.Global_Speed_LCD.setStyleSheet(u"QLCDNumber {\n"
"    border: 1px solid #f0f0f0;         /* Border color and width */\n"
"    border-radius: 4px;                /* Rounded corners */\n"
"    padding: 5px;                      /* Optional padding inside border */\n"
"    background-color: transparent;         /* Background color inside the border */\n"
"    color: #f0f0f0;                    /* Color for the LCD digits */\n"
"}\n"
"")
        self.Global_Speed_LCD.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout_9.addWidget(self.Global_Speed_LCD, 5, 1, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)

        self.verticalSpacer_11 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_9.addItem(self.verticalSpacer_11, 4, 1, 1, 1)

        self.Global_Speed_Label = QLabel(self.frame)
        self.Global_Speed_Label.setObjectName(u"Global_Speed_Label")
        sizePolicy4.setHeightForWidth(self.Global_Speed_Label.sizePolicy().hasHeightForWidth())
        self.Global_Speed_Label.setSizePolicy(sizePolicy4)
        self.Global_Speed_Label.setFont(font1)

        self.gridLayout_9.addWidget(self.Global_Speed_Label, 3, 1, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer_9, 5, 0, 1, 1)

        self.Global_Heading_Label = QLabel(self.frame)
        self.Global_Heading_Label.setObjectName(u"Global_Heading_Label")
        sizePolicy4.setHeightForWidth(self.Global_Heading_Label.sizePolicy().hasHeightForWidth())
        self.Global_Heading_Label.setSizePolicy(sizePolicy4)
        self.Global_Heading_Label.setFont(font1)

        self.gridLayout_9.addWidget(self.Global_Heading_Label, 3, 4, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer_10, 3, 5, 1, 1)

        self.verticalSpacer_8 = QSpacerItem(10, 100, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_9.addItem(self.verticalSpacer_8, 8, 4, 1, 1)

        self.Global_Heading_LCD = QLCDNumber(self.frame)
        self.Global_Heading_LCD.setObjectName(u"Global_Heading_LCD")
        sizePolicy3.setHeightForWidth(self.Global_Heading_LCD.sizePolicy().hasHeightForWidth())
        self.Global_Heading_LCD.setSizePolicy(sizePolicy3)
        self.Global_Heading_LCD.setMinimumSize(QSize(120, 60))
        self.Global_Heading_LCD.setMaximumSize(QSize(400, 200))
        self.Global_Heading_LCD.setStyleSheet(u"QLCDNumber {\n"
"    border: 1px solid #f0f0f0;         /* Border color and width */\n"
"    border-radius: 4px;                /* Rounded corners */\n"
"    padding: 5px;                      /* Optional padding inside border */\n"
"    background-color: transparent;         /* Background color inside the border */\n"
"    color: #f0f0f0;                    /* Color for the LCD digits */\n"
"}\n"
"")
        self.Global_Heading_LCD.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout_9.addWidget(self.Global_Heading_LCD, 5, 4, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer_16, 5, 2, 1, 1)


        self.gridLayout.addWidget(self.frame, 2, 0, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        sizePolicy3.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy3)
        self.label_2.setMaximumSize(QSize(400, 16777215))

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)


        self.gridLayout_8.addLayout(self.gridLayout, 2, 1, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(10, 10, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_7, 2, 2, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(10, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_8.addItem(self.verticalSpacer_6, 5, 6, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(10, 10, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_6, 2, 11, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(10, 15, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_8.addItem(self.verticalSpacer_5, 3, 7, 1, 1)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_15 = QGridLayout()
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.gridLayout_15.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy3.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy3)
        self.frame_3.setMinimumSize(QSize(390, 364))
        self.frame_3.setMaximumSize(QSize(400, 0))
        self.frame_3.setStyleSheet(u"background-color: rgb(44, 44, 44);\n"
"color: rgb(240, 240, 240);")
        self.frame_3.setFrameShape(QFrame.Panel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.frame_3.setLineWidth(3)
        self.gridLayout_16 = QGridLayout(self.frame_3)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.gridLayout_16.setHorizontalSpacing(6)
        self.gridLayout_16.setContentsMargins(-1, 20, -1, -1)
        self.S_Label = QLabel(self.frame_3)
        self.S_Label.setObjectName(u"S_Label")
        font5 = QFont()
        font5.setPointSize(14)
        self.S_Label.setFont(font5)
        self.S_Label.setAlignment(Qt.AlignCenter)

        self.gridLayout_16.addWidget(self.S_Label, 5, 1, 1, 1)

        self.Compass_Dial = QDial(self.frame_3)
        self.Compass_Dial.setObjectName(u"Compass_Dial")
        sizePolicy3.setHeightForWidth(self.Compass_Dial.sizePolicy().hasHeightForWidth())
        self.Compass_Dial.setSizePolicy(sizePolicy3)
        self.Compass_Dial.setMinimumSize(QSize(150, 150))
        self.Compass_Dial.setMaximumSize(QSize(160, 160))
        self.Compass_Dial.setStyleSheet(u"background-color: rgb(202, 202, 202);")
        self.Compass_Dial.setMaximum(360)
        self.Compass_Dial.setSliderPosition(180)
        self.Compass_Dial.setOrientation(Qt.Horizontal)
        self.Compass_Dial.setWrapping(True)
        self.Compass_Dial.setNotchesVisible(True)

        self.gridLayout_16.addWidget(self.Compass_Dial, 4, 1, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_16.addItem(self.verticalSpacer_3, 2, 1, 1, 1)

        self.verticalSpacer_10 = QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_16.addItem(self.verticalSpacer_10, 6, 1, 1, 1)

        self.Compass_Label = QLabel(self.frame_3)
        self.Compass_Label.setObjectName(u"Compass_Label")
        self.Compass_Label.setFont(font1)
        self.Compass_Label.setAlignment(Qt.AlignCenter)

        self.gridLayout_16.addWidget(self.Compass_Label, 0, 1, 1, 1)

        self.East_Label = QLabel(self.frame_3)
        self.East_Label.setObjectName(u"East_Label")
        self.East_Label.setFont(font5)

        self.gridLayout_16.addWidget(self.East_Label, 4, 2, 1, 1)

        self.North_Label = QLabel(self.frame_3)
        self.North_Label.setObjectName(u"North_Label")
        self.North_Label.setFont(font5)
        self.North_Label.setAlignment(Qt.AlignCenter)

        self.gridLayout_16.addWidget(self.North_Label, 3, 1, 1, 1)

        self.West_Label = QLabel(self.frame_3)
        self.West_Label.setObjectName(u"West_Label")
        self.West_Label.setFont(font5)
        self.West_Label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_16.addWidget(self.West_Label, 4, 0, 1, 1)

        self.line_2 = QFrame(self.frame_3)
        self.line_2.setObjectName(u"line_2")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.line_2.sizePolicy().hasHeightForWidth())
        self.line_2.setSizePolicy(sizePolicy5)
        self.line_2.setFrameShadow(QFrame.Raised)
        self.line_2.setLineWidth(3)
        self.line_2.setFrameShape(QFrame.HLine)

        self.gridLayout_16.addWidget(self.line_2, 1, 0, 1, 3)


        self.gridLayout_15.addWidget(self.frame_3, 0, 0, 1, 1, Qt.AlignLeft|Qt.AlignVCenter)


        self.gridLayout_2.addLayout(self.gridLayout_15, 0, 0, 1, 1)


        self.gridLayout_8.addLayout(self.gridLayout_2, 4, 1, 1, 3)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_2, 4, 6, 1, 1)

        self.horizontalSpacer_8 = QSpacerItem(10, 10, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_8, 2, 13, 1, 1)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_10 = QGridLayout()
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy4.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy4)
        self.frame_2.setMinimumSize(QSize(300, 300))
        self.frame_2.setMaximumSize(QSize(300, 16777215))
        self.frame_2.setStyleSheet(u"background-color: rgb(44, 44, 44);\n"
"color: rgb(240, 240, 240);")
        self.frame_2.setFrameShape(QFrame.Panel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.frame_2.setLineWidth(3)
        self.gridLayout_12 = QGridLayout(self.frame_2)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gridLayout_12.setContentsMargins(-1, 20, -1, -1)
        self.pushButton = QPushButton(self.frame_2)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy3.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy3)
        icon = QIcon()
        icon.addFile(u"../Grafisk/Gray Otter.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(260, 260))
        self.pushButton.setAutoDefault(False)
        self.pushButton.setFlat(True)

        self.gridLayout_12.addWidget(self.pushButton, 3, 1, 2, 3)

        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setEnabled(True)
        self.label.setTabletTracking(False)
        self.label.setAcceptDrops(False)
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet(u"QLabel {\n"
"    background-color: transparent;\n"
"}\n"
"")
        self.label.setTextFormat(Qt.AutoText)
        self.label.setScaledContents(False)
        self.label.setWordWrap(False)
        self.label.setOpenExternalLinks(False)

        self.gridLayout_12.addWidget(self.label, 1, 1, 1, 3)

        self.Gloabl_Throttle1_Label_2 = QLabel(self.frame_2)
        self.Gloabl_Throttle1_Label_2.setObjectName(u"Gloabl_Throttle1_Label_2")
        sizePolicy4.setHeightForWidth(self.Gloabl_Throttle1_Label_2.sizePolicy().hasHeightForWidth())
        self.Gloabl_Throttle1_Label_2.setSizePolicy(sizePolicy4)
        font6 = QFont()
        font6.setPointSize(10)
        font6.setBold(True)
        font6.setWeight(QFont.Weight.Bold)
        self.Gloabl_Throttle1_Label_2.setFont(font6)

        self.gridLayout_12.addWidget(self.Gloabl_Throttle1_Label_2, 5, 2, 1, 1, Qt.AlignHCenter)

        self.Global_Throttle2_Label = QLabel(self.frame_2)
        self.Global_Throttle2_Label.setObjectName(u"Global_Throttle2_Label")
        sizePolicy4.setHeightForWidth(self.Global_Throttle2_Label.sizePolicy().hasHeightForWidth())
        self.Global_Throttle2_Label.setSizePolicy(sizePolicy4)
        self.Global_Throttle2_Label.setFont(font)

        self.gridLayout_12.addWidget(self.Global_Throttle2_Label, 7, 3, 1, 1)

        self.horizontalSpacer_14 = QSpacerItem(200, 200, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout_12.addItem(self.horizontalSpacer_14, 6, 4, 1, 1)

        self.verticalSpacer_17 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_12.addItem(self.verticalSpacer_17, 2, 1, 1, 1)

        self.Global_Throttle1_Status_2 = QProgressBar(self.frame_2)
        self.Global_Throttle1_Status_2.setObjectName(u"Global_Throttle1_Status_2")
        self.Global_Throttle1_Status_2.setMinimumSize(QSize(30, 0))
        font7 = QFont()
        font7.setPointSize(8)
        font7.setBold(False)
        font7.setWeight(QFont.Weight.Normal)
        self.Global_Throttle1_Status_2.setFont(font7)
        self.Global_Throttle1_Status_2.setStyleSheet(u"QProgressBar {\n"
"    color: black;                      /* Text color */\n"
"    border: 2px solid #2c2c2c;         /* Border color */\n"
"    border-radius: 4px;                /* Rounded corners */\n"
"    text-align: center;                /* Center align the text */\n"
"    background-color: #f0f0f0;         /* Background color for unfilled portion */\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: #f97f55;         /* Chunk (progress) color */\n"
"    /*border-radius: 4px;                /* Match rounding of progress bar */\n"
"}\n"
"")
        self.Global_Throttle1_Status_2.setMaximum(2000)
        self.Global_Throttle1_Status_2.setValue(500)
        self.Global_Throttle1_Status_2.setOrientation(Qt.Vertical)
        self.Global_Throttle1_Status_2.setInvertedAppearance(False)
        self.Global_Throttle1_Status_2.setTextDirection(QProgressBar.TopToBottom)

        self.gridLayout_12.addWidget(self.Global_Throttle1_Status_2, 6, 1, 1, 1)

        self.horizontalSpacer_13 = QSpacerItem(200, 200, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout_12.addItem(self.horizontalSpacer_13, 6, 0, 1, 1)

        self.Gloabl_Throttle1_Label = QLabel(self.frame_2)
        self.Gloabl_Throttle1_Label.setObjectName(u"Gloabl_Throttle1_Label")
        sizePolicy4.setHeightForWidth(self.Gloabl_Throttle1_Label.sizePolicy().hasHeightForWidth())
        self.Gloabl_Throttle1_Label.setSizePolicy(sizePolicy4)
        self.Gloabl_Throttle1_Label.setFont(font)

        self.gridLayout_12.addWidget(self.Gloabl_Throttle1_Label, 7, 1, 1, 1)

        self.Global_Throttle2_Status_2 = QProgressBar(self.frame_2)
        self.Global_Throttle2_Status_2.setObjectName(u"Global_Throttle2_Status_2")
        self.Global_Throttle2_Status_2.setMinimumSize(QSize(30, 0))
        self.Global_Throttle2_Status_2.setFont(font3)
        self.Global_Throttle2_Status_2.setStyleSheet(u"QProgressBar {\n"
"    color: black;                      /* Text color */\n"
"    border: 2px solid #2c2c2c;         /* Border color */\n"
"    border-radius: 4px;                /* Rounded corners */\n"
"    text-align: center;                /* Center align the text */\n"
"    background-color: #f0f0f0;         /* Background color for unfilled portion */\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: #f97f55;         /* Chunk (progress) color */\n"
"    /*border-radius: 4px;                /* Match rounding of progress bar */\n"
"}\n"
"")
        self.Global_Throttle2_Status_2.setMaximum(2000)
        self.Global_Throttle2_Status_2.setValue(1500)
        self.Global_Throttle2_Status_2.setTextVisible(True)
        self.Global_Throttle2_Status_2.setOrientation(Qt.Vertical)
        self.Global_Throttle2_Status_2.setInvertedAppearance(False)
        self.Global_Throttle2_Status_2.setTextDirection(QProgressBar.TopToBottom)

        self.gridLayout_12.addWidget(self.Global_Throttle2_Status_2, 6, 3, 1, 1)


        self.gridLayout_10.addWidget(self.frame_2, 1, 0, 1, 1, Qt.AlignHCenter)

        self.verticalFrame = QFrame(self.centralwidget)
        self.verticalFrame.setObjectName(u"verticalFrame")
        self.verticalFrame.setStyleSheet(u"background-color: rgb(44, 44, 44);\n"
"color: rgb(240, 240, 240);")
        self.verticalLayout_2 = QVBoxLayout(self.verticalFrame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")

        self.gridLayout_10.addWidget(self.verticalFrame, 0, 0, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_10, 0, 0, 1, 1)


        self.gridLayout_8.addLayout(self.gridLayout_3, 2, 12, 1, 1)

        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.MapPlaceHolder = QGraphicsView(self.centralwidget)
        self.MapPlaceHolder.setObjectName(u"MapPlaceHolder")
        sizePolicy3.setHeightForWidth(self.MapPlaceHolder.sizePolicy().hasHeightForWidth())
        self.MapPlaceHolder.setSizePolicy(sizePolicy3)
        self.MapPlaceHolder.setMinimumSize(QSize(500, 400))
        self.MapPlaceHolder.setStyleSheet(u"background-color: rgb(44, 44, 44);\n"
"")

        self.gridLayout_7.addWidget(self.MapPlaceHolder, 0, 0, 1, 1)


        self.gridLayout_8.addLayout(self.gridLayout_7, 2, 3, 1, 8)

        self.gridFrame = QFrame(self.centralwidget)
        self.gridFrame.setObjectName(u"gridFrame")
        self.gridFrame.setMinimumSize(QSize(0, 20))
        self.gridFrame.setMaximumSize(QSize(16777215, 20))
        font8 = QFont()
        font8.setKerning(True)
        self.gridFrame.setFont(font8)
        self.gridFrame.setStyleSheet(u"background-color: rgb(204, 204, 204);")
        self.gridFrame.setLineWidth(0)
        self.gridLayout_11 = QGridLayout(self.gridFrame)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setContentsMargins(1, 0, 1, 0)
        self.label_3 = QLabel(self.gridFrame)
        self.label_3.setObjectName(u"label_3")
        font9 = QFont()
        font9.setFamily(u"Consolas")
        font9.setPointSize(10)
        font9.setBold(True)
        font9.setWeight(QFont.Weight.Bold)
        self.label_3.setFont(font9)

        self.gridLayout_11.addWidget(self.label_3, 0, 1, 1, 1)

        self.horizontalSpacer_12 = QSpacerItem(4, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_11.addItem(self.horizontalSpacer_12, 0, 4, 1, 1)

        self.Exit_Button = QPushButton(self.gridFrame)
        self.Exit_Button.setObjectName(u"Exit_Button")
        sizePolicy.setHeightForWidth(self.Exit_Button.sizePolicy().hasHeightForWidth())
        self.Exit_Button.setSizePolicy(sizePolicy)
        self.Exit_Button.setMinimumSize(QSize(42, 10))
        self.Exit_Button.setMaximumSize(QSize(40, 14))
        font10 = QFont()
        font10.setFamily(u"MT Extra")
        font10.setBold(True)
        font10.setWeight(QFont.Weight.Bold)
        self.Exit_Button.setFont(font10)
        self.Exit_Button.setStyleSheet(u"/* Default style for the exit button with gradient background */\n"
"QPushButton {\n"
"    background-color: qlineargradient(\n"
"        spread:pad, \n"
"        x1:0, y1:0, x2:0, y2:1, \n"
"        stop:0 #FF4D4D,        /* Lighter red at the top */\n"
"        stop:1 #8B0000         /* Darker red at the bottom */\n"
"    );\n"
"    color: white;                       /* White text color for 'X' */ \n"
"	border: 1px solid #2c2c2c;\n"
"    border-radius: 2px;                 /* Optional: rounded corners */\n"
"    font-size: 10px;                    /* Font size for 'X' */\n"
"    font-weight: bold;                  /* Bold 'X' */\n"
"    min-width: 40px;                    /* Minimum width */\n"
"    min-height: 8px;                   /* Minimum height */\n"
"}\n"
"\n"
"/* Hover effect: Lighter gradient */\n"
"QPushButton:hover {\n"
"    background-color: qlineargradient(\n"
"        spread:pad, \n"
"        x1:0, y1:0, x2:0, y2:1, \n"
"        stop:0 #FF6666,        /* Even lighter red at the top */\n"
"   "
                        "     stop:1 #B22222         /* Darker red at the bottom */\n"
"    );\n"
"}\n"
"\n"
"/* Pressed effect: Slightly darker gradient */\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(\n"
"        spread:pad, \n"
"        x1:0, y1:0, x2:0, y2:1, \n"
"        stop:0 #B22222,        /* Darker shade at the top */\n"
"        stop:1 #8B0000         /* Darkest shade at the bottom */\n"
"    );\n"
"    padding-top: 4px;                   /* Move content down to simulate press */\n"
"    padding-bottom: 2px;\n"
"}\n"
"")

        self.gridLayout_11.addWidget(self.Exit_Button, 0, 3, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_11.addItem(self.horizontalSpacer_11, 0, 0, 1, 1)

        self.horizontalSpacer_15 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_11.addItem(self.horizontalSpacer_15, 0, 2, 1, 1)


        self.gridLayout_8.addWidget(self.gridFrame, 0, 1, 1, 12)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setMinimumSize(QSize(0, 2))
        self.line.setStyleSheet(u"color: rgb(44, 44, 44);")
        self.line.setFrameShadow(QFrame.Raised)
        self.line.setLineWidth(2)
        self.line.setFrameShape(QFrame.HLine)

        self.gridLayout_8.addWidget(self.line, 1, 1, 1, 12)

        self.horizontalSpacer = QSpacerItem(80, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer, 4, 4, 1, 1)

        self.gridLayout_8.setColumnStretch(7, 5)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 2016, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.pushButton.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Waypoints_Label.setText(QCoreApplication.translate("MainWindow", u"Waypoints", None))
        self.Track_Load_Button.setText(QCoreApplication.translate("MainWindow", u"Load", None))
        self.Track_Label.setText(QCoreApplication.translate("MainWindow", u"TRACK", None))
        self.Enable_Track_Button.setText(QCoreApplication.translate("MainWindow", u"Enable", None))
        self.Clear_Waypoint_Button.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.Enable_Standby_Button.setText(QCoreApplication.translate("MainWindow", u"Enable", None))
        self.Standby_Label.setText(QCoreApplication.translate("MainWindow", u"STANDBY", None))
        self.Enable_Dp_Button.setText(QCoreApplication.translate("MainWindow", u"Enable", None))
        self.Dp_Label.setText(QCoreApplication.translate("MainWindow", u"POSITION", None))
        self.Dp_Load_Button.setText(QCoreApplication.translate("MainWindow", u"Load", None))
        self.Deviation_Dp_Label.setText(QCoreApplication.translate("MainWindow", u"DEVIATION", None))
        self.Sail_Label.setText(QCoreApplication.translate("MainWindow", u"SAIL", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"              Turn", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"                       Knots", None))
        self.Enable_Sail_Button.setText(QCoreApplication.translate("MainWindow", u"Enable", None))
        self.Global_Speed_Label.setText(QCoreApplication.translate("MainWindow", u"Speed", None))
        self.Global_Heading_Label.setText(QCoreApplication.translate("MainWindow", u"Heading", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:48pt; font-weight:600; color:#3fb184;\">HMI</span></p><p align=\"center\"><span style=\" font-size:18pt; color:#ffffff;\">OTTER</span></p><p align=\"center\"><br/></p><p align=\"center\"><span style=\" font-size:12pt; color:#ffffff;\">GRUPPE 5</span></p></body></html>", None))
        self.S_Label.setText(QCoreApplication.translate("MainWindow", u"S", None))
        self.Compass_Label.setText(QCoreApplication.translate("MainWindow", u"COMPAS", None))
        self.East_Label.setText(QCoreApplication.translate("MainWindow", u"E", None))
        self.North_Label.setText(QCoreApplication.translate("MainWindow", u"N", None))
        self.West_Label.setText(QCoreApplication.translate("MainWindow", u"W", None))
        self.pushButton.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600; color:#3fb184;\">Thrusters</span></p></body></html>", None))
        self.Gloabl_Throttle1_Label_2.setText(QCoreApplication.translate("MainWindow", u"RPM", None))
        self.Global_Throttle2_Label.setText(QCoreApplication.translate("MainWindow", u"R", None))
        self.Global_Throttle1_Status_2.setFormat(QCoreApplication.translate("MainWindow", u"%p%", None))
        self.Gloabl_Throttle1_Label.setText(QCoreApplication.translate("MainWindow", u"L", None))
        self.Global_Throttle2_Status_2.setFormat(QCoreApplication.translate("MainWindow", u"%p%", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.Exit_Button.setText(QCoreApplication.translate("MainWindow", u"X", None))
    # retranslateUi
