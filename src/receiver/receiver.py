# -*- coding: utf-8 -*-
from PyQt4 import QtGui, QtCore
import sys
import socket
import receiver_ui

class Receiver(QtGui.QMainWindow, receiver_ui.Ui_MainWindow):
    def __init__(self, parent=None ):
        super(Receiver, self).__init__(parent)
        self.setupUi(self)
        ##################################################
        # Variables
        ##################################################
        self.port = int(self.input_port.text())
        self.connected = False

        self.button_connect.clicked.connect(lambda: self.socket_init())

        if self.connected == False:
            self.input_port.setEnabled(True)
            self.button_connect.setText("Connect")
            self.console("STATUS: Disconnected")
        else:
            self.input_port.setEnabled(False)
            self.button_connect.setText("Disconnect")
            self.console("STATUS: Connected")
            self.getMessage()

    ##################################################
        # Functions
    ##################################################
    def console(self, text):
        item = QtGui.QListWidgetItem()
        item.setText(text)
        item.setFlags(QtCore.Qt.NoItemFlags)
        self.display_console.addItem(item)
        
    def cleanConsole(self):
        self.display_console.clear()

    def message(self, text):
        item = QtGui.QListWidgetItem()
        item.setText(text)
        item.setFlags(QtCore.Qt.NoItemFlags)
        self.display_message.addItem(item)
        
    def cleanMessage(self):
        self.display_message.clear()

    def socket_init(self):
        if self.connected == True:
            self.sock.close()
            self.connected = False
        else:
            self.console("Initializing socket TCP/IP")
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.server_address = ('localhost', self.port)
            self.console("Port {}".format(self.port))
            self.sock.bind(self.server_address)

            # Listen for incoming connections
            self.sock.listen(1)
            while True:
                self.console("Waiting for a connection...")
                self.connection, self.client_address = self.sock.accept()
                self.console("Connection from {}".format(self.client_address))
                if(self.connection.accept):
                    break
            self.connected = True

    def getMessage(self):
        while True:
            data = self.connection.recv(32)
            message = data.decode("utf-8")
            print("{}".format(message))
            self.message(message)

            if(len(data) <= 0):
                break
        self.sock.close()
        self.connected = False

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = Receiver()
    window.show()
    app.exec_()
