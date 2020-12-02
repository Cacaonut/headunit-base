# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'media_music_player.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import os
import threading

from PyQt5 import QtCore, QtGui, QtWidgets
from mutagen.easyid3 import EasyID3
from mutagen import File
from mutagen.mp3 import MP3
from pygame import mixer


class Ui_content(object):
    def setupUi(self, content, owner):
        self.owner = owner
        content.setObjectName("content")
        content.resize(660, 300)
        content.setStyleSheet("#content {\n"
                              "    background: black\n"
                              "}\n"
                              "\n"
                              "* {\n"
                              "    color: white\n"
                              "}")
        self.music_slider = QtWidgets.QSlider(content)
        self.music_slider.setGeometry(QtCore.QRect(80, 280, 500, 20))
        self.music_slider.setStyleSheet("QSlider::groove:horizontal { \n"
                                        "    background-color: #7F7F7F; \n"
                                        "    height: 2px;\n"
                                        "}\n"
                                        "\n"
                                        "QSlider::handle:horizontal { \n"
                                        "    background-color: #E00000; \n"
                                        "    width: 8px; \n"
                                        "    height: 8px;\n"
                                        "    border: 3px solid #E00000;\n"
                                        "    border-radius: 7px; \n"
                                        "    margin-top: -6px;\n"
                                        "    margin-bottom: -6px;\n"
                                        "}\n"
                                        "\n"
                                        "QSlider::sub-page:horizontal {\n"
                                        "    background-color: #E00000;\n"
                                        "}")
        self.music_slider.setOrientation(QtCore.Qt.Horizontal)
        self.music_slider.setObjectName("music_slider")
        self.music_slider.valueChanged.connect(self.sliderPressed)
        self.music_slider.mouseReleaseEvent = self.sliderChanged
        self.disc_cover = QtWidgets.QLabel(content)
        self.disc_cover.setGeometry(QtCore.QRect(30, 25, 200, 200))
        self.disc_cover.setText("")
        self.disc_cover.setPixmap(QtGui.QPixmap(":/images/cover.png"))
        self.disc_cover.setScaledContents(True)
        self.disc_cover.setObjectName("disc_cover")
        self.album_icon = QtWidgets.QLabel(content)
        self.album_icon.setGeometry(QtCore.QRect(270, 80, 30, 30))
        self.album_icon.setText("")
        self.album_icon.setPixmap(QtGui.QPixmap(":/images/disc.svg"))
        self.album_icon.setScaledContents(True)
        self.album_icon.setObjectName("album_icon")
        self.artist_icon = QtWidgets.QLabel(content)
        self.artist_icon.setGeometry(QtCore.QRect(270, 120, 30, 30))
        self.artist_icon.setText("")
        self.artist_icon.setPixmap(QtGui.QPixmap(":/images/artist.svg"))
        self.artist_icon.setScaledContents(True)
        self.artist_icon.setObjectName("artist_icon")
        self.title_icon = QtWidgets.QLabel(content)
        self.title_icon.setGeometry(QtCore.QRect(270, 40, 30, 30))
        self.title_icon.setText("")
        self.title_icon.setPixmap(QtGui.QPixmap(":/images/music.svg"))
        self.title_icon.setScaledContents(True)
        self.title_icon.setObjectName("title_icon")
        self.btn_play = QtWidgets.QLabel(content)
        self.btn_play.setGeometry(QtCore.QRect(410, 195, 50, 50))
        self.btn_play.setText("")
        self.btn_play.setPixmap(QtGui.QPixmap(":/images/play.svg"))
        self.btn_play.setScaledContents(True)
        self.btn_play.setObjectName("btn_play")
        self.btn_play.mouseReleaseEvent = self.playBtnPressed
        self.btn_last = QtWidgets.QLabel(content)
        self.btn_last.setGeometry(QtCore.QRect(340, 195, 50, 50))
        self.btn_last.setText("")
        self.btn_last.setPixmap(QtGui.QPixmap(":/images/last.svg"))
        self.btn_last.setScaledContents(True)
        self.btn_last.setObjectName("btn_last")
        self.btn_last.mouseReleaseEvent = self.rewindBtnPressed
        self.btn_next = QtWidgets.QLabel(content)
        self.btn_next.setGeometry(QtCore.QRect(480, 195, 50, 50))
        self.btn_next.setText("")
        self.btn_next.setPixmap(QtGui.QPixmap(":/images/next.svg"))
        self.btn_next.setScaledContents(True)
        self.btn_next.setObjectName("btn_next")
        self.btn_next.mouseReleaseEvent = self.nextBtnPressed
        self.label_music_pos = QtWidgets.QLabel(content)
        self.label_music_pos.setGeometry(QtCore.QRect(20, 280, 45, 15))
        font = QtGui.QFont()
        font.setFamily("Comfortaa")
        font.setPointSize(11)
        self.label_music_pos.setFont(font)
        self.label_music_pos.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_music_pos.setObjectName("label_music_pos")
        self.label_length = QtWidgets.QLabel(content)
        self.label_length.setGeometry(QtCore.QRect(595, 280, 47, 15))
        font = QtGui.QFont()
        font.setFamily("Comfortaa")
        font.setPointSize(11)
        self.label_length.setFont(font)
        self.label_length.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_length.setObjectName("label_length")
        self.label_artist = QtWidgets.QLabel(content)
        self.label_artist.setGeometry(QtCore.QRect(315, 120, 300, 30))
        font = QtGui.QFont()
        font.setFamily("Comfortaa")
        font.setPointSize(13)
        self.label_artist.setFont(font)
        self.label_artist.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_artist.setObjectName("label_artist")
        self.label_title = QtWidgets.QLabel(content)
        self.label_title.setGeometry(QtCore.QRect(315, 40, 300, 30))
        font = QtGui.QFont()
        font.setFamily("Comfortaa")
        font.setPointSize(13)
        self.label_title.setFont(font)
        self.label_title.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_title.setObjectName("label_title")
        self.label_album = QtWidgets.QLabel(content)
        self.label_album.setGeometry(QtCore.QRect(315, 80, 300, 30))
        font = QtGui.QFont()
        font.setFamily("Comfortaa")
        font.setPointSize(13)
        self.label_album.setFont(font)
        self.label_album.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_album.setObjectName("label_album")

        self.retranslateUi(content)
        QtCore.QMetaObject.connectSlotsByName(content)

        self.slider_pressed = False
        self.fetching_info = False
        self.current_offset = 0

    def retranslateUi(self, content):
        _translate = QtCore.QCoreApplication.translate
        content.setWindowTitle(_translate("content", "Form"))
        self.label_music_pos.setText(_translate("content", "0:00"))
        self.label_length.setText(_translate("content", "0:00"))
        self.label_artist.setText(_translate("content", ""))
        self.label_title.setText(_translate("content", ""))
        self.label_album.setText(_translate("content", ""))

    def updateUI(self):
        if self.slider_pressed or self.fetching_info:
            threading.Timer(0.1, self.updateUI).start()
            return

        self.fetching_info = True

        if self.owner.useBluetooth:
            try:
                props = self.player_prop_iface.GetAll("org.bluez.MediaPlayer1")
                if props["Status"] == "playing" or props["Status"] == "paused":
                    if props["Status"] == "playing":
                        self.btn_play.setPixmap(QtGui.QPixmap(":/images/pause.svg"))
                    else:
                        self.btn_play.setPixmap(QtGui.QPixmap(":/images/play.svg"))
                    track = props["Track"]
                    self.label_title.setText(track["Title"])
                    self.label_artist.setText(track["Artist"])
                    self.label_album.setText(track["Album"])

                    length = track["Duration"] / 1000.0
                    length_minutes = int(length / 60)
                    length_seconds = int(length - length_minutes * 60)
                    self.label_length.setText(str(length_minutes) + ":" + f"{length_seconds:02d}")

                    pos = props["Position"] / 1000.0
                    pos_minutes = int(pos / 60)
                    pos_seconds = int(pos - pos_minutes * 60)
                    self.label_music_pos.setText(str(pos_minutes) + ":" + f"{pos_seconds:02d}")

                    progress = (pos * 100) / length
                    self.music_slider.blockSignals(True)
                    self.music_slider.setValue(progress)
                    self.music_slider.blockSignals(False)

                else:
                    self.btn_play.setPixmap(QtGui.QPixmap(":/images/play.svg"))
                    self.label_title.setText("")
                    self.label_album.setText("")
                    self.label_artist.setText("")
                    self.label_music_pos.setText("0:00")
                    self.label_length.setText("0:00")
                    self.disc_cover.setPixmap(QtGui.QPixmap(":/images/cover.png"))
                    self.music_slider.blockSignals(True)
                    self.music_slider.setValue(0)
                    self.music_slider.blockSignals(False)
            except IndexError as e:
                print("Error retrieving bluetooth music info:")
                print(e)
        else:
            if mixer.music.get_busy():
                try:
                    id3 = EasyID3(self.owner.current_file)
                    self.label_title.setText(id3["title"][0])

                    try:
                        self.label_artist.setText(id3["artist"][0])
                    except:
                        self.label_artist.setText("-")
                    try:
                        self.label_album.setText(id3["album"][0])
                    except:
                        self.label_album.setText("-")

                except:
                    self.label_title.setText(os.path.basename(self.owner.current_file))
                    self.label_album.setText("-")
                    self.label_artist.setText("-")

                try:
                    file = File(self.owner.current_file)
                    artwork = file.tags['APIC:'].data
                    pixmap = QtGui.QPixmap()
                    pixmap.loadFromData(artwork)
                    self.disc_cover.setPixmap(pixmap)
                except:
                    self.disc_cover.setPixmap(QtGui.QPixmap(":/images/cover.png"))

                self.length_seconds = 0
                try:
                    mp3 = MP3(self.owner.current_file)
                    self.length_seconds = mp3.info.length
                    length_minutes = int(self.length_seconds / 60)
                    seconds = int(self.length_seconds - length_minutes * 60)
                    self.label_length.setText(str(length_minutes) + ":" + f"{seconds:02d}")
                except:
                    self.label_length.setText("")

                pos_seconds = self.current_offset + mixer.music.get_pos() / 1000
                pos_minutes = int(pos_seconds / 60)
                seconds = int(pos_seconds - pos_minutes * 60)
                self.label_music_pos.setText(str(pos_minutes) + ":" + f"{seconds:02d}")

                progress = (pos_seconds * 100) / self.length_seconds
                self.music_slider.blockSignals(True)
                self.music_slider.setValue(progress)
                self.music_slider.blockSignals(False)

            else:
                self.btn_play.setPixmap(QtGui.QPixmap(":/images/play.svg"))
                self.label_title.setText("")
                self.label_album.setText("")
                self.label_artist.setText("")
                self.label_music_pos.setText("0:00")
                self.label_length.setText("0:00")
                self.disc_cover.setPixmap(QtGui.QPixmap(":/images/cover.png"))
                self.music_slider.blockSignals(True)
                self.music_slider.setValue(0)
                self.music_slider.blockSignals(False)

        self.fetching_info = False
        threading.Timer(0.1, self.updateUI).start()

    def playBtnPressed(self, event):
        self.owner.pause()

    def nextBtnPressed(self, event):
        self.owner.next()

    def rewindBtnPressed(self, event):
        self.owner.rewind()

    def sliderPressed(self, event):
        self.slider_pressed = True

    def sliderChanged(self, event):
        self.slider_pressed = False
        if mixer.music.get_busy():
            progress = self.music_slider.value()
            current_pos = self.current_offset + mixer.music.get_pos() / 1000
            new_pos = self.length_seconds * progress / 100
            self.current_offset += new_pos - current_pos
            mixer.music.rewind()
            mixer.music.set_pos(new_pos)

    def setupBluetooth(self):
        import dbus, dbus.mainloop.glib, sys
        print("setting up bluetooth")
        dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)
        bus = dbus.SystemBus()
        obj = bus.get_object('org.bluez', "/")
        mgr = dbus.Interface(obj, 'org.freedesktop.DBus.ObjectManager')
        self.player_iface = None
        self.player_prop_iface = None
        for path, ifaces in mgr.GetManagedObjects().items():
            if 'org.bluez.MediaPlayer1' in ifaces:
                self.player_iface = dbus.Interface(
                    bus.get_object('org.bluez', path),
                    'org.bluez.MediaPlayer1')
                self.player_prop_iface = dbus.Interface(
                    bus.get_object('org.bluez', path),
                    'org.freedesktop.DBus.Properties')
        if not self.player_iface:
            sys.exit('Error: Media Player not found.')
