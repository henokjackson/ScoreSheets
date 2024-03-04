# Import File For Global Variables
from multiprocessing import cpu_count#, Queue

# Data Holders
currentPdfDataDictionary = {}
currentPdfDataList = []

# File Paths
sourceFolderPath = './test_data'
outputFolderParentPath = '.'
outputFolderName = 'output'
outputFileName = 'ScoreSheet'
courseProviderNameListCsvFilePath = './config/info/CourseList.csv'
personNameListCsvFilePath = './config/info/NameList.csv'
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

# Shared UI Variables
progressBarPercentage = 0
currentFileName = ''
currentFileNo = 0

# Threads
initProcessesThread = None
initProcessesThreadNativeId = -1

initProgressBarUpdateThread = None
initProgressBarUpdateThreadNativeId = -1

# Thread Safe Queues
# currentFileNoQueue = Queue()
# currentFileNameQueue = Queue()
# progressBarPercentageQueue = Queue()