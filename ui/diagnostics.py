# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'diagnostics.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_content(object):
    def setupUi(self, content):
        content.setObjectName("content")
        content.resize(660, 300)
        content.setStyleSheet("#content {\n"
                              "    background: black\n"
                              "}\n"
                              "\n"
                              "* {\n"
                              "    color: white\n"
                              "}")
        self.label = QtWidgets.QLabel(content)
        self.label.setGeometry(QtCore.QRect(260, 120, 140, 60))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.retranslateUi(content)
        QtCore.QMetaObject.connectSlotsByName(content)

    def retranslateUi(self, content):
        _translate = QtCore.QCoreApplication.translate
        content.setWindowTitle(_translate("content", "Form"))
        self.label.setText(_translate("content", "Diagnostics"))
