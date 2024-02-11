from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setFixedSize(403, 281)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("assets/misc/copyleft.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet("background-color: rgb(236, 234, 231);")
        self.logo_label = QtWidgets.QLabel(Dialog)
        self.logo_label.setGeometry(QtCore.QRect(115, 170, 171, 71))
        self.logo_label.setText("")
        self.logo_label.setPixmap(QtGui.QPixmap("assets/org/rset.gif"))
        self.logo_label.setScaledContents(True)
        self.logo_label.setObjectName("logo_label")
        self.credits_textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.credits_textBrowser.setGeometry(QtCore.QRect(10, 10, 381, 261))
        self.credits_textBrowser.setStyleSheet("")
        self.credits_textBrowser.setOpenExternalLinks(True)
        self.credits_textBrowser.setOpenLinks(True)
        self.credits_textBrowser.setObjectName("credits_textBrowser")
        self.logo_label_2 = QtWidgets.QLabel(Dialog)
        self.logo_label_2.setGeometry(QtCore.QRect(120, 150, 171, 71))
        self.logo_label_2.setText("")
        self.logo_label_2.setPixmap(QtGui.QPixmap("assets/org/rset.gif"))
        self.logo_label_2.setScaledContents(True)
        self.logo_label_2.setObjectName("logo_label_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Credits"))
        self.credits_textBrowser.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Contributers</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">------------</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Henok Jackson (<a href=\"https://github.com/henokjackson\"><span style=\" text-decoration: underline; color:#0000ff;\">@henokjackson</span></a>)</p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Jisha Joseph (<a href=\"https://github.com/jamiebit\"><span style=\" text-decoration: underline; color:#0000ff;\">@jamiebit</span></a>)</p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Gloria Joseph (<a href=\"https://github.com/gloria01joseph\"><span style=\" text-decoration: underline; color:#0000ff;\">@gloria01joseph</span></a>)</p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; text-decoration: underline;\">The project was built for :</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600; text-decoration: underline;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600; text-decoration: underline;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600; text-decoration: underline;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600; text-decoration: underline;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600; text-decoration: underline;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600; text-decoration: underline;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Github : <a href=\"https://github.com/henokjackson/ScoreSheets\"><span style=\" text-decoration: underline; color:#0000ff;\">ScoreSheets</span></a></p></body></html>"))

def Start():
    dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(dialog)
    dialog.setWindowModality(QtCore.Qt.ApplicationModal)
    dialog.show()
    dialog.exec_()