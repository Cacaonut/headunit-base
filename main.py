from PyQt5 import QtCore, QtGui, QtWidgets
import ui.main


if __name__ == "__main__":
    import sys
    import gi
    gi.require_version('Wnck', '3.0')
    from gi.repository import Wnck

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = ui.main.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
