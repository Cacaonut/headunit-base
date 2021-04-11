# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'home.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import threading

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_content(object):
    def setupUi(self, content, owner):
        self.owner = owner
        content.setObjectName("content")
        content.resize(720, 435)
        content.setStyleSheet("#content {\n"
                              "    background: black;\n"
                              "}\n"
                              "\n"
                              "* {\n"
                              "    color: white;\n"
                              "}")
        self.widget_car = QtWidgets.QWidget(content)
        self.widget_car.setGeometry(QtCore.QRect(20, 20, 210, 190))
        self.widget_car.setStyleSheet("background: #262626")
        self.widget_car.setObjectName("widget_car")
        self.widget_car.mouseReleaseEvent = self.owner.switchToCar
        self.label_speed = QtWidgets.QLabel(self.widget_car)
        self.label_speed.setGeometry(QtCore.QRect(55, 25, 100, 30))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(16)
        self.label_speed.setFont(font)
        self.label_speed.setAlignment(QtCore.Qt.AlignCenter)
        self.label_speed.setObjectName("label_speed")
        self.label_speed_value = QtWidgets.QLabel(self.widget_car)
        self.label_speed_value.setGeometry(QtCore.QRect(55, 55, 100, 30))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(14)
        self.label_speed_value.setFont(font)
        self.label_speed_value.setStyleSheet("color: #D9D9D9")
        self.label_speed_value.setAlignment(QtCore.Qt.AlignCenter)
        self.label_speed_value.setObjectName("label_speed_value")
        self.label_rotation = QtWidgets.QLabel(self.widget_car)
        self.label_rotation.setGeometry(QtCore.QRect(55, 105, 100, 30))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(16)
        self.label_rotation.setFont(font)
        self.label_rotation.setAlignment(QtCore.Qt.AlignCenter)
        self.label_rotation.setObjectName("label_rotation")
        self.label_rotation_value = QtWidgets.QLabel(self.widget_car)
        self.label_rotation_value.setGeometry(QtCore.QRect(55, 135, 100, 30))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(14)
        self.label_rotation_value.setFont(font)
        self.label_rotation_value.setStyleSheet("color: #D9D9D9")
        self.label_rotation_value.setAlignment(QtCore.Qt.AlignCenter)
        self.label_rotation_value.setObjectName("label_rotation_value")
        self.widget_radio = QtWidgets.QWidget(content)
        self.widget_radio.setGeometry(QtCore.QRect(20, 230, 210, 190))
        self.widget_radio.setStyleSheet("background: #262626")
        self.widget_radio.setObjectName("widget_radio")
        self.widget_radio.mouseReleaseEvent = self.owner.switchToRadio
        self.label_radio = QtWidgets.QLabel(self.widget_radio)
        self.label_radio.setGeometry(QtCore.QRect(55, 15, 100, 30))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(16)
        self.label_radio.setFont(font)
        self.label_radio.setAlignment(QtCore.Qt.AlignCenter)
        self.label_radio.setObjectName("label_radio")
        self.btn_play_radio = QtWidgets.QLabel(self.widget_radio)
        self.btn_play_radio.setGeometry(QtCore.QRect(80, 115, 50, 50))
        self.btn_play_radio.setText("")
        self.btn_play_radio.setPixmap(QtGui.QPixmap(":/images/play.svg"))
        self.btn_play_radio.setScaledContents(True)
        self.btn_play_radio.setObjectName("btn_play_radio")
        self.label_station = QtWidgets.QLabel(self.widget_radio)
        self.label_station.setGeometry(QtCore.QRect(40, 70, 130, 30))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(14)
        self.label_station.setFont(font)
        self.label_station.setStyleSheet("color: #D9D9D9")
        self.label_station.setAlignment(QtCore.Qt.AlignCenter)
        self.label_station.setObjectName("label_station")
        self.btn_up_radio = QtWidgets.QLabel(self.widget_radio)
        self.btn_up_radio.setGeometry(QtCore.QRect(135, 115, 50, 50))
        self.btn_up_radio.setText("")
        self.btn_up_radio.setPixmap(QtGui.QPixmap(":/images/radio_up.svg"))
        self.btn_up_radio.setScaledContents(True)
        self.btn_up_radio.setObjectName("btn_up_radio")
        self.btn_down_radio = QtWidgets.QLabel(self.widget_radio)
        self.btn_down_radio.setGeometry(QtCore.QRect(25, 115, 50, 50))
        self.btn_down_radio.setText("")
        self.btn_down_radio.setPixmap(QtGui.QPixmap(":/images/radio_down.svg"))
        self.btn_down_radio.setScaledContents(True)
        self.btn_down_radio.setObjectName("btn_down_radio")
        self.widget_2 = QtWidgets.QWidget(content)
        self.widget_2.setGeometry(QtCore.QRect(490, 20, 210, 190))
        self.widget_2.setStyleSheet("background: #262626")
        self.widget_2.setObjectName("widget_2")
        self.label_diagnostics = QtWidgets.QLabel(self.widget_2)
        self.label_diagnostics.setGeometry(QtCore.QRect(25, 15, 160, 30))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(16)
        self.label_diagnostics.setFont(font)
        self.label_diagnostics.setAlignment(QtCore.Qt.AlignCenter)
        self.label_diagnostics.setObjectName("label_diagnostics")
        self.label_diagnostics_desc = QtWidgets.QLabel(self.widget_2)
        self.label_diagnostics_desc.setGeometry(QtCore.QRect(20, 110, 170, 60))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(14)
        self.label_diagnostics_desc.setFont(font)
        self.label_diagnostics_desc.setStyleSheet("color: #D9D9D9")
        self.label_diagnostics_desc.setAlignment(QtCore.Qt.AlignCenter)
        self.label_diagnostics_desc.setObjectName("label_diagnostics_desc")
        self.btn_diagnostics_check = QtWidgets.QLabel(self.widget_2)
        self.btn_diagnostics_check.setGeometry(QtCore.QRect(80, 60, 50, 50))
        self.btn_diagnostics_check.setText("")
        self.btn_diagnostics_check.setPixmap(QtGui.QPixmap(":/images/check_green.svg"))
        self.btn_diagnostics_check.setScaledContents(True)
        self.btn_diagnostics_check.setObjectName("btn_diagnostics_check")
        self.widget_media = QtWidgets.QWidget(content)
        self.widget_media.setGeometry(QtCore.QRect(255, 230, 210, 190))
        self.widget_media.setStyleSheet("background: #262626")
        self.widget_media.setObjectName("widget_media")
        self.widget_media.mouseReleaseEvent = self.owner.switchToMedia
        self.label_media = QtWidgets.QLabel(self.widget_media)
        self.label_media.setGeometry(QtCore.QRect(55, 15, 100, 30))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(16)
        self.label_media.setFont(font)
        self.label_media.setAlignment(QtCore.Qt.AlignCenter)
        self.label_media.setObjectName("label_media")
        self.btn_play_media = QtWidgets.QLabel(self.widget_media)
        self.btn_play_media.setGeometry(QtCore.QRect(80, 115, 50, 50))
        self.btn_play_media.setText("")
        self.btn_play_media.setPixmap(QtGui.QPixmap(":/images/play.svg"))
        self.btn_play_media.setScaledContents(True)
        self.btn_play_media.setObjectName("btn_play_media")
        self.label_song = QtWidgets.QLabel(self.widget_media)
        self.label_song.setGeometry(QtCore.QRect(20, 70, 170, 30))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(14)
        self.label_song.setFont(font)
        self.label_song.setStyleSheet("color: #D9D9D9")
        self.label_song.setAlignment(QtCore.Qt.AlignCenter)
        self.label_song.setObjectName("label_song")
        self.btn_next_media = QtWidgets.QLabel(self.widget_media)
        self.btn_next_media.setGeometry(QtCore.QRect(135, 115, 50, 50))
        self.btn_next_media.setText("")
        self.btn_next_media.setPixmap(QtGui.QPixmap(":/images/next.svg"))
        self.btn_next_media.setScaledContents(True)
        self.btn_next_media.setObjectName("btn_next_media")
        self.btn_last_media = QtWidgets.QLabel(self.widget_media)
        self.btn_last_media.setGeometry(QtCore.QRect(25, 115, 50, 50))
        self.btn_last_media.setText("")
        self.btn_last_media.setPixmap(QtGui.QPixmap(":/images/last.svg"))
        self.btn_last_media.setScaledContents(True)
        self.btn_last_media.setObjectName("btn_last_media")
        self.widget_android_auto = QtWidgets.QWidget(content)
        self.widget_android_auto.setGeometry(QtCore.QRect(490, 230, 210, 190))
        self.widget_android_auto.setStyleSheet("background: #262626")
        self.widget_android_auto.setObjectName("widget_android_auto")
        self.label_android_auto = QtWidgets.QLabel(self.widget_android_auto)
        self.label_android_auto.setGeometry(QtCore.QRect(25, 15, 160, 30))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(16)
        self.label_android_auto.setFont(font)
        self.label_android_auto.setAlignment(QtCore.Qt.AlignCenter)
        self.label_android_auto.setObjectName("label_android_auto")
        self.label_android_auto_desc = QtWidgets.QLabel(self.widget_android_auto)
        self.label_android_auto_desc.setGeometry(QtCore.QRect(20, 60, 170, 110))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(14)
        self.label_android_auto_desc.setFont(font)
        self.label_android_auto_desc.setStyleSheet("color: #D9D9D9")
        self.label_android_auto_desc.setAlignment(QtCore.Qt.AlignCenter)
        self.label_android_auto_desc.setObjectName("label_android_auto_desc")
        self.label = QtWidgets.QLabel(content)
        self.label.setGeometry(QtCore.QRect(255, 53, 210, 123))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/images/toyota.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")

        self.retranslateUi(content)
        QtCore.QMetaObject.connectSlotsByName(content)

        self.finishedMediaSetup = False
        self.finishedRadioSetup = False

    def retranslateUi(self, content):
        _translate = QtCore.QCoreApplication.translate
        content.setWindowTitle(_translate("content", "Form"))
        self.label_speed.setText(_translate("content", "Speed"))
        self.label_speed_value.setText(_translate("content", "-"))
        self.label_rotation.setText(_translate("content", "Rotation"))
        self.label_rotation_value.setText(_translate("content", "-"))
        self.label_radio.setText(_translate("content", "Radio"))
        self.label_station.setText(_translate("content", "-"))
        self.label_diagnostics.setText(_translate("content", "Diagnostics"))
        self.label_diagnostics_desc.setText(_translate("content", "All tests were\n"
                                                                  "successful"))
        self.label_media.setText(_translate("content", "Media"))
        self.label_song.setText(_translate("content", "-"))
        self.label_android_auto.setText(_translate("content", "Android Auto"))
        self.label_android_auto_desc.setText(_translate("content", "Connect your\n"
                                                                   "Android mobile\n"
                                                                   "phone to launch\n"
                                                                   "Android Auto"))

    def updateUI(self):
        try:
            # Cockpit
            if hasattr(self.owner, "ui_car") and hasattr(self.owner.ui_car, "ui_cockpit"):
                self.label_speed_value.setText(str(self.owner.ui_car.ui_cockpit.speed) + " km/h")
                self.label_rotation_value.setText(str(self.owner.ui_car.ui_cockpit.rpm) + " rpm")

            # Radio
            if hasattr(self.owner, "ui_radio"):
                if not self.finishedRadioSetup:
                    self.finishRadioSetup()
                radio_station = self.owner.ui_radio.label_station.text()
                if radio_station == "-":
                    radio_station = self.owner.ui_radio.label_frequency.text()
                self.label_station.setText(radio_station)
                if self.owner.ui_radio.playing:
                    self.btn_play_radio.setPixmap(QtGui.QPixmap(":/images/pause.svg"))
                else:
                    self.btn_play_radio.setPixmap(QtGui.QPixmap(":/images/play.svg"))

            # Media
            if hasattr(self.owner, "ui_media"):
                if not self.finishedMediaSetup:
                    self.finishMediaSetup()
                self.label_song.setText(self.owner.ui_media.ui_music_player.label_title.text())
                playing = True
                if self.owner.ui_media.useBluetooth:
                    playing = not self.owner.ui_media.bt_paused
                else:
                    playing = not self.owner.ui_media.paused
                if playing:
                    self.btn_play_media.setPixmap(QtGui.QPixmap(":/images/pause.svg"))
                else:
                    self.btn_play_media.setPixmap(QtGui.QPixmap(":/images/play.svg"))
        except Exception as e:
            print("Error updating home view:")
            print(e)

    def finishMediaSetup(self):
        self.finishedMediaSetup = True
        self.btn_play_media.mouseReleaseEvent = self.owner.ui_media.ui_music_player.playBtnPressed
        self.btn_next_media.mouseReleaseEvent = self.owner.ui_media.ui_music_player.nextBtnPressed
        self.btn_last_media.mouseReleaseEvent = self.owner.ui_media.ui_music_player.rewindBtnPressed

    def finishRadioSetup(self):
        self.finishedRadioSetup = True
        self.btn_play_radio.mouseReleaseEvent = self.owner.ui_radio.playPressed
        self.btn_up_radio.mouseReleaseEvent = self.owner.ui_radio.upClicked
        self.btn_down_radio.mouseReleaseEvent = self.owner.ui_radio.downClicked
