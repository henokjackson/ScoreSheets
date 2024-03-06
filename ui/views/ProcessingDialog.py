from PyQt5 import QtCore, QtGui, QtWidgets
from ui.controllers import ProcessingDialogController

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(449, 137)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../assets/misc/info.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.WindowTitleHint | QtCore.Qt.CustomizeWindowHint)
        self.fileno_label = QtWidgets.QLabel(Dialog)
        self.fileno_label.setGeometry(QtCore.QRect(120, 40, 311, 17))
        self.fileno_label.setObjectName("fileno_label")
        self.filename_label = QtWidgets.QLabel(Dialog)
        self.filename_label.setGeometry(QtCore.QRect(120, 20, 311, 20))
        self.filename_label.setObjectName("filename_label")
        self.file_name_label = QtWidgets.QLabel(Dialog)
        self.file_name_label.setGeometry(QtCore.QRect(40, 20, 81, 17))
        self.file_name_label.setObjectName("file_name_label")
        self.abort_pushButton = QtWidgets.QPushButton(Dialog)
        self.abort_pushButton.setGeometry(QtCore.QRect(190, 100, 71, 25))
        self.abort_pushButton.setObjectName("abort_pushButton")
        self.abort_pushButton.clicked.connect(lambda: ProcessingDialogController.Abort());
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
        self.fileno_label.setText(_translate("Dialog", "1"))
        self.filename_label.setText(_translate("Dialog", "Sample.pdf"))
        self.file_name_label.setText(_translate("Dialog", "File Name :"))
        self.abort_pushButton.setText(_translate("Dialog", "Abort"))
        self.file_no_label.setText(_translate("Dialog", "File No.  :"))

    def mainProcessesCompletedMessage():
        mainProcessesCompletedMessageBox = QtWidgets.QMessageBox()
        mainProcessesCompletedMessageBox.setIcon(QtWidgets.QMessageBox.Information)
        mainProcessesCompletedMessageBox.setText("Score Calculation Completed.")
        mainProcessesCompletedMessageBox.setWindowTitle("Info")
        mainProcessesCompletedMessageBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        mainProcessesCompletedMessageBox.exec_()

def Render():
    dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(dialog)
    dialog.setWindowModality(QtCore.Qt.ApplicationModal)
    dialog.show()

    # Timer For Refreshing Progress Bar
    timer = QtCore.QTimer()
    timer.timeout.connect(lambda: ProcessingDialogController.RefreshProgressBar(ui, timer, dialog))
    timer.start(1)
    
    dialog.exec_()