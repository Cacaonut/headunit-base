from PyQt5 import QtCore, QtGui, QtWidgets
import os


class Ui_content(object):
    def setupUi(self, content):
        content.setObjectName("content")
        content.resize(300, 200)
        content.setStyleSheet("#content {\n"
                              "    background: #151515\n"
                              "}\n"
                              "\n"
                              "* {\n"
                              "    color: white\n"
                              "}")
        self.button_shutdown = QtWidgets.QWidget(content)
        self.button_shutdown.setGeometry(QtCore.QRect(50, 15, 200, 80))
        self.button_shutdown.setStyleSheet("background: #262626")
        self.button_shutdown.setObjectName("button_shutdown")
        self.button_shutdown.mouseReleaseEvent = self.shutdown
        self.label_shutdown = QtWidgets.QLabel(self.button_shutdown)
        self.label_shutdown.setGeometry(QtCore.QRect(25, 40, 160, 30))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(16)
        self.label_shutdown.setFont(font)
        self.label_shutdown.setAlignment(QtCore.Qt.AlignCenter)
        self.label_shutdown.setObjectName("label_shutdown")
        self.label_shutdown.setText("Shutdown")

        self.button_reboot = QtWidgets.QWidget(content)
        self.button_reboot.setGeometry(QtCore.QRect(105, 15, 200, 80))
        self.button_reboot.setStyleSheet("background: #262626")
        self.button_reboot.setObjectName("button_reboot")
        self.button_reboot.mouseReleaseEvent = self.reboot
        self.label_reboot = QtWidgets.QLabel(self.button_reboot)
        self.label_reboot.setGeometry(QtCore.QRect(25, 40, 160, 30))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(16)
        self.label_reboot.setFont(font)
        self.label_reboot.setAlignment(QtCore.Qt.AlignCenter)
        self.label_reboot.setObjectName("label_reboot")
        self.label_reboot.setText("Reboot")

        QtCore.QMetaObject.connectSlotsByName(content)
    
    def shutdown(self, event):
        os.system("shutdown now")

    def reboot(self, event):
        os.system("reboot")
