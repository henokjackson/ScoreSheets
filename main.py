import os                                                                                               # LIBRARY FOR FOLDER OPERATIONS
import csv                                                                                              # LIBRARY FOR CSV FILE OPERTIONS
import nltk
import spacy                                                                                            # LIBRARY FOR NLP
import string                                                                                           # LIBRARY FOR STRING OPERATIONS
import PyPDF2                                                                                           # LIBRARY FOR READING NO.OF PAGES IN A PDF
import multiprocessing                                                                                  # LIBRARY FOR GETTING CPU CORE COUNT
import pdf2image as PDF                                                                                 # LIBRARY FOR CONVERTING PDF TO IMAGE
from pathlib import Path                                                                                # LIBRARY FOR READING FILE EXTENSION FROM PATH
import pytesseract as OCR                                                                               # LIBRARY FOR OCR
from nltk.corpus import stopwords                                                                       # LIBRARY FOR DETERMINING STOPWORDS FROM TEXT
from PIL import Image, ImageEnhance                                                                     # LIBRARY FOR IMAGE PROCESSING
from nltk.tokenize import word_tokenize                                                                 # LIBRARY FOR TOKENIZATION OF TEXT

nltk.download('stopwords')
nltk.download('punkt')

imgContrastEnhanceFactor = 1.5
imgSharpnessEnhanceFactor = 2

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

week12Score = 0
week6Score = 0 
week3Score = 0 
week2Score = 0 
week1Score = 0

def ScoreAggregator():
    if not currentPdfDataList:
        currentPdfDataList.append(currentPdfDataDictionary)
    else:
        IsPersonDataExisting = False

        # Aggregating Scores of Same Type of Courses Taken By The Same Person
        for index, currentPdfDataListDictionaryItem in enumerate(currentPdfDataList, 0):
            if(currentPdfDataListDictionaryItem["Name"] == currentPdfDataDictionary["Name"] and currentPdfDataListDictionaryItem["Course Type"] == currentPdfDataDictionary["Course Type"]):
                currentPdfDataDictionary["Current Score"] += currentPdfDataListDictionaryItem["Current Score"]
                currentPdfDataDictionary["Duration"] += currentPdfDataListDictionaryItem["Duration"]
                currentPdfDataList[index] = currentPdfDataDictionary
                IsPersonDataExisting = True
                break
        # Append Data of New Person
        if not IsPersonDataExisting: currentPdfDataList.append(currentPdfDataDictionary)

def ProgressBar(current, total):
    os.system('clear')
    progress = (current/total)*10
    print("Progress: [", "█"*int(progress), " "*(10-int(progress)), "\b] ~", int(progress*10), "%")
    print("\nItem No. => ", current, "\nFilename => ", pdfFileName)

def WorkspaceSetup(outputFolderParentPath):
    os.makedirs(outputFolderParentPath+'/'+outputFolderName)

def Menu():
    os.system('clear')
    print("\t"*3+"█"*58)
    print("\t"*3+"██"+"\t"*7+"██")
    print("\t"*3+"██"+"\t"*2+"CERTIFICATE POINT CALCULATOR"+"\t"*2+"██")
    print("\t"*3+"██"+"\t"*7+"██")
    print("\t"*3+"█"*58)

def TextPreProcess(text):
    # Junk Removal
    characterReplaceMap = str.maketrans(string.punctuation, ' '*len(string.punctuation))   
    junkRemovedText = text.translate(characterReplaceMap)

    # Generate Stopwords List
    stopwordsList=set(stopwords.words("english"))

    # Tokenization
    tokenList = word_tokenize(junkRemovedText)

    # Stopwords Removal
    stopwordsRemovedTokenList=[]
    for token in tokenList:
        if token not in stopwordsList:
            stopwordsRemovedTokenList.append(token)

    # Generating Clean Text
    refinedText = ' '.join(stopwordsRemovedTokenList)

    # Generating Clean Words List
    refinedTextWordsList = stopwordsRemovedTokenList

    return refinedText,refinedTextWordsList

def TextProcess(text):
    # Setting Course Type Variable
    courseType="NON MOOC"
    
    # Perform Text Pre-Processing
    refinedText, refinedTextWordsList = TextPreProcess(text)

    # Open Course Provider Listing File
    courseProviderNameListCsvFile = open(courseProviderNameListCsvFilePath)
    courseProviderNameListCsvFileColumnsList = csv.reader(courseProviderNameListCsvFile)

    # Iterating Through Course Providers' List To Find The Match and Set Course Type
    for column in courseProviderNameListCsvFileColumnsList:
        for refinedTextWord in refinedTextWordsList:
            if (str(column[0]).lower()) == (str(refinedTextWord).lower()):
                courseType=column[1]

    # Entity Variables
    personName = "UNIDENTIFIED"
    personsNameList = []

    # Named Entity Recognition
    modelNLP = spacy.load("en_core_web_sm")
    namedEntitiesList = modelNLP(refinedText).ents

    # Generating List of Persons In Text
    for name in namedEntitiesList:
        if name.label_ == "PERSON":
            personsNameList.append(name.text)

    # Opening Persons' Name Listing File
    personNameListCsvFile = open(personNameListCsvFilePath)
    personNameListCsvFileColumnsList = csv.reader(personNameListCsvFile)

    # Iterating Through Person Name List To Find The Match and Set Course Type
    for column in personNameListCsvFileColumnsList:
        for personsNameListItem in personsNameList:
            if (str(column[0]).lower()) == (str(personsNameListItem).lower()):
                personName = personsNameListItem
    
    # Generate Hyperlink To Unidentified Certificates
    if(personName == "UNIDENTIFIED"):
        currentPdfDataDictionary["Name"] = "=HYPERLINK("+"\""+sourceFolderPath+"/"+pdfFileName+"\""+",\"NO_NAME\""+")"
    else:
        currentPdfDataDictionary["Name"] = personName
    currentPdfDataDictionary["Course Type"] = courseType

def CSVWriter():
    # Setting CSV File Columns Names
    csvColumns = ['Name','Course Type','Duration','Current Score','Total Score']

    global isCsvHeaderWritten
    
    # Opening CSV File
    scoreSheetCsvFile = open(outputFolderParentPath + '/' + outputFolderName + "/CertificateDetails.csv", 'a+')
    scoreSheetCsvFileWriter = csv.DictWriter(scoreSheetCsvFile, fieldnames = csvColumns)

    # Writing CSV Header
    if not isCsvHeaderWritten:
        scoreSheetCsvFileWriter.writeheader()
        isCsvHeaderWritten = True
    
    # Calculating Total SCore
    for data in currentPdfDataList:
        if (isMarksCustomized):
            data["Total Score"] = data["Current Score"]
        else:
            # Checking Total Score Restriction
            if (data["Current Score"] >= 50):
                data["Total Score"] = data["Current Score"]
                data["Current Score"] = 50
            else:
                data["Total Score"] = data["Current Score"]
        # Writting Data To CSV
        scoreSheetCsvFileWriter.writerow(data)
    
def TextExtract(currentPageImage):
    # Read Text From Image
    text = OCR.image_to_string(currentPageImage)
    
    # Text Processing Function
    TextProcess(text)

def ScoreCalculator(courseDuration):
    
    courseDurationClone = courseDuration
    totalScore = 0

    while(courseDurationClone >= 12):
        totalScore += week12Score
        courseDurationClone -= 12
        
    while(courseDurationClone >= 6):
        totalScore += week6Score
        courseDurationClone -= 6

    while(courseDurationClone >= 3):
        totalScore += int(week3Score)
        courseDurationClone -= 3
    
    while(courseDurationClone >= 2):
        totalScore += week2Score
        courseDurationClone -= 2
    
    while(courseDurationClone >= 1):
        totalScore += week1Score
        courseDurationClone -= 1

    return totalScore

def CropImage(inputImage):
    # Get Image Size
    _, inputImageHeight = inputImage.size
    
    # Crop Image
    outputImage = inputImage.crop((0, 0, 600, inputImageHeight))

    return outputImage

def ScaleImage(inputImage):
    # Get Image Size
    inputImageWidth, inputImageHeight = inputImage.size 

    # Create a White Canvas
    canvas = Image.new('RGB', (1080, 1080), 'white')

    # Reduce Input Image
    inputImageWidthReduced = int(inputImageWidth/5)                                                             
    inputImageHeightReduced = int(inputImageHeight/5)
    inputImageResized = inputImage.resize((inputImageWidthReduced, inputImageHeightReduced))

    # Get Canvas SIze
    canvasWidth, canvasHeight = canvas.size

    # Calculating Image Offset
    imageBorderOffset = (int((canvasWidth-inputImageWidthReduced)/2),int((canvasHeight-inputImageHeightReduced)/2))

    # Pasting Image To Canvas
    canvas.paste(inputImageResized, imageBorderOffset)

    outputImage = canvas

    return outputImage

def ParseWeeks(img):
    # Read Text From Image, Configuring To Read Large Fonts
    text = OCR.image_to_string(img, config='--psm 6')

    # Determine Course Duration
    longestCourseDuration = 0
    for word in text:
        if word.isnumeric():
            if longestCourseDuration < int(word):
                longestCourseDuration = int(word)

    courseDuration = longestCourseDuration

    return courseDuration

def GetCourseDuration(preprocessedpdfCurrentPageImage):
    # Crop The Required Area 
    preprocessedpdfCurrentPageImage = CropImage(preprocessedpdfCurrentPageImage) 
    
    # Scale Image To Required Size
    preprocessedpdfCurrentPageImage = ScaleImage(preprocessedpdfCurrentPageImage)

    # Parse Course Duration From Pre-Processed Image
    courseDuration = ParseWeeks(preprocessedpdfCurrentPageImage)

    # Set Course Duration
    currentPdfDataDictionary["Duration"] = courseDuration

    # Calculate Score
    totalScore = ScoreCalculator(courseDuration)
    
    # Set Scores
    currentPdfDataDictionary["Current Score"] = totalScore

def CustomizeMarks():
    global week12Score, week6Score, week3Score, week2Score, week1Score

    week12Score = int(input("INPUT MARKS FOR WEEK > or = 12 WEEKS:"))
    week6Score = int(input("INPUT MARKS FOR WEEK > or = 6 WEEKS:"))
    week3Score = int(input("INPUT MARKS FOR WEEK > or = 3 WEEKS:"))
    week2Score = int(input("INPUT MARKS FOR WEEK > or = 2 WEEKS:"))
    week1Score = int(input("INPUT MARKS FOR WEEK > or = 1 WEEK :"))


def ImagePreProcess(pdfCurrentPageImage):
    # Increase Image Contrast
    pdfCurrentPageImage = ImageEnhance.Contrast(pdfCurrentPageImage).enhance(imgContrastEnhanceFactor)

    # Increase Image Sharpness
    pdfCurrentPageImage = ImageEnhance.Sharpness(pdfCurrentPageImage).enhance(imgSharpnessEnhanceFactor)

    # Convert Image To Grayscale
    pdfCurrentPageImage = pdfCurrentPageImage.convert('L')

    # Correct Image Orientation
    angle = OCR.image_to_osd(pdfCurrentPageImage)
    angle = angle.split("\n")
    rot = [int(i) for i in angle[2].split() if i.isdigit()]
    pdfCurrentPageImage = pdfCurrentPageImage.rotate(rot[0],expand = True)

    # Return Pre-Processed Image
    return pdfCurrentPageImage

def PDFDataExtract():
    # Setting Up PDF Reader
    pdfReader = PyPDF2.PdfReader(open(sourceFolderPath+"/"+pdfFileName,mode="rb"),strict=False)

    # Converting All Pages of PDF To List of Images
    pdfPagesImgList = PDF.convert_from_path(sourceFolderPath+"/"+pdfFileName,thread_count=multiprocessing.cpu_count(),dpi=200,strict=False)

    # Processing Each Page
    for pdfCurrentPageNumber, pdfCurrentPageImage in enumerate(pdfPagesImgList,1):

        # Checking For First-Page and Last-Page
        if pdfCurrentPageNumber == len(pdfReader.pages) or pdfCurrentPageNumber == 1:

            # Pre-Processing The Image
            preprocessedpdfCurrentPageImage = ImagePreProcess(pdfCurrentPageImage)

            # Extract Info From First-Page
            if pdfCurrentPageNumber == 1: TextExtract(preprocessedpdfCurrentPageImage)

            # Extract Info From Last-Page
            elif pdfCurrentPageNumber == len(pdfReader.pages): GetCourseDuration(preprocessedpdfCurrentPageImage)

def LoadKTUScheme():
    global week12Score, week6Score, week3Score, week2Score, week1Score
    
    week1Score = 3
    week2Score = 6
    week3Score = 12
    week6Score = 25
    week12Score = 50

def Configuration():
    global sourceFolderPath, outputFolderParentPath, courseProviderNameListCsvFilePath, personNameListCsvFilePath, pdfFileName, currentPdfDataDictionary, isMarksCustomized

    # Input Parameters
    sourceFolderPath = input("\nCertificates Folder Path : ")
    courseProviderNameListCsvFilePath = input("Courses List CSV File Path : ")
    personNameListCsvFilePath = input("Name List CSV File Path : ")
    isMarksCustomized = True if (input("Do Want To Customize The Marking Scheme [DEFAULT SCHEME : KTU] (Y/N) ? : ").lower() == 'y') else False
    outputFolderParentPath = input("Output Folder Path : ")

def FlushBuffers():
    global currentPdfDataDictionary
    currentPdfDataDictionary = {}

if __name__ == "__main__":
    # Render Main Menu
    Menu()   

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