import subprocess
subprocess.Popen(["sudo", "rfcomm", "connect", "hci0", "00:1D:A5:68:98:8B"]) # Connect obd2 adapter

from PyQt5 import QtCore, QtGui, QtWidgets
import ui.main


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = ui.main.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
