# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'folder.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import os

from PyQt5 import QtCore, QtGui, QtWidgets
import ui.media_file_browser as media_file_browser


class Ui_widget(object):
    def setupUi(self, widget, owner):
        widget.setObjectName("widget")
        widget.resize(600, 45)
        widget.setStyleSheet("#widget {\n"
                             "    background: black;\n"
                             "    border-bottom: 1px solid #CCC\n"
                             "}\n"
                             "\n"
                             "* {\n"
                             "    color: white\n"
                             "}")
        self.label_id = QtWidgets.QLabel(widget)
        self.label_id.setGeometry(QtCore.QRect(10, 10, 25, 25))
        font = QtGui.QFont()
        font.setFamily("Montserrat Light")
        font.setPointSize(13)
        self.label_id.setFont(font)
        self.label_id.setStyleSheet("color: #CCC")
        self.label_id.setAlignment(QtCore.Qt.AlignCenter)
        self.label_id.setObjectName("label_id")
        self.label_title = QtWidgets.QLabel(widget)
        self.label_title.setGeometry(QtCore.QRect(100, 10, 300, 25))
        font = QtGui.QFont()
        font.setFamily("Montserrat Light")
        font.setPointSize(13)
        self.label_title.setFont(font)
        self.label_title.setStyleSheet("")
        self.label_title.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_title.setObjectName("label_title")

        QtCore.QMetaObject.connectSlotsByName(widget)
