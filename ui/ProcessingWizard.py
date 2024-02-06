import sys
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setWindowFlag(QtCore.Qt.WindowCloseButtonHint, False)
        Form.setObjectName("Form")
        Form.setFixedSize(453, 134)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../assets/logo/Icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setStyleSheet("background-color: rgb(236, 234, 231);")
        self.process_progressBar = QtWidgets.QProgressBar(Form)
        self.process_progressBar.setGeometry(QtCore.QRect(10, 70, 431, 16))
        self.process_progressBar.setProperty("value", 24)
        self.process_progressBar.setObjectName("process_progressBar")
        self.abort_pushButton = QtWidgets.QPushButton(Form)
        self.abort_pushButton.setGeometry(QtCore.QRect(190, 100, 71, 25))
        self.abort_pushButton.setObjectName("abort_pushButton")
        self.file_name_label = QtWidgets.QLabel(Form)
        self.file_name_label.setGeometry(QtCore.QRect(40, 20, 81, 17))
        self.file_name_label.setObjectName("file_name_label")
        self.file_no_label = QtWidgets.QLabel(Form)
        self.file_no_label.setGeometry(QtCore.QRect(40, 40, 71, 17))
        self.file_no_label.setObjectName("file_no_label")
        self.file_name_label_2 = QtWidgets.QLabel(Form)
        self.file_name_label_2.setGeometry(QtCore.QRect(120, 20, 311, 20))
        self.file_name_label_2.setObjectName("file_name_label_2")
        self.file_name_label_3 = QtWidgets.QLabel(Form)
        self.file_name_label_3.setGeometry(QtCore.QRect(120, 40, 311, 17))
        self.file_name_label_3.setObjectName("file_name_label_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Processing"))
        self.abort_pushButton.setText(_translate("Form", "Abort"))
        self.file_name_label.setText(_translate("Form", "File Name :"))
        self.file_no_label.setText(_translate("Form", "File No.  :"))
        self.file_name_label_2.setText(_translate("Form", "Sample.pdf"))
        self.file_name_label_3.setText(_translate("Form", "1"))
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())