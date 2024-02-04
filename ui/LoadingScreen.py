from time import sleep
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(566, 331)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color: rgb(236, 234, 231);")
        MainWindow.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.logo_label = QtWidgets.QLabel(self.centralwidget)
        self.logo_label.setGeometry(QtCore.QRect(-80, 90, 641, 151))
        self.logo_label.setText("")
        self.logo_label.setPixmap(QtGui.QPixmap("../assets/logo/Logo.png"))
        self.logo_label.setScaledContents(False)
        self.logo_label.setObjectName("logo_label")
        self.version_label = QtWidgets.QLabel(self.centralwidget)
        self.version_label.setGeometry(QtCore.QRect(510, 310, 51, 20))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.version_label.setFont(font)
        self.version_label.setObjectName("version_label")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ScoreSheets"))
        self.version_label.setText(_translate("MainWindow", "Version 1.0"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    QtCore.QTimer.singleShot(2000, MainWindow.close)
    sys.exit(app.exec_())