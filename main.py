from PyQt5 import QtCore, QtGui, QtWidgets
import ui.main


def setupBluetooth():
    import bluetooth

    server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)

    port = 1
    server_sock.bind(("", port))
    server_sock.listen(1)
    bluetooth.advertise_service(server_sock, "Toyota RAV 4")

    client_sock, address = server_sock.accept()
    client_name = bluetooth.lookup_name(address)
    print("Connected to " + client_name + "(" + address + ")")


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = ui.main.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    # setupBluetooth()
    sys.exit(app.exec_())
