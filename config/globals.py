# Import File For Global Variables
from multiprocessing import cpu_count
# Data Holders
currentPdfDataDictionary = {}
currentPdfDataList = []

# File Pathss
sourceFolderPath = None
outputFolderParentPath = '.'
outputFolderName = 'data'
outputFileName = 'ScoreSheet'
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

# Performance Parameters
noOfThreads = cpu_count()
pdfDPI = 200

# UI Parameters
markingSchemeFilePath = 'KTU Marking Scheme (default)'

# Marking Scheme Variables
week1Score = 0
week2Score = 0
week3Score = 0
week6Score = 0
week12Score = 0