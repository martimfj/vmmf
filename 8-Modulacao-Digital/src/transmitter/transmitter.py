# -*- coding: utf-8 -*-
from PyQt4 import QtGui, QtCore
import sys
import socket
import transmitter_ui

class Transmitter(QtGui.QMainWindow, transmitter_ui.Ui_MainWindow):
    def __init__(self, parent=None ):
        super(Transmitter, self).__init__(parent)
        self.setupUi(self)
        ##################################################
        # Variables
        ##################################################
        self.port = int(self.input_port.text())
        self.connected = False
        self.message = None

        self.button_connect.clicked.connect(lambda: self.socket_init())
        self.button_send.clicked.connect(lambda: self.sendMessage())

    def checkStatus(self):
        if self.connected == False:
            self.input_port.setEnabled(True)
            self.button_connect.setText("Connect")
            self.console("STATUS: Disconnected")
        else:
            self.input_port.setEnabled(False)
            self.button_connect.setText("Disconnect")
            self.console("STATUS: Connected")

        self.input_port.textChanged.connect(lambda: self.updatePort())

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

    def chat(self, text):
        item = QtGui.QListWidgetItem()
        item.setText(text)
        item.setFlags(QtCore.Qt.NoItemFlags)
        self.display_content.addItem(item)
        
    def cleanChat(self):
        self.display_content.clear()

    def socket_init(self):
        if self.connected == True:
            self.sock.close()
            self.connected = False
        else:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            # Connect the socket to the port where the server is listening
            self.server_address = ('localhost', self.port)
            self.console("Connecting to {} on port {}".format(*self.server_address))
            self.sock.connect(self.server_address)
            self.connected = True
            self.checkStatus()

    def sendMessage(self):
        if self.connected == False:
            self.console("Connection isn't established")
        else:
            self.message = self.input_message.text()
            self.chat(self.message)
            x = str(self.message)
            data = x.encode()
            self.sock.send(data)
            self.console("Sending message encoded as {}".format(data))
            #self.sock.sendall(data)
            self.input_message.setText("")

    def updatePort(self):
        self.port = int(self.input_port.text())

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = Transmitter()
    window.show()
    app.exec_()
