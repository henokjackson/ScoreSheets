import os
import nltk
import globals
from pathlib import Path
from Elements import Banner, ProgressBar
from FileIO import CSVWriter, PDFDataExtract
from ScoreCalculation import CustomizeMarks, LoadKTUScheme, ScoreAggregator
from Configuration import Configuration, FlushBuffers, SystemSetup, WorkspaceSetup

nltk.download('stopwords')
nltk.download('punkt')

if __name__ == "__main__":
    # Setting Up System Parameters
    SystemSetup()

    # Render Main Screen
    Banner()

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