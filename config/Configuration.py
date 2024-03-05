import os
from shutil import rmtree
from config import Globals

def SystemSetup():
    if os.name == "posix": Globals.clearScreenCommand = 'clear'
    elif os.name == "nt" : Globals.clearScreenCommand = 'cls'

def WorkspaceSetup():
    os.makedirs(Globals.outputFolderParentPath+'/'+Globals.outputFolderName)

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
    rmtree("config/__pycache__")
    rmtree("file_handling/__pycache__")
    rmtree("image_processing/__pycache__")
    rmtree("score_calculation/__pycache__")
    rmtree("text_processing/__pycache__")
    rmtree("process_handler/__pycache__")
    rmtree("ui/controllers/__pycache__")
    rmtree("ui/views/__pycache__")