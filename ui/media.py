# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'media.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import os
import random
import subprocess
import threading

import pygame
from PyQt5 import QtCore, QtGui, QtWidgets
from mutagen.easyid3 import EasyID3

import ui.media_music_player as media_music_player
import ui.media_file_browser as media_file_browser
from pygame import mixer


class Ui_content(object):
    current_bt_device = ""

    def setupUi(self, content):
        self.paused = True
        self.bt_paused = True
        self.useBluetooth = True
        self.current_file = ""
        self.queue = []
        self.current_dir = ""

        content.setObjectName("content")
        content.resize(720, 435)
        content.setStyleSheet("#content {\n"
                              "    background: black;\n"
                              "}\n"
                              "\n"
                              "* {\n"
                              "    color: white;\n"
                              "}")
        self.btn_bluetooth = QtWidgets.QWidget(content)
        self.btn_bluetooth.setEnabled(False)
        self.btn_bluetooth.setGeometry(QtCore.QRect(30, 30, 180, 45))
        self.btn_bluetooth.setStyleSheet("#btn_bluetooth {\n"
                                         "    background: #252525; color: white\n"
                                         "}\n"
                                         "\n"
                                         "#btn_bluetooth::hover {\n"
                                         "    background: #303030;\n"
                                         "}\n"
                                         "\n"
                                         "#btn_bluetooth::!enabled {\n"
                                         "    background: #595959;\n"
                                         "    border-bottom: 3px solid #E00000;\n"
                                         "}")
        self.btn_bluetooth.setObjectName("btn_bluetooth")
        self.text_btn_bluetooth = QtWidgets.QLabel(self.btn_bluetooth)
        self.text_btn_bluetooth.setGeometry(QtCore.QRect(20, 10, 140, 25))
        font = QtGui.QFont()
        font.setFamily("Montserrat Light")
        font.setPointSize(16)
        self.text_btn_bluetooth.setFont(font)
        self.text_btn_bluetooth.setLineWidth(1)
        self.text_btn_bluetooth.setAlignment(QtCore.Qt.AlignCenter)
        self.text_btn_bluetooth.setObjectName("text_btn_bluetooth")
        self.btn_usb = QtWidgets.QWidget(content)
        self.btn_usb.setEnabled(True)
        self.btn_usb.setGeometry(QtCore.QRect(230, 30, 180, 45))
        self.btn_usb.setStyleSheet("#btn_usb {\n"
                                   "    background: #252525; color: white\n"
                                   "}\n"
                                   "\n"
                                   "#btn_usb::hover {\n"
                                   "    background: #303030;\n"
                                   "}\n"
                                   "\n"
                                   "#btn_usb::!enabled {\n"
                                   "    background: #595959;\n"
                                   "    border-bottom: 3px solid #E00000;\n"
                                   "}")
        self.btn_usb.setObjectName("btn_usb")
        self.text_btn_usb = QtWidgets.QLabel(self.btn_usb)
        self.text_btn_usb.setGeometry(QtCore.QRect(20, 10, 140, 25))
        font = QtGui.QFont()
        font.setFamily("Montserrat Light")
        font.setPointSize(16)
        self.text_btn_usb.setFont(font)
        self.text_btn_usb.setLineWidth(1)
        self.text_btn_usb.setAlignment(QtCore.Qt.AlignCenter)
        self.text_btn_usb.setObjectName("text_btn_usb")
        self.content = QtWidgets.QStackedWidget(content)
        self.content.setGeometry(QtCore.QRect(30, 100, 660, 300))
        self.content.setObjectName("content")
        self.btn_file_browser = QtWidgets.QWidget(content)
        self.btn_file_browser.setEnabled(True)
        self.btn_file_browser.setVisible(False)
        self.btn_file_browser.setGeometry(QtCore.QRect(600, 30, 70, 45))
        self.btn_file_browser.setStyleSheet("#btn_file_browser {\n"
                                            "    background: #252525; color: white\n"
                                            "}\n"
                                            "\n"
                                            "#btn_file_browser::hover {\n"
                                            "    background: #303030;\n"
                                            "}\n"
                                            "\n"
                                            "#btn_file_browser::!enabled {\n"
                                            "    background: #595959;\n"
                                            "    border-bottom: 3px solid #E00000;\n"
                                            "}")
        self.btn_file_browser.setObjectName("btn_file_browser")
        self.text_btn_file_browser = QtWidgets.QLabel(self.btn_file_browser)
        self.text_btn_file_browser.setGeometry(QtCore.QRect(15, 2, 40, 40))
        font = QtGui.QFont()
        font.setFamily("Avenir Next LT Pro")
        font.setPointSize(16)
        self.text_btn_file_browser.setFont(font)
        self.text_btn_file_browser.setLineWidth(1)
        self.text_btn_file_browser.setText("")
        self.text_btn_file_browser.setPixmap(QtGui.QPixmap(":/images/file_browser.svg"))
        self.text_btn_file_browser.setScaledContents(True)
        self.text_btn_file_browser.setAlignment(QtCore.Qt.AlignCenter)
        self.text_btn_file_browser.setObjectName("text_btn_file_browser")

        # Music Player
        content_music_player = QtWidgets.QWidget()
        self.ui_music_player = media_music_player.Ui_content()
        self.ui_music_player.setupUi(content_music_player, self)
        self.content.addWidget(content_music_player)

        # File Browser
        content_file_browser = QtWidgets.QWidget()
        ui_file_browser = media_file_browser.Ui_content()
        ui_file_browser.setupUi(content_file_browser, self)
        self.content.addWidget(content_file_browser)

        # Set button actions
        self.btn_bluetooth.mouseReleaseEvent = self.switchToBluetooth
        self.btn_usb.mouseReleaseEvent = self.switchToUSB
        self.btn_file_browser.mouseReleaseEvent = self.switchToFileBrowser

        self.retranslateUi(content)
        QtCore.QMetaObject.connectSlotsByName(content)

        mixer.init()
        self.ui_music_player.updateUI()
        pygame.init()
        self.cooldown = False
        self.stopped = True
        self.checkForMusicStop()

    def retranslateUi(self, content):
        _translate = QtCore.QCoreApplication.translate
        content.setWindowTitle(_translate("content", "Form"))
        self.text_btn_bluetooth.setText(_translate("content", "Bluetooth"))
        self.text_btn_usb.setText(_translate("content", "USB"))

    def switchToBluetooth(self, event):
        self.content.setCurrentIndex(0)
        self.btn_bluetooth.setEnabled(False)
        self.btn_usb.setEnabled(True)
        self.btn_file_browser.setVisible(False)
        self.stop()
        self.useBluetooth = True
        self.ui_music_player.setupBluetooth = True
        #self.bt_process = subprocess.Popen(['bluealsa-aplay', self.current_bt_device])
        self.ui_music_player.music_slider.setEnabled(False)

    def switchToUSB(self, event):
        self.content.setCurrentIndex(0)
        self.btn_bluetooth.setEnabled(True)
        self.btn_usb.setEnabled(False)
        self.btn_file_browser.setEnabled(True)
        self.btn_file_browser.setVisible(True)
        self.useBluetooth = False
        self.ui_music_player.music_slider.setEnabled(True)

    def switchToFileBrowser(self, event):
        self.content.setCurrentIndex(1)
        self.btn_bluetooth.setEnabled(True)
        self.btn_usb.setEnabled(True)
        self.btn_file_browser.setEnabled(False)
        self.btn_file_browser.setVisible(True)

    def play(self):
        if self.useBluetooth:
            print("Play")
            self.ui_music_player.player_iface.Play()
        else:
            print("Playing file: " + self.current_file)
            try:
                self.setPlaying()
                mixer.music.load(self.current_file)
                mixer.music.play()
                self.startCooldown()
            except:
                print("File could not be played")

    def setPlaying(self):
        self.paused = False
        self.stopped = False
        self.ui_music_player.btn_play.setPixmap(QtGui.QPixmap(":/images/pause.svg"))
        self.ui_music_player.current_offset = 0

    def pause(self):
        if not self.cooldown:
            if self.useBluetooth:
                if self.bt_paused:
                    print("Play")
                    try:
                        self.ui_music_player.player_iface.Play()
                        self.bt_paused = False
                    except:
                        pass
                else:
                    try:
                        self.ui_music_player.player_iface.Pause()
                        self.bt_paused = True
                    except:
                        pass
            else:
                if not self.paused:
                    mixer.music.pause()
                    self.paused = True
                    self.ui_music_player.btn_play.setPixmap(QtGui.QPixmap(":/images/play.svg"))
                    print("Pause")
                else:
                    mixer.music.unpause()
                    self.paused = False
                    self.ui_music_player.btn_play.setPixmap(QtGui.QPixmap(":/images/pause.svg"))
                    print("Play")

    def next(self):
        if not self.cooldown:
            if self.useBluetooth:
                try:
                    self.ui_music_player.player_iface.Next()
                except:
                    pass
            else:
                mixer.music.stop()

    def rewind(self):
        if not self.cooldown:
            if self.useBluetooth:
                try:
                    self.ui_music_player.player_iface.Previous()
                except:
                    pass
            else:
                mixer.music.stop()
                self.play()

    def checkForMusicStop(self):
        try:
            if not self.stopped:
                if not mixer.music.get_busy():
                    next_track = ""
                    if len(self.queue) > 0:
                        next_track = self.queue[0]
                        self.queue.remove(self.queue[0])
                    elif os.path.exists(self.current_dir):
                        files = []
                        audio_files = [".mp3"]

                        for item in os.listdir(self.current_dir):
                            if os.path.isfile(os.path.join(self.current_dir, item)):
                                filename, file_extension = os.path.splitext(item)
                                if file_extension in audio_files:
                                    files.append(item)

                        next_track = random.choice(files)

                    if not next_track == "":
                        self.current_file = os.path.join(self.current_dir, next_track)
                        self.play()
        finally:
            threading.Timer(0.1, self.checkForMusicStop).start()

    def startCooldown(self):
        self.cooldown = True
        threading.Timer(1, self.finishCooldown).start()

    def finishCooldown(self):
        self.cooldown = False

    def stop(self):
        mixer.music.stop()
        self.stopped = True
