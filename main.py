import os
import bluetool

from PyQt5 import QtCore, QtGui, QtWidgets
import ui.main


def setupBluetooth():
    bt = bluetool.Bluetooth()
    print(bt.get_paired_devices())


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = ui.main.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    setupBluetooth()
    sys.exit(app.exec_())
