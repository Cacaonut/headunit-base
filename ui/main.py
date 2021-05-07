import subprocess
import threading
from datetime import datetime
from sys import platform
import serial
import uinput
import time
import os
import obd

from PyQt5 import QtCore, QtGui, QtWidgets

import ui.res.resources
import ui.car as car
import ui.devices as devices
import ui.home as home
import ui.media as media
import ui.settings as settings
from ui import radio


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Headunit")
        MainWindow.setEnabled(True)
        MainWindow.resize(800, 480)
        if platform == "linux" or platform == "linux2":
            MainWindow.showFullScreen()
            #MainWindow.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
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
        self.label = QtWidgets.QLabel(self.top_bar)
        self.label.setGeometry(QtCore.QRect(735, 8, 50, 29))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/images/toyota.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_temperature = QtWidgets.QLabel(self.top_bar)
        self.label_temperature.setGeometry(QtCore.QRect(10, 7, 80, 30))
        font = QtGui.QFont()
        font.setFamily("Montserrat Light")
        font.setPointSize(16)
        self.label_temperature.setFont(font)
        self.label_temperature.setAutoFillBackground(False)
        self.label_temperature.setStyleSheet("")
        self.label_temperature.setScaledContents(False)
        self.label_temperature.setAlignment(QtCore.Qt.AlignCenter)
        self.label_temperature.setObjectName("label_temperature")
        self.label_volume_up = QtWidgets.QLabel(self.top_bar)
        self.label_volume_up.setGeometry(QtCore.QRect(670, 7, 30, 30))
        self.label_volume_up.setText("")
        self.label_volume_up.setPixmap(QtGui.QPixmap(":/images/plus.svg"))
        self.label_volume_up.setScaledContents(True)
        self.label_volume_up.setObjectName("label_volume_up")
        self.label_volume_down = QtWidgets.QLabel(self.top_bar)
        self.label_volume_down.setGeometry(QtCore.QRect(590, 7, 30, 30))
        self.label_volume_down.setText("")
        self.label_volume_down.setPixmap(QtGui.QPixmap(":/images/minus.svg"))
        self.label_volume_down.setScaledContents(True)
        self.label_volume_down.setObjectName("label_volume_down")
        self.label_volume = QtWidgets.QLabel(self.top_bar)
        self.label_volume.setGeometry(QtCore.QRect(610, 7, 70, 30))
        font = QtGui.QFont()
        font.setFamily("Montserrat Light")
        font.setPointSize(16)
        self.label_volume.setFont(font)
        self.label_volume.setAutoFillBackground(False)
        self.label_volume.setStyleSheet("")
        self.label_volume.setScaledContents(False)
        self.label_volume.setAlignment(QtCore.Qt.AlignCenter)
        self.label_volume.setObjectName("label_volume")
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
        self.btn_car.setGeometry(QtCore.QRect(720, 264, 80, 70))
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
        self.btn_devices.setGeometry(QtCore.QRect(720, 337, 80, 70))
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
        self.btn_radio = QtWidgets.QWidget(self.centralwidget)
        self.btn_radio.setGeometry(QtCore.QRect(720, 191, 80, 70))
        self.btn_radio.setStyleSheet("#btn_radio {\n"
                                     "    background: #252525; color: white\n"
                                     "}\n"
                                     "\n"
                                     "#btn_radio::hover {\n"
                                     "    background: #303030;\n"
                                     "}\n"
                                     "\n"
                                     "#btn_radio::!enabled {\n"
                                     "    background: #595959;\n"
                                     "    border-bottom: 3px solid #E00000;\n"
                                     "}")
        self.btn_radio.setObjectName("btn_radio")
        self.text_btn_radio = QtWidgets.QLabel(self.btn_radio)
        self.text_btn_radio.setGeometry(QtCore.QRect(10, 47, 60, 15))
        font = QtGui.QFont()
        font.setFamily("Montserrat Light")
        font.setPointSize(11)
        self.text_btn_radio.setFont(font)
        self.text_btn_radio.setStyleSheet("")
        self.text_btn_radio.setLineWidth(1)
        self.text_btn_radio.setTextFormat(QtCore.Qt.AutoText)
        self.text_btn_radio.setAlignment(QtCore.Qt.AlignCenter)
        self.text_btn_radio.setWordWrap(False)
        self.text_btn_radio.setObjectName("text_btn_radio")
        self.image_btn_radio = QtWidgets.QLabel(self.btn_radio)
        self.image_btn_radio.setGeometry(QtCore.QRect(20, 3, 40, 40))
        self.image_btn_radio.setText("")
        self.image_btn_radio.setPixmap(QtGui.QPixmap(":/images/radio.svg"))
        self.image_btn_radio.setScaledContents(True)
        self.image_btn_radio.setObjectName("image_btn_radio")
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
        self.text_btn_settings.setGeometry(QtCore.QRect(10, 42, 60, 20))
        font = QtGui.QFont()
        font.setFamily("Montserrat Light")
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

        # Setup OBD2 connection
        obd.logger.setLevel(obd.logging.DEBUG)
        attempts = "-"
        for i in range(20):
            self.obd_conn = obd.Async(protocol="6", baudrate=38400, fast=False)
            if self.obd_conn.supports(obd.commands.AMBIANT_AIR_TEMP):
                attempts = str(i+1)
                print("Needed connection attempts: " + attempts)
                break
            self.obd_conn.close()
        with open("obd2conn_attempts.txt", "a") as file:
            file.write(attempts)

        self.obd_conn.watch(obd.commands.AMBIANT_AIR_TEMP, callback=self.tempChanged)

        # Home
        self.content_home = QtWidgets.QWidget()
        self.ui_home = home.Ui_content()
        self.ui_home.setupUi(self.content_home, self)
        self.content.addWidget(self.content_home)

        # Media
        self.content_media = QtWidgets.QWidget()
        self.ui_media = media.Ui_content()
        self.ui_media.setupUi(self.content_media)
        if self.ui_media.useBluetooth:
            self.ui_media.switchToBluetooth(None)
        self.content.addWidget(self.content_media)

        # Radio
        self.content_radio = QtWidgets.QWidget()
        self.ui_radio = radio.Ui_content()
        self.ui_radio.setupUi(self.content_radio)
        self.content.addWidget(self.content_radio)

        # Car
        self.content_car = QtWidgets.QWidget()
        self.ui_car = car.Ui_content()
        self.ui_car.setupUi(self.content_car, self.obd_conn)
        self.content.addWidget(self.content_car)

        # Devices
        self.content_devices = QtWidgets.QWidget()
        ui_devices = devices.Ui_content()
        ui_devices.setupUi(self.content_devices)
        self.content.addWidget(self.content_devices)

        # Android Auto
        if platform == "linux" or platform == "linux2":
            self.startAA(None)

        # Settings
        self.content_settings = QtWidgets.QWidget()
        self.ui_settings = settings.Ui_content()
        self.ui_settings.setupUi(self.content_settings)
        self.content.addWidget(self.content_settings)
        self.label_volume_up.mouseReleaseEvent = self.volumeUpPressed
        self.label_volume_down.mouseReleaseEvent = self.volumeDownPressed

        # Set button actions
        self.btn_home.mouseReleaseEvent = self.switchToHome
        self.btn_media.mouseReleaseEvent = self.switchToMedia
        self.btn_car.mouseReleaseEvent = self.switchToCar
        self.btn_devices.mouseReleaseEvent = self.switchToDevices
        self.btn_radio.mouseReleaseEvent = self.switchToRadio
        self.btn_settings.mouseReleaseEvent = self.switchToSettings

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.updateTimer = QtCore.QTimer(MainWindow)
        self.updateTimer.setInterval(100)
        self.updateTimer.timeout.connect(self.updateUI)
        self.updateTimer.start()

        threading.Thread(target=self.steeringWheelControls).start()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Headunit"))
        self.label_title.setText(_translate("MainWindow", "HOME"))
        self.label_temperature.setText(_translate("MainWindow", "- °C"))
        self.label_volume.setText(_translate("MainWindow", "-"))
        self.text_btn_media.setText(_translate("MainWindow", "Media"))
        self.text_btn_home.setText(_translate("MainWindow", "Home"))
        self.text_btn_car.setText(_translate("MainWindow", "Car"))
        self.text_btn_devices.setText(_translate("MainWindow", "Devices"))
        self.text_btn_radio.setText(_translate("MainWindow", "Radio"))
        self.text_btn_settings.setText(_translate("MainWindow", "Settings"))

    def tempChanged(self, t):
        if not t.is_null():
            self.label_temperature.setText(t + " °C")

    def switchToHome(self, event):
        self.content.setCurrentWidget(self.content_home)
        self.btn_home.setEnabled(False)
        self.current_tab.setEnabled(True)
        self.label_title.setText("HOME")
        self.current_tab = self.btn_home

    def switchToMedia(self, event):
        self.content.setCurrentWidget(self.content_media)
        self.btn_media.setEnabled(False)
        self.current_tab.setEnabled(True)
        self.label_title.setText("MEDIA")
        self.current_tab = self.btn_media
        if self.ui_media.useBluetooth:
            self.ui_media.switchToBluetooth(None)
        if not self.ui_media.ui_music_player.updateThreadRunning:
            #self.ui_media.ui_music_player.updateUI()
            pass

    def switchToCar(self, event):
        self.content.setCurrentWidget(self.content_car)
        self.btn_car.setEnabled(False)
        self.current_tab.setEnabled(True)
        self.label_title.setText("CAR")
        self.current_tab = self.btn_car

    def switchToDevices(self, event):
        self.content.setCurrentWidget(self.content_devices)
        self.btn_devices.setEnabled(False)
        self.current_tab.setEnabled(True)
        self.label_title.setText("DEVICES")
        self.current_tab = self.btn_devices

    def switchToRadio(self, event):
        self.content.setCurrentWidget(self.content_radio)
        self.btn_radio.setEnabled(False)
        self.current_tab.setEnabled(True)
        self.label_title.setText("RADIO")
        self.current_tab = self.btn_radio
        self.ui_radio.loadFavourites()

    def switchToSettings(self, event):
        self.content.setCurrentWidget(self.content_settings)
        self.btn_settings.setEnabled(False)
        self.current_tab.setEnabled(True)
        self.label_title.setText("SETTINGS")
        self.current_tab = self.btn_settings

    def updateUI(self):
        volume = str(self.ui_settings.volume)
        self.label_volume.setText(volume)

        self.ui_home.updateUI()

    def startAA(self, event):
        self.aa_process = subprocess.Popen(["sudo", "/home/pi/openauto/bin/autoapp"])
        self.content_home.label_android_auto_desc.setText("Connect your\n"
                                                                   "Android mobile\n"
                                                                   "phone to launch\n"
                                                                   "Android Auto")
        self.content_home.label_android_auto_startstop.setText("Press to stop")

    def stopAA(self, event):
        if hasattr(self, 'aa_process'):
            self.aa_process.kill()
        self.content_home.label_android_auto_desc.setText("Not running")
        self.content_home.label_android_auto_startstop.setText("Press to start")

    def volumeUpPressed(self, event):
        self.ui_settings.changeVolume(self.ui_settings.volume + 2)

    def volumeDownPressed(self, event):
        self.ui_settings.changeVolume(self.ui_settings.volume - 2)

    def tempChanged(self, t):
        if not t.is_null():
            temp = str(t).split(" ")[0]
            print("Temp: " + temp)
            self.label_temperature.setText(temp + " °C")

    def steeringWheelControls(self):
        print("Steering wheel controls client started")
        longpress = 1.0
        self.aa_wid = "-1"

        s = serial.Serial("/dev/ttyACM0", 9600, timeout=1)
        s.isOpen()

        os.system("sudo modprobe uinput")
        time.sleep(0.5)
        os.system("sudo chmod 777 /dev/uinput")
        virtual_kb = uinput.Device([uinput.KEY_P, uinput.KEY_O, uinput.KEY_V, uinput.KEY_N, uinput.KEY_B, uinput.KEY_M, uinput.KEY_LEFTALT, uinput.KEY_TAB, uinput.KEY_ENTER])

        while True:
            if s.in_waiting > 0:
                line = s.readline().decode("utf-8")
                try:
                    command, duration_string = line.split("|")
                    duration = float(duration_string)

                    if duration >= 0.1:
                        print("Command received: '" + command + "' (" + str(duration) + ")")
                        window_name = subprocess.check_output(["xdotool", "getactivewindow", "getwindowname"]).decode("utf-8")
                        print("Active window: '" + window_name + "'")
                        if ("autoapp" in window_name):
                            in_aa = True
                            self.aa_wid = subprocess.check_output(["xdotool", "getactivewindow"]).decode("utf-8")
                            print("Saved Android Auto WID: " + self.aa_wid)
                        else:
                            in_aa = False
            
                        if command == "VOL+":
                            if duration >= longpress:
                                for i in range(5):
                                    self.volumeUpPressed(None)
                            else:
                                self.volumeUpPressed(None)
                        elif command == "VOL-":
                            if duration >= longpress:
                                for i in range(5):
                                    self.volumeDownPressed(None)
                            else:
                                self.volumeDownPressed(None)
                        elif command == "SEEK+":
                            if duration >= longpress:
                                self.ui_radio.upClicked(None)
                            else:
                                if in_aa:
                                    virtual_kb.emit_click(uinput.KEY_N)
                                else:
                                    self.ui_media.ui_music_player.nextBtnPressed(None)
                        elif command == "SEEK-":
                            if duration >= longpress:
                                self.ui_radio.downClicked(None)
                            else:
                                if in_aa:
                                    virtual_kb.emit_click(uinput.KEY_V)
                                else:
                                    self.ui_media.ui_music_player.rewindBtnPressed(None)
                        elif command == "MODE" and self.aa_wid != "-1":
                            active_wid = subprocess.check_output(["xdotool", "getactivewindow"]).decode("utf-8")
                            print("Current Window: " + active_wid)
                            main_wid = subprocess.check_output(["xdotool", "search", "--name", "Headunit"]).decode("utf-8")
                            print("Headunit: " + main_wid)

                            if (active_wid == main_wid):
                                os.system("xdotool windowactivate " + self.aa_wid)
                            else:
                                os.system("xdotool windowactivate " + main_wid)
                        elif command == "CALL END":
                            virtual_kb.emit_click(uinput.KEY_O)
                        elif command == "CALL START":
                            virtual_kb.emit_click(uinput.KEY_P)
                        elif command == "VOICE":
                            if duration >= 5.0:
                                subprocess.call(['shutdown', '-h', 'now'], shell=False)
                            elif duration >= longpress:
                                virtual_kb.emit_click(uinput.KEY_M)
                            else:
                                if in_aa:
                                    virtual_kb.emit_click(uinput.KEY_B)
                                else:
                                    self.ui_media.ui_music_player.playBtnPressed(None)
                except Exception as e:
                    print("Error on Steering Wheel Controls:")
                    print(e)
