# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'media_file_browser.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import os
import ui.lists.file
import ui.lists.folder
from mutagen.mp3 import MP3
from mutagen.easyid3 import EasyID3
from sys import platform


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
        self.btn_play = QtWidgets.QWidget(content)
        self.btn_play.setEnabled(True)
        self.btn_play.setGeometry(QtCore.QRect(0, 265, 120, 35))
        self.btn_play.setStyleSheet("#btn_play {\n"
                                    "    background: #252525; color: white\n"
                                    "}\n"
                                    "\n"
                                    "#btn_play::hover {\n"
                                    "    background: #303030;\n"
                                    "}\n"
                                    "\n"
                                    "#btn_play::!enabled {\n"
                                    "    background: #595959;\n"
                                    "    border-bottom: 3px solid #E00000;\n"
                                    "}")
        self.btn_play.setObjectName("btn_play")
        self.text_btn_play = QtWidgets.QLabel(self.btn_play)
        self.text_btn_play.setGeometry(QtCore.QRect(10, 5, 100, 25))
        font = QtGui.QFont()
        font.setFamily("Montserrat Light")
        font.setPointSize(14)
        self.text_btn_play.setFont(font)
        self.text_btn_play.setLineWidth(1)
        self.text_btn_play.setAlignment(QtCore.Qt.AlignCenter)
        self.text_btn_play.setObjectName("text_btn_play")
        self.btn_shuffle = QtWidgets.QWidget(content)
        self.btn_shuffle.setEnabled(True)
        self.btn_shuffle.setGeometry(QtCore.QRect(135, 265, 120, 35))
        self.btn_shuffle.setStyleSheet("#btn_shuffle {\n"
                                       "    background: #252525; color: white\n"
                                       "}\n"
                                       "\n"
                                       "#btn_shuffle::hover {\n"
                                       "    background: #303030;\n"
                                       "}\n"
                                       "\n"
                                       "#btn_shuffle::!enabled {\n"
                                       "    background: #595959;\n"
                                       "    border-bottom: 3px solid #E00000;\n"
                                       "}")
        self.btn_shuffle.setObjectName("btn_shuffle")
        self.text_btn_shuffle = QtWidgets.QLabel(self.btn_shuffle)
        self.text_btn_shuffle.setGeometry(QtCore.QRect(10, 5, 100, 25))
        font = QtGui.QFont()
        font.setFamily("Montserrat Light")
        font.setPointSize(14)
        self.text_btn_shuffle.setFont(font)
        self.text_btn_shuffle.setLineWidth(1)
        self.text_btn_shuffle.setAlignment(QtCore.Qt.AlignCenter)
        self.text_btn_shuffle.setObjectName("text_btn_shuffle")
        self.scrollArea = QtWidgets.QScrollArea(content)
        self.scrollArea.setGeometry(QtCore.QRect(0, 60, 660, 190))
        self.scrollArea.setStyleSheet("#scrollArea  {\n"
                                      "    border: none;\n"
                                      "    background: black\n"
                                      "}")
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setObjectName("scrollArea")
        scroller = QtWidgets.QScroller.scroller(self.scrollArea.viewport())
        scroller.grabGesture(self.scrollArea, QtWidgets.QScroller.TouchGesture)
        scrollerProps = scroller.scrollerProperties()
        scrollerProps.setScrollMetric(QtWidgets.QScrollerProperties.HorizontalOvershootPolicy,
                                      QtWidgets.QScrollerProperties.OvershootAlwaysOff)
        scrollerProps.setScrollMetric(QtWidgets.QScrollerProperties.VerticalOvershootPolicy,
                                      QtWidgets.QScrollerProperties.OvershootAlwaysOff)
        scroller.setScrollerProperties(scrollerProps)
        self.scrollAreaWidget = QtWidgets.QFrame()
        self.scrollAreaWidget.setStyleSheet("#scrollAreaWidget {\n"
                                            "    background: black;\n"
                                            "}")
        self.scrollAreaWidget.setObjectName("scrollAreaWidget")
        self.scrollAreaLayout = QtWidgets.QVBoxLayout()
        self.scrollAreaWidget.setLayout(self.scrollAreaLayout)
        self.scrollArea.setWidget(self.scrollAreaWidget)
        self.btn_back = QtWidgets.QWidget(content)
        self.btn_back.setEnabled(True)
        self.btn_back.setGeometry(QtCore.QRect(10, 10, 30, 30))
        self.btn_back.setStyleSheet("#btn_back {\n"
                                    "    background: #252525; color: white\n"
                                    "}\n"
                                    "\n"
                                    "#btn_back::hover {\n"
                                    "    background: #303030;\n"
                                    "}\n"
                                    "\n"
                                    "#btn_back::!enabled {\n"
                                    "    background: #595959;\n"
                                    "    border-bottom: 3px solid #E00000;\n"
                                    "}")
        self.btn_back.setObjectName("btn_back")
        self.btn_back.mouseReleaseEvent = self.toParentDir
        self.label_btn_back = QtWidgets.QLabel(self.btn_back)
        self.label_btn_back.setGeometry(QtCore.QRect(2, 2, 26, 26))
        self.label_btn_back.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_btn_back.setStyleSheet("")
        self.label_btn_back.setText("")
        self.label_btn_back.setPixmap(QtGui.QPixmap(":/images/back.png"))
        self.label_btn_back.setScaledContents(True)
        self.label_btn_back.setObjectName("label_btn_back")
        self.label_path = QtWidgets.QLabel(content)
        self.label_path.setGeometry(QtCore.QRect(70, 10, 500, 30))
        font = QtGui.QFont()
        font.setFamily("Montserrat Light")
        font.setPointSize(16)
        self.label_path.setFont(font)
        self.label_path.setObjectName("label_path")

        # Search for files and directories
        self.retranslateUi(content)
        if platform == "linux" or platform == "linux2":
            self.current_path = "/home/pi"
        else:
            self.current_path = "D:\\"
        self.updateFiles()
        QtCore.QMetaObject.connectSlotsByName(content)

    def retranslateUi(self, content):
        _translate = QtCore.QCoreApplication.translate
        content.setWindowTitle(_translate("content", "Form"))
        self.text_btn_play.setText(_translate("content", "Play"))
        self.text_btn_shuffle.setText(_translate("content", "Shuffle"))
        self.label_path.setText(_translate("content", "path/to/current/directory"))

    def updateFiles(self):
        for i in reversed(range(self.scrollAreaLayout.count())):
            self.scrollAreaLayout.itemAt(i).widget().setParent(None)
        dirs = []
        files = []
        audio_files = [".mp3"]

        for item in os.listdir(self.current_path):
            if os.path.isfile(os.path.join(self.current_path, item)):
                filename, file_extension = os.path.splitext(item)
                if file_extension in audio_files:
                    files.append(item)
            else:
                dirs.append(item)

        for directory in dirs:
            content_dir = QtWidgets.QWidget()
            ui_dir = ui.lists.folder.Ui_widget()
            ui_dir.setupUi(content_dir, self)
            ui_dir.label_title.setText(directory)
            self.scrollAreaLayout.addWidget(content_dir)

        i = 0
        for file in files:
            i += 1
            content_file = QtWidgets.QWidget()
            ui_file = ui.lists.file.Ui_widget()
            ui_file.setupUi(content_file, self, file, self.owner)
            filename, file_extension = os.path.splitext(file)
            ui_file.label_number.setText(str(i))
            mp3 = MP3(os.path.join(self.current_path, file))
            id3 = EasyID3(os.path.join(self.current_path, file))
            ui_file.label_title.setText(id3["title"][0])
            minutes = int(mp3.info.length / 60)
            if minutes > 0:
                seconds = int(mp3.info.length - minutes * 60)
            else:
                seconds = int(mp3.info.length)
            print(str(minutes) + ":" + str(seconds))
            ui_file.label_length.setText(str(minutes) + ":" + f"{seconds:02d}")
            self.scrollAreaLayout.addWidget(content_file)

        self.scrollAreaWidget.resize(660, (len(dirs) + len(files)) * 47)
        self.label_path.setText(self.current_path)

    def toParentDir(self, event):
        self.changePath(os.path.dirname(self.current_path))

    def changePath(self, path):
        print(path)
        self.current_path = path
        self.updateFiles()
