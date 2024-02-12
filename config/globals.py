# Import File For Global Variables

# Data Holders
currentPdfDataDictionary = {}
currentPdfDataList = []

# File Pathss
sourceFolderPath = None
outputFolderParentPath = '.'
outputFolderName = 'data'
courseProviderNameListCsvFilePath = None
personNameListCsvFilePath = None
pdfFileName = None

# Constants
imgContrastEnhanceFactor = 1.5
imgSharpnessEnhanceFactor = 2

# Config Flags
isMarksCustomized = False
isCsvHeaderWritten = False

# Logical Parameters
maximumScoreThreshold = 50

# OS Parameters
clearScreenCommand = ''