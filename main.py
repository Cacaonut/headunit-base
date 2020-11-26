import os
import bluetool

from PyQt5 import QtCore, QtGui, QtWidgets
import ui.main


def setupBluetooth():
    bt = bluetool.Bluetooth()
    bt.make_discoverable()
    print("-----------------------")
    print("PAIRED DEVICES")
    print(bt.get_paired_devices())
    print("-----------------------")


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = ui.main.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    setupBluetooth()
    sys.exit(app.exec_())
