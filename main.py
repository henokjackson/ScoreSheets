import os
import nltk
from pathlib import Path
from config import globals
from ui import LoadingScreen, MainScreen
from ui.Elements import Banner, ProgressBar
from file_handling.FileIO import CSVWriter, PDFDataExtract
from score_calculation.ScoreCalculation import CustomizeMarks, LoadKTUScheme, ScoreAggregator
from config.Configuration import Configuration, FlushBuffers, SystemSetup, WorkspaceSetup, ClearCache

nltk.download('stopwords')
nltk.download('punkt')

if __name__ == "__main__":
    # Load Splash Screen
    LoadingScreen.Start()

    # Render Main Screen
    MainScreen.Start()

    # Input Configuration
    Configuration()

    # Setting Up Workspace
    WorkspaceSetup(globals.outputFolderParentPath)

    # Load Default Marking Scheme (KTU)
    LoadKTUScheme()

    # Customize Marking Scheme
    if globals.isMarksCustomized: CustomizeMarks()

    # Performing PDF Search and Parsing
    for index, globals.pdfFileName in enumerate(os.listdir(globals.sourceFolderPath),1):
        # Update Progress
        ProgressBar(index, len(os.listdir(globals.sourceFolderPath)))
        
        fileExt = Path(globals.pdfFileName).suffix.lower()
        
        # PDF Parsing
        if fileExt == '.pdf': PDFDataExtract()
        
        # Add Up Scores Of The Same Person
        ScoreAggregator()

        # Flush Out Current-File Data Holders
        FlushBuffers()
    
    # Write Results to CSV File
    CSVWriter()