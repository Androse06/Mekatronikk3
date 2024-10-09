# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DesignerDemoRxGmSA.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenuBar,
    QSizePolicy, QSlider, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1065, 673)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.HorisontalSlider1 = QSlider(self.centralwidget)
        self.HorisontalSlider1.setObjectName(u"HorisontalSlider1")
        self.HorisontalSlider1.setGeometry(QRect(390, 530, 160, 22))
        self.HorisontalSlider1.setMaximum(100)
        self.HorisontalSlider1.setOrientation(Qt.Horizontal)
        self.VerticalSlider1 = QSlider(self.centralwidget)
        self.VerticalSlider1.setObjectName(u"VerticalSlider1")
        self.VerticalSlider1.setGeometry(QRect(70, 310, 22, 160))
        self.VerticalSlider1.setMaximum(50)
        self.VerticalSlider1.setOrientation(Qt.Vertical)
        self.VerticalSlider2 = QSlider(self.centralwidget)
        self.VerticalSlider2.setObjectName(u"VerticalSlider2")
        self.VerticalSlider2.setGeometry(QRect(150, 310, 22, 160))
        self.VerticalSlider2.setMaximum(50)
        self.VerticalSlider2.setOrientation(Qt.Vertical)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(170, 430, 49, 16))
        self.VerticalSlideLabel2 = QLabel(self.centralwidget)
        self.VerticalSlideLabel2.setObjectName(u"VerticalSlideLabel2")
        self.VerticalSlideLabel2.setGeometry(QRect(140, 480, 49, 16))
        self.HorisontalLabel1 = QLabel(self.centralwidget)
        self.HorisontalLabel1.setObjectName(u"HorisontalLabel1")
        self.HorisontalLabel1.setGeometry(QRect(410, 570, 49, 16))
        self.VerticalSliderLabel1 = QLabel(self.centralwidget)
        self.VerticalSliderLabel1.setObjectName(u"VerticalSliderLabel1")
        self.VerticalSliderLabel1.setGeometry(QRect(60, 490, 49, 16))
        self.mapPlaceholder = QWidget(self.centralwidget)
        self.mapPlaceholder.setObjectName(u"mapPlaceholder")
        self.mapPlaceholder.setGeometry(QRect(330, 140, 361, 281))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1065, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.VerticalSlideLabel2.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.HorisontalLabel1.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.VerticalSliderLabel1.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
    # retranslateUi

