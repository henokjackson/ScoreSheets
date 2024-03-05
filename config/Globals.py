# File For Global Variables
from multiprocessing import cpu_count#, Queue

# Data Holders
currentPdfDataDictionary = {}
currentPdfDataList = []

# File Paths / Names
sourceFolderPath = './test_data'
outputFolderParentPath = '.'
outputFolderName = 'output'
outputFileName = 'ScoreSheet'
courseProviderNameListCsvFilePath = './config/info/CourseList.csv'
personNameListCsvFilePath = './config/info/NameList.csv'
markingSchemeFilePath = 'KTU Marking Scheme (default)'
pdfFileName = None

# Image Processing Constants
imgContrastEnhanceFactor = 1.5
imgSharpnessEnhanceFactor = 2

# Config Flags
isMarksCustomized = False
isCsvHeaderWritten = False

# Logical Parameters
maximumScoreThreshold = 50
loadingScreenInfoListIndex = 0

# OS Parameters
clearScreenCommand = ''

# Performance Parameters
noOfThreads = cpu_count()
pdfDPI = 200

# Marking Scheme Variables
week1Score = 0
week2Score = 0
week3Score = 0
week6Score = 0
week12Score = 0

# UI Variables
progressBarPercentage = 0
currentFileName = ''
currentFileNo = 0

# Thread Variables
initProcessesThread = None
initProcessesThreadNativeId = -1

#initProgressBarUpdateThread = None
#initProgressBarUpdateThreadNativeId = -1

# Thread Safe Queues
#currentFileNoQueue = Queue()
#currentFileNameQueue = Queue()
#progressBarPercentageQueue = Queue()