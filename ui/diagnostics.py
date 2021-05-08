# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'diagnostics.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import ui.lists.dtc

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
        self.label.setGeometry(QtCore.QRect(160, 120, 340, 60))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label.setVisible(True)
        self.container = QtWidgets.QWidget(content)
        self.container.setGeometry(QtCore.QRect(0, 0, 660, 281))
        self.container.setObjectName("container")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.container)
        self.verticalLayout.setSizeConstraint(
            QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.dtcs = [
            ("P0104", "Mass or Volume Air Flow Circuit Intermittent"),
            ("B0004", "PCM Discrete Input Speed Signal Not Present"),
            ("C0128", "Low Brake Fluid Circuit Low"),
            ("U0063", "Vehicle Communication Bus D (-) shorted to Bus D (+)")
        ]

        self.updateUI()

        self.retranslateUi(content)
        QtCore.QMetaObject.connectSlotsByName(content)

    def retranslateUi(self, content):
        _translate = QtCore.QCoreApplication.translate
        content.setWindowTitle(_translate("content", "Form"))
        self.label.setText(_translate("content", "No diagnostic trouble codes found."))

    def updateUI(self):
        if self.dtcs:
            self.label.setVisible(False)
            self.container.setVisible(True)

            for i in reversed(range(self.verticalLayout.count())):
                self.verticalLayout.itemAt(i).widget().setParent(None)

            for dtc in self.dtcs:
                content_dtc = QtWidgets.QWidget()
                ui_dtc = ui.lists.dtc.Ui_widget()
                ui_dtc.setupUi(content_dtc, self)
                ui_dtc.label_id.setText(dtc[0])
                ui_dtc.label_title.setText(dtc[1])
                self.verticalLayout.addWidget(content_dtc)

            self.container.setFixedHeight(self.verticalLayout.count() * 45)
        else:
            self.label.setVisible(True)
            self.container.setVisible(False)
