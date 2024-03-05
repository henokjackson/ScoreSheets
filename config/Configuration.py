import os
from shutil import rmtree
from config import Globals

def SystemSetup():
    if os.name == "posix": Globals.clearScreenCommand = 'clear'
    elif os.name == "nt" : Globals.clearScreenCommand = 'cls'

def WorkspaceSetup():
    try:
        os.makedirs(Globals.outputFolderParentPath+'/'+Globals.outputFolderName)
    except FileExistsError:
        print("Folder Already Exists !, Removing Current Folder and Its Contents...")
        rmtree(Globals.outputFolderParentPath+'/'+Globals.outputFolderName)
        WorkspaceSetup()


def Configuration(sourceFolderPath, courseProviderNameListCsvFilePath, personNameListCsvFilePath, isMarksCustomized, outputFolderParentPath):
    # Input Parameters
    Globals.sourceFolderPath = sourceFolderPath
    Globals.courseProviderNameListCsvFilePath = courseProviderNameListCsvFilePath
    Globals.personNameListCsvFilePath = personNameListCsvFilePath
    Globals.isMarksCustomized = isMarksCustomized
    Globals.outputFolderParentPath = outputFolderParentPath

def FlushBuffers():
    Globals.currentPdfDataDictionary = {}

def ClearCache():
    for folder in Globals.pycacheFoldersList:
        rmtree(folder)