# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Workspace.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(710, 600)
        MainWindow.setStyleSheet("background-color: rgb(236, 234, 231);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Logo = QtWidgets.QLabel(self.centralwidget)
        self.Logo.setGeometry(QtCore.QRect(-10, 0, 811, 151))
        self.Logo.setText("")
        self.Logo.setPixmap(QtGui.QPixmap("../Assets/Logo/Logo.png"))
        self.Logo.setObjectName("Logo")
        self.Version = QtWidgets.QLabel(self.centralwidget)
        self.Version.setGeometry(QtCore.QRect(700, 580, 41, 16))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(7)
        font.setBold(False)
        font.setWeight(50)
        self.Version.setFont(font)
        self.Version.setStyleSheet("color: rgb(255, 255, 255);")
        self.Version.setObjectName("Version")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Version.setText(_translate("MainWindow", "Version 1.0"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
