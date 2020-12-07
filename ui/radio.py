# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'radio.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import subprocess, shlex
import threading

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_content(object):
    def setupUi(self, content):
        content.setObjectName("content")
        content.resize(720, 435)
        content.setStyleSheet("#content {\n"
                              "    background: black;\n"
                              "}\n"
                              "\n"
                              "* {\n"
                              "    color: white;\n"
                              "}")
        self.station_cover = QtWidgets.QLabel(content)
        self.station_cover.setGeometry(QtCore.QRect(70, 70, 200, 200))
        self.station_cover.setText("")
        self.station_cover.setPixmap(QtGui.QPixmap(":/images/station_cover.png"))
        self.station_cover.setScaledContents(True)
        self.station_cover.setObjectName("station_cover")
        self.station_icon = QtWidgets.QLabel(content)
        self.station_icon.setGeometry(QtCore.QRect(310, 80, 30, 30))
        self.station_icon.setText("")
        self.station_icon.setPixmap(QtGui.QPixmap(":/images/station.svg"))
        self.station_icon.setScaledContents(True)
        self.station_icon.setObjectName("station_icon")
        self.label_station = QtWidgets.QLabel(content)
        self.label_station.setGeometry(QtCore.QRect(355, 80, 300, 30))
        font = QtGui.QFont()
        font.setFamily("Comfortaa")
        font.setPointSize(12)
        self.label_station.setFont(font)
        self.label_station.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_station.setObjectName("label_station")
        self.frequency_icon = QtWidgets.QLabel(content)
        self.frequency_icon.setGeometry(QtCore.QRect(310, 120, 30, 30))
        self.frequency_icon.setText("")
        self.frequency_icon.setPixmap(QtGui.QPixmap(":/images/frequency.svg"))
        self.frequency_icon.setScaledContents(True)
        self.frequency_icon.setObjectName("frequency_icon")
        self.label_frequency = QtWidgets.QLabel(content)
        self.label_frequency.setGeometry(QtCore.QRect(355, 120, 300, 30))
        font = QtGui.QFont()
        font.setFamily("Comfortaa")
        font.setPointSize(12)
        self.label_frequency.setFont(font)
        self.label_frequency.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_frequency.setObjectName("label_frequency")
        self.info_icon = QtWidgets.QLabel(content)
        self.info_icon.setGeometry(QtCore.QRect(310, 160, 30, 30))
        self.info_icon.setText("")
        self.info_icon.setPixmap(QtGui.QPixmap(":/images/music.svg"))
        self.info_icon.setScaledContents(True)
        self.info_icon.setObjectName("info_icon")
        self.label_info = QtWidgets.QLabel(content)
        self.label_info.setGeometry(QtCore.QRect(355, 160, 300, 30))
        font = QtGui.QFont()
        font.setFamily("Comfortaa")
        font.setPointSize(12)
        self.label_info.setFont(font)
        self.label_info.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_info.setObjectName("label_info")
        self.btn_down = QtWidgets.QLabel(content)
        self.btn_down.setGeometry(QtCore.QRect(380, 230, 50, 50))
        self.btn_down.setText("")
        self.btn_down.setPixmap(QtGui.QPixmap(":/images/radio_down.svg"))
        self.btn_down.setScaledContents(True)
        self.btn_down.setObjectName("btn_down")
        self.btn_down.mouseReleaseEvent = self.down
        self.btn_play = QtWidgets.QLabel(content)
        self.btn_play.setGeometry(QtCore.QRect(450, 230, 50, 50))
        self.btn_play.setText("")
        self.btn_play.setPixmap(QtGui.QPixmap(":/images/play.svg"))
        self.btn_play.setScaledContents(True)
        self.btn_play.setObjectName("btn_play")
        self.btn_play.mouseReleaseEvent = self.playPressed
        self.btn_up = QtWidgets.QLabel(content)
        self.btn_up.setGeometry(QtCore.QRect(520, 230, 50, 50))
        self.btn_up.setText("")
        self.btn_up.setPixmap(QtGui.QPixmap(":/images/radio_up.svg"))
        self.btn_up.setScaledContents(True)
        self.btn_up.setObjectName("btn_up")
        self.btn_up.mouseReleaseEvent = self.up
        self.btn_fav_1 = QtWidgets.QWidget(content)
        self.btn_fav_1.setEnabled(True)
        self.btn_fav_1.setGeometry(QtCore.QRect(51, 345, 122, 61))
        self.btn_fav_1.setStyleSheet("#btn_fav_1 {\n"
                                     "    background: #252525; color: white\n"
                                     "}\n"
                                     "\n"
                                     "#btn_fav_1::hover {\n"
                                     "    background: #303030;\n"
                                     "}\n"
                                     "\n"
                                     "#btn_fav_1::!enabled {\n"
                                     "    background: #595959;\n"
                                     "    border-bottom: 3px solid #E00000;\n"
                                     "}")
        self.btn_fav_1.setObjectName("btn_fav_1")
        self.btn_fav_1.mouseReleaseEvent = self.favourite1
        self.btn_fav_1_frequency = QtWidgets.QLabel(self.btn_fav_1)
        self.btn_fav_1_frequency.setGeometry(QtCore.QRect(0, 7, 122, 25))
        font = QtGui.QFont()
        font.setFamily("Comfortaa")
        font.setPointSize(14)
        self.btn_fav_1_frequency.setFont(font)
        self.btn_fav_1_frequency.setAlignment(QtCore.Qt.AlignCenter)
        self.btn_fav_1_frequency.setObjectName("btn_fav_1_frequency")
        self.btn_fav_1_station = QtWidgets.QLabel(self.btn_fav_1)
        self.btn_fav_1_station.setGeometry(QtCore.QRect(0, 32, 122, 20))
        font = QtGui.QFont()
        font.setFamily("Comfortaa")
        font.setPointSize(10)
        self.btn_fav_1_station.setFont(font)
        self.btn_fav_1_station.setAlignment(QtCore.Qt.AlignCenter)
        self.btn_fav_1_station.setObjectName("btn_fav_1_station")
        self.btn_fav_2 = QtWidgets.QWidget(content)
        self.btn_fav_2.setEnabled(True)
        self.btn_fav_2.setGeometry(QtCore.QRect(175, 345, 122, 61))
        self.btn_fav_2.setStyleSheet("#btn_fav_2 {\n"
                                     "    background: #252525; color: white\n"
                                     "}\n"
                                     "\n"
                                     "#btn_fav_2::hover {\n"
                                     "    background: #303030;\n"
                                     "}\n"
                                     "\n"
                                     "#btn_fav_2::!enabled {\n"
                                     "    background: #595959;\n"
                                     "    border-bottom: 3px solid #E00000;\n"
                                     "}")
        self.btn_fav_2.setObjectName("btn_fav_2")
        self.btn_fav_2.mouseReleaseEvent = self.favourite2
        self.btn_fav_2_frequency = QtWidgets.QLabel(self.btn_fav_2)
        self.btn_fav_2_frequency.setGeometry(QtCore.QRect(0, 7, 122, 25))
        font = QtGui.QFont()
        font.setFamily("Comfortaa")
        font.setPointSize(14)
        self.btn_fav_2_frequency.setFont(font)
        self.btn_fav_2_frequency.setAlignment(QtCore.Qt.AlignCenter)
        self.btn_fav_2_frequency.setObjectName("btn_fav_2_frequency")
        self.btn_fav_2_station = QtWidgets.QLabel(self.btn_fav_2)
        self.btn_fav_2_station.setGeometry(QtCore.QRect(0, 32, 122, 20))
        font = QtGui.QFont()
        font.setFamily("Comfortaa")
        font.setPointSize(10)
        self.btn_fav_2_station.setFont(font)
        self.btn_fav_2_station.setAlignment(QtCore.Qt.AlignCenter)
        self.btn_fav_2_station.setObjectName("btn_fav_2_station")
        self.btn_fav_3 = QtWidgets.QWidget(content)
        self.btn_fav_3.setEnabled(True)
        self.btn_fav_3.setGeometry(QtCore.QRect(299, 345, 122, 61))
        self.btn_fav_3.setStyleSheet("#btn_fav_3 {\n"
                                     "    background: #252525; color: white\n"
                                     "}\n"
                                     "\n"
                                     "#btn_fav_3::hover {\n"
                                     "    background: #303030;\n"
                                     "}\n"
                                     "\n"
                                     "#btn_fav_3::!enabled {\n"
                                     "    background: #595959;\n"
                                     "    border-bottom: 3px solid #E00000;\n"
                                     "}")
        self.btn_fav_3.setObjectName("btn_fav_3")
        self.btn_fav_3.mouseReleaseEvent = self.favourite3
        self.btn_fav_3_frequency = QtWidgets.QLabel(self.btn_fav_3)
        self.btn_fav_3_frequency.setGeometry(QtCore.QRect(0, 7, 122, 25))
        font = QtGui.QFont()
        font.setFamily("Comfortaa")
        font.setPointSize(14)
        self.btn_fav_3_frequency.setFont(font)
        self.btn_fav_3_frequency.setAlignment(QtCore.Qt.AlignCenter)
        self.btn_fav_3_frequency.setObjectName("btn_fav_3_frequency")
        self.btn_fav_3_station = QtWidgets.QLabel(self.btn_fav_3)
        self.btn_fav_3_station.setGeometry(QtCore.QRect(0, 32, 122, 20))
        font = QtGui.QFont()
        font.setFamily("Comfortaa")
        font.setPointSize(10)
        self.btn_fav_3_station.setFont(font)
        self.btn_fav_3_station.setAlignment(QtCore.Qt.AlignCenter)
        self.btn_fav_3_station.setObjectName("btn_fav_3_station")
        self.btn_fav_4 = QtWidgets.QWidget(content)
        self.btn_fav_4.setEnabled(True)
        self.btn_fav_4.setGeometry(QtCore.QRect(423, 345, 122, 61))
        self.btn_fav_4.setStyleSheet("#btn_fav_4 {\n"
                                     "    background: #252525; color: white\n"
                                     "}\n"
                                     "\n"
                                     "#btn_fav_4::hover {\n"
                                     "    background: #303030;\n"
                                     "}\n"
                                     "\n"
                                     "#btn_fav_4::!enabled {\n"
                                     "    background: #595959;\n"
                                     "    border-bottom: 3px solid #E00000;\n"
                                     "}")
        self.btn_fav_4.setObjectName("btn_fav_4")
        self.btn_fav_4.mouseReleaseEvent = self.favourite4
        self.btn_fav_4_frequency = QtWidgets.QLabel(self.btn_fav_4)
        self.btn_fav_4_frequency.setGeometry(QtCore.QRect(0, 7, 122, 25))
        font = QtGui.QFont()
        font.setFamily("Comfortaa")
        font.setPointSize(14)
        self.btn_fav_4_frequency.setFont(font)
        self.btn_fav_4_frequency.setAlignment(QtCore.Qt.AlignCenter)
        self.btn_fav_4_frequency.setObjectName("btn_fav_4_frequency")
        self.btn_fav_4_station = QtWidgets.QLabel(self.btn_fav_4)
        self.btn_fav_4_station.setGeometry(QtCore.QRect(0, 32, 122, 20))
        font = QtGui.QFont()
        font.setFamily("Comfortaa")
        font.setPointSize(10)
        self.btn_fav_4_station.setFont(font)
        self.btn_fav_4_station.setAlignment(QtCore.Qt.AlignCenter)
        self.btn_fav_4_station.setObjectName("btn_fav_4_station")
        self.btn_fav_5 = QtWidgets.QWidget(content)
        self.btn_fav_5.setEnabled(True)
        self.btn_fav_5.setGeometry(QtCore.QRect(547, 345, 122, 61))
        self.btn_fav_5.setStyleSheet("#btn_fav_5 {\n"
                                     "    background: #252525; color: white\n"
                                     "}\n"
                                     "\n"
                                     "#btn_fav_5::hover {\n"
                                     "    background: #303030;\n"
                                     "}\n"
                                     "\n"
                                     "#btn_fav_5::!enabled {\n"
                                     "    background: #595959;\n"
                                     "    border-bottom: 3px solid #E00000;\n"
                                     "}")
        self.btn_fav_5.setObjectName("btn_fav_5")
        self.btn_fav_5.mouseReleaseEvent = self.favourite5
        self.btn_fav_5_frequency = QtWidgets.QLabel(self.btn_fav_5)
        self.btn_fav_5_frequency.setGeometry(QtCore.QRect(0, 7, 122, 25))
        font = QtGui.QFont()
        font.setFamily("Comfortaa")
        font.setPointSize(14)
        self.btn_fav_5_frequency.setFont(font)
        self.btn_fav_5_frequency.setAlignment(QtCore.Qt.AlignCenter)
        self.btn_fav_5_frequency.setObjectName("btn_fav_5_frequency")
        self.btn_fav_5_station = QtWidgets.QLabel(self.btn_fav_5)
        self.btn_fav_5_station.setGeometry(QtCore.QRect(0, 32, 122, 20))
        font = QtGui.QFont()
        font.setFamily("Comfortaa")
        font.setPointSize(10)
        self.btn_fav_5_station.setFont(font)
        self.btn_fav_5_station.setAlignment(QtCore.Qt.AlignCenter)
        self.btn_fav_5_station.setObjectName("btn_fav_5_station")
        self.btn_set_fav = QtWidgets.QLabel(content)
        self.btn_set_fav.setGeometry(QtCore.QRect(620, 80, 40, 40))
        self.btn_set_fav.setText("")
        self.btn_set_fav.setPixmap(QtGui.QPixmap(":/images/fav_empty.svg"))
        self.btn_set_fav.setScaledContents(True)
        self.btn_set_fav.setObjectName("btn_set_fav")
        self.btn_set_fav.mouseReleaseEvent = self.saveFavourite

        self.settings = QtCore.QSettings("Cacaonut", "Headunit")

        self.loadFavourites()

        self.playing = False
        self.changeFrequency(float(self.settings.value("radio/current_freq", 87.5)))

        self.retranslateUi(content)
        QtCore.QMetaObject.connectSlotsByName(content)

    def retranslateUi(self, content):
        _translate = QtCore.QCoreApplication.translate
        content.setWindowTitle(_translate("content", "Form"))
        self.label_station.setText(_translate("content", "-"))
        self.label_info.setText(_translate("content", "-"))

    def changeFrequency(self, frequency):
        self.current_freq = frequency
        self.settings.setValue("radio/current_freq", self.current_freq)
        self.label_frequency.setText(format(self.current_freq, ".1f") + " MHz")

        #if self.playing:
            #self.stop()
            #self.play()

        self.btn_fav_1.setEnabled(True)
        self.btn_fav_2.setEnabled(True)
        self.btn_fav_3.setEnabled(True)
        self.btn_fav_4.setEnabled(True)
        self.btn_fav_5.setEnabled(True)
        self.btn_set_fav.setPixmap(QtGui.QPixmap(":/images/fav_empty.svg"))

        if self.current_freq == self.slot1_freq:
            self.btn_fav_1.setEnabled(False)
            self.btn_set_fav.setPixmap(QtGui.QPixmap(":/images/fav_full.svg"))
        if self.current_freq == self.slot2_freq:
            self.btn_fav_2.setEnabled(False)
            self.btn_set_fav.setPixmap(QtGui.QPixmap(":/images/fav_full.svg"))
        if self.current_freq == self.slot3_freq:
            self.btn_fav_3.setEnabled(False)
            self.btn_set_fav.setPixmap(QtGui.QPixmap(":/images/fav_full.svg"))
        if self.current_freq == self.slot4_freq:
            self.btn_fav_4.setEnabled(False)
            self.btn_set_fav.setPixmap(QtGui.QPixmap(":/images/fav_full.svg"))
        if self.current_freq == self.slot5_freq:
            self.btn_fav_5.setEnabled(False)
            self.btn_set_fav.setPixmap(QtGui.QPixmap(":/images/fav_full.svg"))

    def loadFavourites(self):
        self.slot1_freq = float(self.settings.value("radio/favourite_1", 0))
        if self.slot1_freq == 0:
            self.btn_fav_1_frequency.setText("-")
        else:
            self.btn_fav_1_frequency.setText(format(self.slot1_freq, ".1f") + " MHz")

        self.slot2_freq = float(self.settings.value("radio/favourite_2", 0))
        if self.slot2_freq == 0:
            self.btn_fav_2_frequency.setText("-")
        else:
            self.btn_fav_2_frequency.setText(format(self.slot2_freq, ".1f") + " MHz")

        self.slot3_freq = float(self.settings.value("radio/favourite_3", 0))
        if self.slot3_freq == 0:
            self.btn_fav_3_frequency.setText("-")
        else:
            self.btn_fav_3_frequency.setText(format(self.slot3_freq, ".1f") + " MHz")

        self.slot4_freq = float(self.settings.value("radio/favourite_4", 0))
        if self.slot4_freq == 0:
            self.btn_fav_4_frequency.setText("-")
        else:
            self.btn_fav_4_frequency.setText(format(self.slot4_freq, ".1f") + " MHz")

        self.slot5_freq = float(self.settings.value("radio/favourite_5", 0))
        if self.slot5_freq == 0:
            self.btn_fav_5_frequency.setText("-")
        else:
            self.btn_fav_5_frequency.setText(format(self.slot5_freq, ".1f") + " MHz")

    def saveFavourite(self, event):
        if self.current_freq == self.slot1_freq:
            self.settings.setValue("radio/favourite_1", 0)
        elif self.current_freq == self.slot2_freq:
            self.settings.setValue("radio/favourite_2", 0)
        elif self.current_freq == self.slot3_freq:
            self.settings.setValue("radio/favourite_3", 0)
        elif self.current_freq == self.slot4_freq:
            self.settings.setValue("radio/favourite_4", 0)
        elif self.current_freq == self.slot5_freq:
            self.settings.setValue("radio/favourite_5", 0)
        elif self.slot1_freq == 0:
            self.slot1_freq = self.current_freq
            self.settings.setValue("radio/favourite_1", self.current_freq)
        elif self.slot2_freq == 0:
            self.slot2_freq = self.current_freq
            self.settings.setValue("radio/favourite_2", self.current_freq)
        elif self.slot3_freq == 0:
            self.slot3_freq = self.current_freq
            self.settings.setValue("radio/favourite_3", self.current_freq)
        elif self.slot4_freq == 0:
            self.slot4_freq = self.current_freq
            self.settings.setValue("radio/favourite_4", self.current_freq)
        elif self.slot5_freq == 0:
            self.slot5_freq = self.current_freq
            self.settings.setValue("radio/favourite_5", self.current_freq)
        self.loadFavourites()
        self.changeFrequency(self.current_freq)

    def favourite1(self, event):
        if self.slot1_freq > 0:
            self.changeFrequency(self.slot1_freq)

    def favourite2(self, event):
        if self.slot2_freq > 0:
            self.changeFrequency(self.slot2_freq)

    def favourite3(self, event):
        if self.slot3_freq > 0:
            self.changeFrequency(self.slot3_freq)

    def favourite4(self, event):
        if self.slot4_freq > 0:
            self.changeFrequency(self.slot4_freq)

    def favourite5(self, event):
        if self.slot5_freq > 0:
            self.changeFrequency(self.slot5_freq)

    def playPressed(self, event):
        if self.playing:
            self.stop()
        else:
            self.play()

    def play(self):
        self.playing = True
        command = 'rtl_fm -M fm -l 0 -A std -p 0 -s 171k -g 20 -F 9 -f 105.7M | readsea --feed-through | aplay -r ' \
                  '171000 -f S16_LE '
        self.process = subprocess.Popen(command, stderr=subprocess.PIPE, shell=True)
        thread = threading.Thread(target=self.fetchRDSOutput)
        thread.start()

        self.btn_play.setPixmap(QtGui.QPixmap(":/images/pause.svg"))

    def stop(self):
        self.playing = False
        self.btn_play.setPixmap(QtGui.QPixmap(":/images/play.svg"))
        if hasattr(self, "process"):
            self.process.kill()

    def up(self, event):
        self.changeFrequency(self.current_freq + 0.1)

    def down(self, event):
        self.changeFrequency(self.current_freq - 0.1)

    def fetchRDSOutput(self):
        while self.playing:
            output = self.process.stderr.readline().decode("utf-8")
            if output == "" and self.process.poll() is not None:
                break
            if True or output.startswith("{") and output.endswith("}"):
                print(">" + output)
