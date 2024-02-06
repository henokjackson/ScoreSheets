import sys
from PyQt5 import QtCore, QtGui, QtWidgets

# Loading Messages Index
index = 0

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Form.setObjectName("Form")
        Form.setFixedSize(537, 265)
        Form.setWindowTitle("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../assets/logo/Icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setStyleSheet("background-color: rgb(236, 234, 231);")
        self.logo_label = QtWidgets.QLabel(Form)
        self.logo_label.setGeometry(QtCore.QRect(-100, 60, 701, 151))
        self.logo_label.setText("")
        self.logo_label.setPixmap(QtGui.QPixmap("../assets/logo/Logo.png"))
        self.logo_label.setObjectName("logo_label")
        self.version_label = QtWidgets.QLabel(Form)
        self.version_label.setGeometry(QtCore.QRect(470, 240, 61, 17))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.version_label.setFont(font)
        self.version_label.setObjectName("version_label")
        self.loading_label = QtWidgets.QLabel(Form)
        self.loading_label.setGeometry(QtCore.QRect(10, 240, 191, 17))
        self.loading_label.setFont(font)
        self.loading_label.setObjectName("loading_label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        self.version_label.setText(_translate("Form", "Version 1.0"))

def Loading():
    global index
    loadingOptions = ["Loading assets...", "Loading coniguration...", "Setting up workspace...", "Clearing up cache...", ]
    
    if index < len(loadingOptions):
        ui.loading_label.setText(loadingOptions[index])
        index = index + 1
    else:
        timer.stop()
        Form.close()
        return

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()

    # Load Message Updater
    timer = QtCore.QTimer()
    timer.timeout.connect(Loading)
    timer.start(400)

    sys.exit(app.exec_())