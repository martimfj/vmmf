# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'transmitter_ui.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        font = QtGui.QFont()
        font.setPointSize(8)
        MainWindow.setFont(font)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.display_content = QtGui.QListWidget(self.centralwidget)
        self.display_content.setGeometry(QtCore.QRect(15, 70, 375, 465))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.display_content.sizePolicy().hasHeightForWidth())
        self.display_content.setSizePolicy(sizePolicy)
        self.display_content.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);\n"
"font: 16pt \"Consolas\";\n"
"selection-background-color: rgb(0, 0, 0);\n"
"selection-color: rgb(0, 0, 0);\n"
"font: 12pt \"Consolas\";\n"
"color: rgb(0, 255, 0);"))
        self.display_content.setFrameShape(QtGui.QFrame.NoFrame)
        self.display_content.setFrameShadow(QtGui.QFrame.Plain)
        self.display_content.setLineWidth(0)
        self.display_content.setAutoScrollMargin(50)
        self.display_content.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.display_content.setProperty("showDropIndicator", False)
        self.display_content.setAlternatingRowColors(False)
        self.display_content.setSelectionMode(QtGui.QAbstractItemView.NoSelection)
        self.display_content.setSelectionBehavior(QtGui.QAbstractItemView.SelectItems)
        self.display_content.setTextElideMode(QtCore.Qt.ElideNone)
        self.display_content.setVerticalScrollMode(QtGui.QAbstractItemView.ScrollPerItem)
        self.display_content.setFlow(QtGui.QListView.TopToBottom)
        self.display_content.setProperty("isWrapping", False)
        self.display_content.setResizeMode(QtGui.QListView.Adjust)
        self.display_content.setLayoutMode(QtGui.QListView.Batched)
        self.display_content.setViewMode(QtGui.QListView.ListMode)
        self.display_content.setModelColumn(0)
        self.display_content.setUniformItemSizes(True)
        self.display_content.setObjectName(_fromUtf8("display_content"))
        self.display_console = QtGui.QListWidget(self.centralwidget)
        self.display_console.setGeometry(QtCore.QRect(410, 70, 375, 465))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.display_console.sizePolicy().hasHeightForWidth())
        self.display_console.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Consolas"))
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.display_console.setFont(font)
        self.display_console.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);\n"
"selection-background-color: rgb(0, 0, 0);\n"
"selection-color: rgb(0, 0, 0);\n"
"font: 12pt \"Consolas\";\n"
"color: rgb(0, 255, 0);"))
        self.display_console.setFrameShape(QtGui.QFrame.NoFrame)
        self.display_console.setFrameShadow(QtGui.QFrame.Plain)
        self.display_console.setLineWidth(0)
        self.display_console.setAutoScrollMargin(50)
        self.display_console.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.display_console.setProperty("showDropIndicator", False)
        self.display_console.setAlternatingRowColors(False)
        self.display_console.setSelectionMode(QtGui.QAbstractItemView.NoSelection)
        self.display_console.setSelectionBehavior(QtGui.QAbstractItemView.SelectItems)
        self.display_console.setTextElideMode(QtCore.Qt.ElideNone)
        self.display_console.setVerticalScrollMode(QtGui.QAbstractItemView.ScrollPerItem)
        self.display_console.setFlow(QtGui.QListView.TopToBottom)
        self.display_console.setProperty("isWrapping", False)
        self.display_console.setResizeMode(QtGui.QListView.Adjust)
        self.display_console.setLayoutMode(QtGui.QListView.Batched)
        self.display_console.setViewMode(QtGui.QListView.ListMode)
        self.display_console.setModelColumn(0)
        self.display_console.setUniformItemSizes(True)
        self.display_console.setObjectName(_fromUtf8("display_console"))
        self.input_message = QtGui.QLineEdit(self.centralwidget)
        self.input_message.setGeometry(QtCore.QRect(15, 550, 325, 35))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.input_message.sizePolicy().hasHeightForWidth())
        self.input_message.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Consolas"))
        font.setPointSize(16)
        self.input_message.setFont(font)
        self.input_message.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);\n"
"color: rgb(0, 255, 0);"))
        self.input_message.setMaxLength(100)
        self.input_message.setFrame(False)
        self.input_message.setCursorPosition(0)
        self.input_message.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.input_message.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.input_message.setObjectName(_fromUtf8("input_message"))
        self.bg_window = QtGui.QLabel(self.centralwidget)
        self.bg_window.setEnabled(True)
        self.bg_window.setGeometry(QtCore.QRect(0, 0, 800, 600))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bg_window.sizePolicy().hasHeightForWidth())
        self.bg_window.setSizePolicy(sizePolicy)
        self.bg_window.setMinimumSize(QtCore.QSize(800, 600))
        self.bg_window.setMaximumSize(QtCore.QSize(800, 600))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Open Sans"))
        self.bg_window.setFont(font)
        self.bg_window.setText(_fromUtf8(""))
        self.bg_window.setPixmap(QtGui.QPixmap(_fromUtf8("transmitter_bg.png")))
        self.bg_window.setObjectName(_fromUtf8("bg_window"))
        self.button_send = QtGui.QPushButton(self.centralwidget)
        self.button_send.setGeometry(QtCore.QRect(355, 550, 35, 35))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_send.sizePolicy().hasHeightForWidth())
        self.button_send.setSizePolicy(sizePolicy)
        self.button_send.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);\n"
"color: rgb(0, 255, 0);"))
        self.button_send.setObjectName(_fromUtf8("button_send"))
        self.input_port = QtGui.QLineEdit(self.centralwidget)
        self.input_port.setGeometry(QtCore.QRect(410, 550, 245, 35))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.input_port.sizePolicy().hasHeightForWidth())
        self.input_port.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Consolas"))
        font.setPointSize(22)
        self.input_port.setFont(font)
        self.input_port.setInputMethodHints(QtCore.Qt.ImhNone)
        self.input_port.setInputMask(_fromUtf8(""))
        self.input_port.setText(_fromUtf8("1234"))
        self.input_port.setMaxLength(5)
        self.input_port.setAlignment(QtCore.Qt.AlignCenter)
        self.input_port.setObjectName(_fromUtf8("input_port"))
        self.button_connect = QtGui.QPushButton(self.centralwidget)
        self.button_connect.setGeometry(QtCore.QRect(670, 550, 115, 35))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_connect.sizePolicy().hasHeightForWidth())
        self.button_connect.setSizePolicy(sizePolicy)
        self.button_connect.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);\n"
"color: rgb(0, 255, 0);"))
        self.button_connect.setObjectName(_fromUtf8("button_connect"))
        self.bg_window.raise_()
        self.display_console.raise_()
        self.display_content.raise_()
        self.input_message.raise_()
        self.button_send.raise_()
        self.input_port.raise_()
        self.button_connect.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Transmitter", None))
        self.button_send.setText(_translate("MainWindow", "Send", None))
        self.input_port.setPlaceholderText(_translate("MainWindow", "Port", None))
        self.button_connect.setText(_translate("MainWindow", "Connect", None))

