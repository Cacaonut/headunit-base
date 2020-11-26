# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'devices.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import threading
from sys import platform

if platform == "linux" or platform == "linux2":
    import bluetool
from PyQt5 import QtCore, QtGui, QtWidgets
import ui.lists.device


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
        self.btn_connected = QtWidgets.QWidget(content)
        self.btn_connected.setEnabled(False)
        self.btn_connected.setGeometry(QtCore.QRect(30, 30, 180, 45))
        self.btn_connected.setStyleSheet("#btn_connected {\n"
                                         "    background: #252525; color: white\n"
                                         "}\n"
                                         "\n"
                                         "#btn_connected::hover {\n"
                                         "    background: #303030;\n"
                                         "}\n"
                                         "\n"
                                         "#btn_connected::!enabled {\n"
                                         "    background: #595959;\n"
                                         "    border-bottom: 3px solid #E00000;\n"
                                         "}")
        self.btn_connected.setObjectName("btn_connected")
        self.btn_connected.mouseReleaseEvent = self.switchToConnected
        self.text_btn_connected = QtWidgets.QLabel(self.btn_connected)
        self.text_btn_connected.setGeometry(QtCore.QRect(20, 10, 140, 25))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(16)
        self.text_btn_connected.setFont(font)
        self.text_btn_connected.setLineWidth(1)
        self.text_btn_connected.setAlignment(QtCore.Qt.AlignCenter)
        self.text_btn_connected.setObjectName("text_btn_connected")
        self.btn_linked = QtWidgets.QWidget(content)
        self.btn_linked.setEnabled(True)
        self.btn_linked.setGeometry(QtCore.QRect(230, 30, 180, 45))
        self.btn_linked.setStyleSheet("#btn_linked {\n"
                                      "    background: #252525; color: white\n"
                                      "}\n"
                                      "\n"
                                      "#btn_linked::hover {\n"
                                      "    background: #303030;\n"
                                      "}\n"
                                      "\n"
                                      "#btn_linked::!enabled {\n"
                                      "    background: #595959;\n"
                                      "    border-bottom: 3px solid #E00000;\n"
                                      "}")
        self.btn_linked.setObjectName("btn_linked")
        self.btn_linked.mouseReleaseEvent = self.switchToLinked
        self.text_btn_linked = QtWidgets.QLabel(self.btn_linked)
        self.text_btn_linked.setGeometry(QtCore.QRect(20, 10, 140, 25))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(16)
        self.text_btn_linked.setFont(font)
        self.text_btn_linked.setLineWidth(1)
        self.text_btn_linked.setAlignment(QtCore.Qt.AlignCenter)
        self.text_btn_linked.setObjectName("text_btn_linked")
        self.btn_connect = QtWidgets.QWidget(content)
        self.btn_connect.setEnabled(True)
        self.btn_connect.setGeometry(QtCore.QRect(30, 365, 120, 35))
        self.btn_connect.setStyleSheet("#btn_connect {\n"
                                       "    background: #252525; color: white\n"
                                       "}\n"
                                       "\n"
                                       "#btn_connect::hover {\n"
                                       "    background: #303030;\n"
                                       "}\n"
                                       "\n"
                                       "#btn_connect::!enabled {\n"
                                       "    background: #595959;\n"
                                       "    border-bottom: 3px solid #E00000;\n"
                                       "}")
        self.btn_connect.setObjectName("btn_connect")
        self.text_btn_connect = QtWidgets.QLabel(self.btn_connect)
        self.text_btn_connect.setGeometry(QtCore.QRect(10, 5, 100, 25))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(14)
        self.text_btn_connect.setFont(font)
        self.text_btn_connect.setLineWidth(1)
        self.text_btn_connect.setAlignment(QtCore.Qt.AlignCenter)
        self.text_btn_connect.setObjectName("text_btn_connect")
        self.scrollArea = QtWidgets.QScrollArea(content)
        self.scrollArea.setGeometry(QtCore.QRect(30, 100, 660, 240))
        self.scrollArea.setStyleSheet("#scrollArea  {\n"
                                      "    border: none;\n"
                                      "    background: black\n"
                                      "}")
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 660, 240))
        self.scrollAreaWidgetContents.setStyleSheet("#scrollAreaWidgetContents {\n"
                                                    "    background: black\n"
                                                    "}")
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(-1, -1, 661, 241))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.timout_label = QtWidgets.QLabel(content)
        self.timout_label.setGeometry(QtCore.QRect(180, 370, 200, 25))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(12)
        self.timout_label.setFont(font)
        self.timout_label.setText("")
        self.timout_label.setObjectName("timout_label")

        self.retranslateUi(content)
        QtCore.QMetaObject.connectSlotsByName(content)

        self.current_tab_connected = True
        if platform == "linux" or platform == "linux2":
            self.setupBluetooth()
            self.updateDevices()

    def retranslateUi(self, content):
        _translate = QtCore.QCoreApplication.translate
        content.setWindowTitle(_translate("content", "Form"))
        self.text_btn_connected.setText(_translate("content", "Connected"))
        self.text_btn_linked.setText(_translate("content", "Linked"))
        self.text_btn_connect.setText(_translate("content", "Connect"))

    def switchToLinked(self, event):
        self.current_tab_connected = False
        self.updateDevices()
        self.btn_connected.setEnabled(True)
        self.btn_linked.setEnabled(False)

    def switchToConnected(self, event):
        self.current_tab_connected = True
        self.updateDevices()
        self.btn_connected.setEnabled(False)
        self.btn_linked.setEnabled(True)

    def setupBluetooth(self):
        self.bluetooth = bluetool.Bluetooth()
        self.bluetooth.make_discoverable()

    def updateDevices(self):
        for i in reversed(range(self.verticalLayout.count())):
            self.verticalLayout.itemAt(i).widget().setParent(None)

        if self.current_tab_connected:
            devices = self.bluetooth.get_connected_devices()
        else:
            devices = self.bluetooth.get_paired_devices()

        for device in devices:
            print(device)
            content_device = QtWidgets.QWidget()
            ui_device = ui.lists.device.Ui_widget()
            ui_device.setupUi(content_device)
            ui_device.label_name.setText(str(device["name"].decode("UTF-8")))
            self.verticalLayout.addWidget(content_device)

        self.scrollAreaWidgetContents.resize(660, len(devices) * 35)
