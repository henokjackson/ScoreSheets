import os
from shutil import rmtree
from config import globals

def SystemSetup():
    if os.name == "posix": globals.clearScreenCommand = 'clear'
    elif os.name == "nt" : globals.clearScreenCommand = 'cls'

def WorkspaceSetup(outputFolderParentPath):
    os.makedirs(outputFolderParentPath+'/'+globals.outputFolderName)

def Configuration():
    # Input Parameters
    globals.sourceFolderPath = input("\nCertificates Folder Path : ")
    globals.courseProviderNameListCsvFilePath = input("Courses List CSV File Path : ")
    globals.personNameListCsvFilePath = input("Name List CSV File Path : ")
    globals.isMarksCustomized = True if (input("Do Want To Customize The Marking Scheme [DEFAULT SCHEME : KTU] (Y/N) ? : ").lower() == 'y') else False
    globals.outputFolderParentPath = input("Output Folder Path : ")

def FlushBuffers():
    globals.currentPdfDataDictionary = {}

def ClearCache():
    rmtree("config/__pycache__")
    rmtree("file_handling/__pycache__")
    rmtree("image_processing/__pycache__")
    rmtree("score_calculation/__pycache__")
    rmtree("text_processing/__pycache__")
    rmtree("ui/__pycache__")