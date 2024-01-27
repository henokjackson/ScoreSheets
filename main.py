import os
import nltk
from pathlib import Path

nltk.download('stopwords')
nltk.download('punkt')

currentPdfDataDictionary = {}
currentPdfDataList = []

sourceFolderPath = ''
outputFolderParentPath = ''
outputFolderName = 'data'
courseProviderNameListCsvFilePath = ''
personNameListCsvFilePath = ''
pdfFileName = ''

isMarksCustomized = False
isCsvHeaderWritten = False

maximumScoreThreshold = 50

clearScreenCommand = ''


if __name__ == "__main__":
    # Setting Up System Parameters
    SystemSetup()

    # Render Main Screen
    Banner()

    # Input Configuration
    Configuration()

    # Setting Up Workspace
    WorkspaceSetup(outputFolderParentPath)

    # Load Default Marking Scheme (KTU)
    LoadKTUScheme()

    # Customize Marking Scheme
    if isMarksCustomized: CustomizeMarks()

    # Performing PDF Search and Parsing
    for index, pdfFileName in enumerate(os.listdir(sourceFolderPath),1):
        # Update Progress
        ProgressBar(index, len(os.listdir(sourceFolderPath)))
        
        fileExt = Path(pdfFileName).suffix.lower()
        
        # PDF Parsing
        if fileExt == '.pdf': PDFDataExtract()
        
        # Add Up Scores Of The Same Person
        ScoreAggregator()

        # Flush Out Current-File Data Holders
        FlushBuffers()
    
    # Write Results to CSV File
    CSVWriter()