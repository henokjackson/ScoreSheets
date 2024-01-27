import os

clearScreenCommand = ''
outputFolderName = ''

def SystemSetup():
    global clearScreenCommand
    if os.name == 'posix': clearScreenCommand = 'clear'
    elif os.name == 'nt' : clearScreenCommand = 'cls'

def WorkspaceSetup(outputFolderParentPath):
    os.makedirs(outputFolderParentPath+'/'+outputFolderName)

def Configuration():
    global sourceFolderPath, outputFolderParentPath, courseProviderNameListCsvFilePath, personNameListCsvFilePath, pdfFileName, currentPdfDataDictionary, isMarksCustomized

    # Input Parameters
    sourceFolderPath = input("\nCertificates Folder Path : ")
    courseProviderNameListCsvFilePath = input("Courses List CSV File Path : ")
    personNameListCsvFilePath = input("Name List CSV File Path : ")
    isMarksCustomized = True if (input("Do Want To Customize The Marking Scheme [DEFAULT SCHEME : KTU] (Y/N) ? : ").lower() == 'y') else False
    outputFolderParentPath = input("Output Folder Path : ")

def FlushBuffers():
    global currentPdfDataDictionary
    currentPdfDataDictionary = {}