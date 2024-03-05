from config import Globals
from PyQt5 import QtWidgets
from threading import Thread
from ui.views import ProcessingDialog
from process_handling import MainProcesses

def SelectSourceFolder(ui):
    sourceFolderPath = QtWidgets.QFileDialog.getExistingDirectory()
    ui.source_folder_path_lineEdit.setText(sourceFolderPath)

def SelectDestinationFolder(ui):
    destinationFolderPath = QtWidgets.QFileDialog.getExistingDirectory()
    ui.destination_folder_lineEdit.setText(destinationFolderPath)

def SelectNameListFile(ui):
    nameListFilePath = QtWidgets.QFileDialog.getOpenFileName()
    ui.name_list_lineEdit.setText(nameListFilePath[0])

def SelectCourseListFile(ui):
    courseListFilePath = QtWidgets.QFileDialog.getOpenFileName()
    ui.courses_list_lineEdit.setText(courseListFilePath[0])

def ExecuteMainProcessesThread(ui):
    # Parameter Check
    if ( ui.source_folder_path_lineEdit.text() == "" or ui.courses_list_lineEdit.text() == "" or ui.name_list_lineEdit.text() == ""):
        parametersNotSuppliedWarningMessageBox = QtWidgets.QMessageBox()
        parametersNotSuppliedWarningMessageBox.setIcon(QtWidgets.QMessageBox.Critical)
        parametersNotSuppliedWarningMessageBox.setText("All file paths were not configured. Please configure all file / folder paths.")
        parametersNotSuppliedWarningMessageBox.setWindowTitle("Error")
        parametersNotSuppliedWarningMessageBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        parametersNotSuppliedWarningMessageBox.exec_()

    else:
        # Getting Parameters
        sourceFolderPath = ui.source_folder_path_lineEdit.text()
        courseProviderNameListCsvFilePath = ui.courses_list_lineEdit.text()
        personNameListCsvFilePath = ui.name_list_lineEdit.text()
        isMarksCustomized = False
        outputFolderParentPath = ui.destination_folder_lineEdit.text()

        # MainProcesses Thread
        Globals.mainProcessesThread = Thread(target = MainProcesses.ExecuteProcesses, name = 'Main Processes Thread', args = (sourceFolderPath, courseProviderNameListCsvFilePath, personNameListCsvFilePath, isMarksCustomized, outputFolderParentPath))
        Globals.mainProcessesThread.start()

        ProcessingDialog.Render()