# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ui/caesar.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import os
os.environ ['QT_QPA_PLATFORM PLUGIN PATH'] ="../platforms"

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(180, 20, 281, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 100, 61, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(50, 220, 55, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(40, 350, 91, 31))
        self.label_4.setObjectName("label_4")
        self.txtplaintext = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.txtplaintext.setGeometry(QtCore.QRect(120, 100, 531, 91))
        self.txtplaintext.setObjectName("txtplaintext")
        self.txtkey = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.txtkey.setGeometry(QtCore.QRect(120, 220, 531, 51))
        self.txtkey.setObjectName("txtkey")
        self.txtcptext = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.txtcptext.setGeometry(QtCore.QRect(120, 340, 531, 91))
        self.txtcptext.setObjectName("txtcptext")
        self.btnen = QtWidgets.QPushButton(self.centralwidget)
        self.btnen.setGeometry(QtCore.QRect(120, 470, 93, 28))
        self.btnen.setObjectName("btnen")
        self.btnde = QtWidgets.QPushButton(self.centralwidget)
        self.btnde.setGeometry(QtCore.QRect(460, 470, 93, 28))
        self.btnde.setObjectName("btnde")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "CAESAR CIPHER"))
        self.label_2.setText(_translate("MainWindow", "Plain Text"))
        self.label_3.setText(_translate("MainWindow", "Key"))
        self.label_4.setText(_translate("MainWindow", "Cipher Text"))
        self.btnen.setText(_translate("MainWindow", "Encrypt"))
        self.btnde.setText(_translate("MainWindow", "Decrypt"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
