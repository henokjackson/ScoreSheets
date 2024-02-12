from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(449, 137)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../assets/misc/info.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.file_name_label_3 = QtWidgets.QLabel(Dialog)
        self.file_name_label_3.setGeometry(QtCore.QRect(120, 40, 311, 17))
        self.file_name_label_3.setObjectName("file_name_label_3")
        self.file_name_label_2 = QtWidgets.QLabel(Dialog)
        self.file_name_label_2.setGeometry(QtCore.QRect(120, 20, 311, 20))
        self.file_name_label_2.setObjectName("file_name_label_2")
        self.file_name_label = QtWidgets.QLabel(Dialog)
        self.file_name_label.setGeometry(QtCore.QRect(40, 20, 81, 17))
        self.file_name_label.setObjectName("file_name_label")
        self.abort_pushButton = QtWidgets.QPushButton(Dialog)
        self.abort_pushButton.setGeometry(QtCore.QRect(190, 100, 71, 25))
        self.abort_pushButton.setObjectName("abort_pushButton")
        self.file_no_label = QtWidgets.QLabel(Dialog)
        self.file_no_label.setGeometry(QtCore.QRect(40, 40, 71, 17))
        self.file_no_label.setObjectName("file_no_label")
        self.process_progressBar = QtWidgets.QProgressBar(Dialog)
        self.process_progressBar.setGeometry(QtCore.QRect(10, 70, 431, 16))
        self.process_progressBar.setProperty("value", 24)
        self.process_progressBar.setObjectName("process_progressBar")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Processing"))
        self.file_name_label_3.setText(_translate("Dialog", "1"))
        self.file_name_label_2.setText(_translate("Dialog", "Sample.pdf"))
        self.file_name_label.setText(_translate("Dialog", "File Name :"))
        self.abort_pushButton.setText(_translate("Dialog", "Abort"))
        self.file_no_label.setText(_translate("Dialog", "File No.  :"))

def Start():
    dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(dialog)
    dialog.setWindowModality(QtCore.Qt.ApplicationModal)
    dialog.show()
    dialog.exec_()