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
        self.checkStatus()

    def checkStatus(self):
        if self.connected == False:
            self.input_port.setEnabled(True)
            self.button_connect.setText("Connect")
            self.console("STATUS: Disconnected")
        else:
            self.input_port.setEnabled(False)
            self.button_connect.setText("Disconnect")
            self.console("STATUS: Connected")

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
        self.display_message.addItem(item)
        
    def cleanChat(self):
        self.display_message.clear()

    def socket_init(self):
        if self.connected == True:
            self.sock.close()
            self.connected = False
        else:
            self.console("Initializing socket TCP/IP")
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server_address = ('localhost', self.port)
            self.console("Port {}".format(self.port))
            sock.bind(server_address)

            # Listen for incoming connections
            sock.listen(1)

            while True:
                self.console("Waiting for a connection...")
                self.connection, self.client_address = sock.accept()
                self.console("Connection from {}".format(client_address))
                self.connected = True
    
    def getMessage(self):
        try:
            print(" connection from {}".format(client_address))

            # Receive the data in small chunks and retransmit it
            while True:
                data = self.connection.recv(16)
                print("{}".format(data))
                if(len(data) <= 0):
                    break
        except:
            print('Erro')
            self.getMessage()

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = Receiver()
    window.show()
    app.exec_()
