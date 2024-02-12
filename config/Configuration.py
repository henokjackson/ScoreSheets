import os
from shutil import rmtree
from config import globals

def SystemSetup():
    if os.name == "posix": globals.clearScreenCommand = 'clear'
    elif os.name == "nt" : globals.clearScreenCommand = 'cls'

def WorkspaceSetup():
    os.makedirs(globals.outputFolderParentPath+'/'+globals.outputFolderName)

def Configuration(sourceFolderPath, courseProviderNameListCsvFilePath, personNameListCsvFilePath, isMarksCustomized, outputFolderParentPath):
    # Input Parameters
    globals.sourceFolderPath = sourceFolderPath
    globals.courseProviderNameListCsvFilePath = courseProviderNameListCsvFilePath
    globals.personNameListCsvFilePath = personNameListCsvFilePath
    globals.isMarksCustomized = isMarksCustomized
    globals.outputFolderParentPath = outputFolderParentPath

def FlushBuffers():
    globals.currentPdfDataDictionary = {}

def ClearCache():
    rmtree("config/__pycache__")
    rmtree("file_handling/__pycache__")
    rmtree("image_processing/__pycache__")
    rmtree("score_calculation/__pycache__")
    rmtree("text_processing/__pycache__")
    rmtree("ui/__pycache__")