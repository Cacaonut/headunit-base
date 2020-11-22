import os
import time

import ui.res.resources
import subprocess
import ui.android_auto as android_auto
import ui.car as car
import ui.devices as devices
import ui.home as home
import ui.media as media
import ui.settings as settings
from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import datetime
import threading
from sys import platform


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Headunit")
        MainWindow.setEnabled(True)
        MainWindow.resize(800, 480)
        if platform == "linux" or platform == "linux2":
            MainWindow.showFullScreen()
            MainWindow.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("#centralwidget {background: #000}\n"
                                         "* {color: white}")
        self.centralwidget.setObjectName("centralwidget")
        self.top_bar = QtWidgets.QWidget(self.centralwidget)
        self.top_bar.setGeometry(QtCore.QRect(0, 0, 800, 45))
        self.top_bar.setStyleSheet("#top_bar {\n"
                                   "    background: #252525; border-bottom: 1px solid white\n"
                                   "}")
        self.top_bar.setObjectName("top_bar")
        self.label_title = QtWidgets.QLabel(self.top_bar)
        self.label_title.setGeometry(QtCore.QRect(260, 7, 200, 30))
        font = QtGui.QFont()
        font.setFamily("Montserrat Light")
        font.setPointSize(16)
        self.label_title.setFont(font)
        self.label_title.setAutoFillBackground(False)
        self.label_title.setStyleSheet("")
        self.label_title.setScaledContents(False)
        self.label_title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_title.setObjectName("label_title")
        self.label_clock = QtWidgets.QLabel(self.top_bar)
        self.label_clock.setGeometry(QtCore.QRect(10, 7, 80, 30))
        font = QtGui.QFont()
        font.setFamily("Montserrat Light")
        font.setPointSize(16)
        self.label_clock.setFont(font)
        self.label_clock.setAutoFillBackground(False)
        self.label_clock.setStyleSheet("")
        self.label_clock.setScaledContents(False)
        self.label_clock.setAlignment(QtCore.Qt.AlignCenter)
        self.label_clock.setObjectName("label_clock")
        self.label = QtWidgets.QLabel(self.top_bar)
        self.label.setGeometry(QtCore.QRect(735, 8, 50, 29))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/images/toyota.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_temperature = QtWidgets.QLabel(self.top_bar)
        self.label_temperature.setGeometry(QtCore.QRect(625, 7, 80, 30))
        font = QtGui.QFont()
        font.setFamily("Montserrat Light")
        font.setPointSize(16)
        self.label_temperature.setFont(font)
        self.label_temperature.setAutoFillBackground(False)
        self.label_temperature.setStyleSheet("")
        self.label_temperature.setScaledContents(False)
        self.label_temperature.setAlignment(QtCore.Qt.AlignCenter)
        self.label_temperature.setObjectName("label_temperature")
        self.btn_media = QtWidgets.QWidget(self.centralwidget)
        self.btn_media.setGeometry(QtCore.QRect(720, 118, 80, 70))
        self.btn_media.setStyleSheet("#btn_media {\n"
                                     "    background: #252525; color: white\n"
                                     "}\n"
                                     "\n"
                                     "#btn_media::hover {\n"
                                     "    background: #303030;\n"
                                     "}\n"
                                     "\n"
                                     "#btn_media::!enabled {\n"
                                     "    background: #595959;\n"
                                     "    border-bottom: 3px solid #E00000;\n"
                                     "}")
        self.btn_media.setObjectName("btn_media")
        self.text_btn_media = QtWidgets.QLabel(self.btn_media)
        self.text_btn_media.setGeometry(QtCore.QRect(10, 47, 60, 15))
        font = QtGui.QFont()
        font.setFamily("Montserrat Light")
        font.setPointSize(11)
        self.text_btn_media.setFont(font)
        self.text_btn_media.setLineWidth(1)
        self.text_btn_media.setAlignment(QtCore.Qt.AlignCenter)
        self.text_btn_media.setObjectName("text_btn_media")
        self.image_btn_media = QtWidgets.QLabel(self.btn_media)
        self.image_btn_media.setGeometry(QtCore.QRect(20, 3, 40, 40))
        self.image_btn_media.setText("")
        self.image_btn_media.setPixmap(QtGui.QPixmap(":/images/media.svg"))
        self.image_btn_media.setScaledContents(True)
        self.image_btn_media.setObjectName("image_btn_media")
        self.btn_home = QtWidgets.QWidget(self.centralwidget)
        self.btn_home.setEnabled(False)
        self.btn_home.setGeometry(QtCore.QRect(720, 45, 80, 70))
        self.btn_home.setStyleSheet("#btn_home {\n"
                                    "    background: #252525; color: white\n"
                                    "}\n"
                                    "\n"
                                    "#btn_home::hover {\n"
                                    "    background: #303030;\n"
                                    "}\n"
                                    "\n"
                                    "#btn_home::!enabled {\n"
                                    "    background: #595959;\n"
                                    "    border-bottom: 3px solid #E00000;\n"
                                    "}")
        self.btn_home.setObjectName("btn_home")
        self.text_btn_home = QtWidgets.QLabel(self.btn_home)
        self.text_btn_home.setGeometry(QtCore.QRect(10, 47, 60, 15))
        font = QtGui.QFont()
        font.setFamily("Montserrat Light")
        font.setPointSize(11)
        self.text_btn_home.setFont(font)
        self.text_btn_home.setLineWidth(1)
        self.text_btn_home.setAlignment(QtCore.Qt.AlignCenter)
        self.text_btn_home.setObjectName("text_btn_home")
        self.image_btn_home = QtWidgets.QLabel(self.btn_home)
        self.image_btn_home.setGeometry(QtCore.QRect(20, 3, 40, 40))
        self.image_btn_home.setText("")
        self.image_btn_home.setPixmap(QtGui.QPixmap(":/images/home.svg"))
        self.image_btn_home.setScaledContents(True)
        self.image_btn_home.setObjectName("image_btn_home")
        self.btn_car = QtWidgets.QWidget(self.centralwidget)
        self.btn_car.setGeometry(QtCore.QRect(720, 191, 80, 70))
        self.btn_car.setStyleSheet("#btn_car {\n"
                                   "    background: #252525; color: white\n"
                                   "}\n"
                                   "\n"
                                   "#btn_car::hover {\n"
                                   "    background: #303030;\n"
                                   "}\n"
                                   "\n"
                                   "#btn_car::!enabled {\n"
                                   "    background: #595959;\n"
                                   "    border-bottom: 3px solid #E00000;\n"
                                   "}")
        self.btn_car.setObjectName("btn_car")
        self.text_btn_car = QtWidgets.QLabel(self.btn_car)
        self.text_btn_car.setGeometry(QtCore.QRect(10, 47, 60, 15))
        font = QtGui.QFont()
        font.setFamily("Montserrat Light")
        font.setPointSize(11)
        self.text_btn_car.setFont(font)
        self.text_btn_car.setLineWidth(1)
        self.text_btn_car.setAlignment(QtCore.Qt.AlignCenter)
        self.text_btn_car.setObjectName("text_btn_car")
        self.image_btn_car = QtWidgets.QLabel(self.btn_car)
        self.image_btn_car.setGeometry(QtCore.QRect(20, 3, 40, 40))
        self.image_btn_car.setText("")
        self.image_btn_car.setPixmap(QtGui.QPixmap(":/images/car.svg"))
        self.image_btn_car.setScaledContents(True)
        self.image_btn_car.setObjectName("image_btn_car")
        self.btn_devices = QtWidgets.QWidget(self.centralwidget)
        self.btn_devices.setGeometry(QtCore.QRect(720, 264, 80, 70))
        self.btn_devices.setStyleSheet("#btn_devices {\n"
                                       "    background: #252525; color: white\n"
                                       "}\n"
                                       "\n"
                                       "#btn_devices::hover {\n"
                                       "    background: #303030;\n"
                                       "}\n"
                                       "\n"
                                       "#btn_devices::!enabled {\n"
                                       "    background: #595959;\n"
                                       "    border-bottom: 3px solid #E00000;\n"
                                       "}")
        self.btn_devices.setObjectName("btn_devices")
        self.text_btn_devices = QtWidgets.QLabel(self.btn_devices)
        self.text_btn_devices.setGeometry(QtCore.QRect(10, 47, 60, 15))
        font = QtGui.QFont()
        font.setFamily("Montserrat Light")
        font.setPointSize(11)
        self.text_btn_devices.setFont(font)
        self.text_btn_devices.setLineWidth(1)
        self.text_btn_devices.setAlignment(QtCore.Qt.AlignCenter)
        self.text_btn_devices.setObjectName("text_btn_devices")
        self.image_btn_devices = QtWidgets.QLabel(self.btn_devices)
        self.image_btn_devices.setGeometry(QtCore.QRect(20, 3, 40, 40))
        self.image_btn_devices.setText("")
        self.image_btn_devices.setPixmap(QtGui.QPixmap(":/images/devices.svg"))
        self.image_btn_devices.setScaledContents(True)
        self.image_btn_devices.setObjectName("image_btn_devices")
        self.btn_android_auto = QtWidgets.QWidget(self.centralwidget)
        self.btn_android_auto.setGeometry(QtCore.QRect(720, 337, 80, 70))
        self.btn_android_auto.setStyleSheet("#btn_android_auto {\n"
                                            "    background: #252525; color: white\n"
                                            "}\n"
                                            "\n"
                                            "#btn_android_auto::hover {\n"
                                            "    background: #303030;\n"
                                            "}\n"
                                            "\n"
                                            "#btn_android_auto::!enabled {\n"
                                            "    background: #595959;\n"
                                            "    border-bottom: 3px solid #E00000;\n"
                                            "}")
        self.btn_android_auto.setObjectName("btn_android_auto")
        self.text_btn_android_auto = QtWidgets.QLabel(self.btn_android_auto)
        self.text_btn_android_auto.setGeometry(QtCore.QRect(10, 30, 60, 30))
        font = QtGui.QFont()
        font.setFamily("Montserrat Light")
        font.setPointSize(11)
        self.text_btn_android_auto.setFont(font)
        self.text_btn_android_auto.setStyleSheet("")
        self.text_btn_android_auto.setLineWidth(1)
        self.text_btn_android_auto.setTextFormat(QtCore.Qt.AutoText)
        self.text_btn_android_auto.setAlignment(QtCore.Qt.AlignCenter)
        self.text_btn_android_auto.setWordWrap(False)
        self.text_btn_android_auto.setObjectName("text_btn_android_auto")
        self.text2_btn_android_auto = QtWidgets.QLabel(self.btn_android_auto)
        self.text2_btn_android_auto.setGeometry(QtCore.QRect(10, 43, 60, 30))
        self.text2_btn_android_auto.setFont(font)
        self.text2_btn_android_auto.setStyleSheet("")
        self.text2_btn_android_auto.setLineWidth(1)
        self.text2_btn_android_auto.setTextFormat(QtCore.Qt.AutoText)
        self.text2_btn_android_auto.setAlignment(QtCore.Qt.AlignCenter)
        self.text2_btn_android_auto.setWordWrap(False)
        self.text2_btn_android_auto.setObjectName("text2_btn_android_auto")
        self.image_btn_android_auto = QtWidgets.QLabel(self.btn_android_auto)
        self.image_btn_android_auto.setGeometry(QtCore.QRect(23, 3, 34, 34))
        self.image_btn_android_auto.setText("")
        self.image_btn_android_auto.setPixmap(QtGui.QPixmap(":/images/android_auto.png"))
        self.image_btn_android_auto.setScaledContents(True)
        self.image_btn_android_auto.setObjectName("image_btn_android_auto")
        self.btn_settings = QtWidgets.QWidget(self.centralwidget)
        self.btn_settings.setGeometry(QtCore.QRect(720, 410, 80, 70))
        self.btn_settings.setStyleSheet("#btn_settings {\n"
                                        "    background: #252525; color: white\n"
                                        "}\n"
                                        "\n"
                                        "#btn_settings::hover {\n"
                                        "    background: #303030;\n"
                                        "}\n"
                                        "\n"
                                        "#btn_settings::!enabled {\n"
                                        "    background: #595959;\n"
                                        "    border-bottom: 3px solid #E00000;\n"
                                        "}")
        self.btn_settings.setObjectName("btn_settings")
        self.text_btn_settings = QtWidgets.QLabel(self.btn_settings)
        self.text_btn_settings.setGeometry(QtCore.QRect(10, 47, 60, 20))
        font = QtGui.QFont()
        font.setFamily("Avenir Next LT Pro")
        font.setPointSize(11)
        self.text_btn_settings.setFont(font)
        self.text_btn_settings.setLineWidth(1)
        self.text_btn_settings.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.text_btn_settings.setObjectName("text_btn_settings")
        self.image_btn_settings = QtWidgets.QLabel(self.btn_settings)
        self.image_btn_settings.setGeometry(QtCore.QRect(20, 3, 40, 40))
        self.image_btn_settings.setText("")
        self.image_btn_settings.setPixmap(QtGui.QPixmap(":/images/settings.svg"))
        self.image_btn_settings.setScaledContents(True)
        self.image_btn_settings.setObjectName("image_btn_settings")
        self.content = QtWidgets.QStackedWidget(self.centralwidget)
        self.content.setGeometry(QtCore.QRect(0, 45, 720, 435))
        self.content.setObjectName("content")
        self.current_tab = self.btn_home

        # Home
        content_home = QtWidgets.QWidget()
        ui_home = home.Ui_content()
        ui_home.setupUi(content_home)
        self.content.addWidget(content_home)

        # Media
        content_media = QtWidgets.QWidget()
        ui_media = media.Ui_content()
        ui_media.setupUi(content_media)
        self.content.addWidget(content_media)

        # Car
        content_car = QtWidgets.QWidget()
        ui_car = car.Ui_content()
        ui_car.setupUi(content_car)
        self.content.addWidget(content_car)

        # Devices
        content_devices = QtWidgets.QWidget()
        ui_devices = devices.Ui_content()
        ui_devices.setupUi(content_devices)
        self.content.addWidget(content_devices)

        # Android Auto
        if platform == "linux" or platform == "linux2":
            subprocess.Popen(["sudo", "/home/pi/openauto/bin/autoapp"])
            time.sleep(3)
            self.content_android_auto = QtWidgets.QWidget()
            ui_android_auto = android_auto.Ui_content()
            ui_android_auto.setupUi(self.content_android_auto, self)
            self.content.addWidget(self.content_android_auto)
            self.current_aa_wid = 0
            self.running = False


        # Settings
        content_settings = QtWidgets.QWidget()
        ui_settings = settings.Ui_content()
        ui_settings.setupUi(content_settings)
        self.content.addWidget(content_settings)

        # Set button actions
        self.btn_home.mouseReleaseEvent = self.switchToHome
        self.btn_media.mouseReleaseEvent = self.switchToMedia
        self.btn_car.mouseReleaseEvent = self.switchToCar
        self.btn_devices.mouseReleaseEvent = self.switchToDevices
        self.btn_android_auto.mouseReleaseEvent = self.switchToAndroidAuto
        self.btn_settings.mouseReleaseEvent = self.switchToSettings

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        self.updateTime()
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Headunit"))
        self.label_title.setText(_translate("MainWindow", "HOME"))
        self.label_temperature.setText(_translate("MainWindow", "21 °C"))
        self.text_btn_media.setText(_translate("MainWindow", "Media"))
        self.text_btn_home.setText(_translate("MainWindow", "Home"))
        self.text_btn_car.setText(_translate("MainWindow", "Car"))
        self.text_btn_devices.setText(_translate("MainWindow", "Devices"))
        self.text_btn_android_auto.setText(_translate("MainWindow", "Android"))
        self.text2_btn_android_auto.setText(_translate("MainWindow", "Auto"))
        self.text_btn_settings.setText(_translate("MainWindow", "Settings"))

    def switchToHome(self, event):
        self.content.setCurrentIndex(0)
        self.btn_home.setEnabled(False)
        self.current_tab.setEnabled(True)
        self.label_title.setText("HOME")
        self.current_tab = self.btn_home

    def switchToMedia(self, event):
        self.content.setCurrentIndex(1)
        self.btn_media.setEnabled(False)
        self.current_tab.setEnabled(True)
        self.label_title.setText("MEDIA")
        self.current_tab = self.btn_media

    def switchToCar(self, event):
        self.content.setCurrentIndex(2)
        self.btn_car.setEnabled(False)
        self.current_tab.setEnabled(True)
        self.label_title.setText("CAR")
        self.current_tab = self.btn_car

    def switchToDevices(self, event):
        self.content.setCurrentIndex(3)
        self.btn_devices.setEnabled(False)
        self.current_tab.setEnabled(True)
        self.label_title.setText("DEVICES")
        self.current_tab = self.btn_devices

    def switchToAndroidAuto(self, event):
        self.content.setCurrentIndex(4)
        self.btn_android_auto.setEnabled(False)
        self.current_tab.setEnabled(True)
        self.label_title.setText("ANDROID AUTO")
        self.bindAndroidAuto()
        self.current_tab = self.btn_android_auto

    def switchToSettings(self, event):
        self.content.setCurrentIndex(5)
        self.btn_settings.setEnabled(False)
        self.current_tab.setEnabled(True)
        self.label_title.setText("SETTINGS")
        self.current_tab = self.btn_settings

    def updateTime(self):
        now = datetime.now()
        current_time = now.strftime("%H:%M")
        self.label_clock.setText(current_time)
        threading.Timer(0.5, self.updateTime).start()

    def bindAndroidAuto(self):
        windows = subprocess.check_output(["wmctrl", "-l"]).decode("UTF-8").split("\n")
        for window in windows:
            if window.find("autoapp") > -1:
                self.running = True
                window_id = window.split(" ")[0]
                print(int(window_id, 0))
                if int(window_id, 0) != self.current_aa_wid:
                    self.current_aa_wid = int(window_id, 0)
                    window_android_auto = QtGui.QWindow.fromWinId(int(window_id, 0))
                    window_android_auto.setFlag(QtCore.Qt.FramelessWindowHint)
                    content_android_auto = QtWidgets.QWidget.createWindowContainer(window_android_auto)
                    self.content.removeWidget(self.content_android_auto)
                    self.content.insertWidget(4, content_android_auto)
                    self.content_android_auto = content_android_auto

        if not self.running:
            self.content_android_auto = QtWidgets.QWidget()
            ui_android_auto = android_auto.Ui_content()
            ui_android_auto.setupUi(self.content_android_auto, self)
            self.content.removeWidget(self.content_android_auto)
            self.content.insertWidget(4, self.content_android_auto)
