import os
from pathlib import Path
from config import globals
from ui.Elements import ProgressBar
from file_handling.FileIO import PDFDataExtract
from config.Configuration import Configuration, FlushBuffers
from score_calculation.ScoreCalculation import ScoreAggregator

def InitProcesses(sourceFolderPath, courseProviderNameListCsvFilePath, personNameListCsvFilePath, isMarksCustomized, outputFolderParentPath):

    # Setting Up Configuration
    Configuration(sourceFolderPath, courseProviderNameListCsvFilePath, personNameListCsvFilePath, isMarksCustomized, outputFolderParentPath)

        # Performing PDF Search and Parsing
    for index, globals.pdfFileName in enumerate(os.listdir(globals.sourceFolderPath),1):
        # Update Progress
        ProgressBar(index, len(os.listdir(globals.sourceFolderPath)))
        
        fileExt = Path(globals.pdfFileName).suffix.lower()
        
        # PDF Parsing
        if fileExt == '.pdf': PDFDataExtract()
        else: continue
        
        # Add Up Scores Of The Same Person
        ScoreAggregator()

        # Flush Out Current-File Data Holders
        FlushBuffers()