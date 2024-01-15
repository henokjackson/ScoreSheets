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
from PIL import Image,ImageEnhance                                                                      # LIBRARY FOR IMAGE PROCESSING
from nltk.tokenize import word_tokenize                                                                 # LIBRARY FOR TOKENIZATION OF TEXT

nltk.download('stopwords')
nltk.download('punkt')

imgContrastEnhanceFactor = 1.5
imgSharpnessEnhanceFactor = 2

currentPdfData = {}
currentPdfDataList = []

sourceFolderPath = ''
outputFolderPath = ''
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
    if not currentPdfDataList: currentPdfDataList.append(currentPdfData)
    else:
        flag=1
        for no,item in enumerate(currentPdfDataList,0):                                                           # ITERATING OVER EACH DICTIONARY FROM DICTLIST
            if(item["NAME"]==currentPdfData["NAME"] and item["COURSE TYPE"]==currentPdfData["COURSE TYPE"]):                # FOR SAME NAME AND COURSE TYPE MERGE POINTS
                currentPdfData["POINTS"]+=item["POINTS"]                                                          # MERGING POINTS
                currentPdfData["DURATION"]+=item["DURATION"]                                                      # MERGING WEEKS
                currentPdfDataList[no]=currentPdfData                                                                       # APPENDING DICTIONARY TO LIST
                flag=0
                break
        if flag==1:
            currentPdfDataList.append(currentPdfData)

def ProgressBar(nue,den):                                                                                   # PROGRESS BAR
    os.system('clear')
    prog=(nue/den)*10
    print("Progress: [","█"*int(prog)," "*(10-int(prog)),"\b] ~",int(prog*10),"%")
    print("\nNO =",nue,", File =",pdfFileName)

def WorkspaceSetup(outputFolderPath):                                                                                 # WORKSPACE SETUP FUNCTION
    os.makedirs(outputFolderPath+"/data")                                                                        # MAKING FOLDER CALLED Data FOR STORING ALL THE PROGRAM DATA

def Menu():                                                                                             # INTERFACE
    os.system('cls')
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
        for index in enumerate(refinedTextWordsList,0):
            if (str(column[0]).lower()) == (str(refinedTextWordsList[index]).lower()):
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
        for index in enumerate(personsNameList,0):
            if (str(column[0]).lower()) == (str(personsNameList[index]).lower()):
                personName = personsNameList[index]
    
    # Generate Hyperlink To Unidentified Certificates
    if(personName == "UNIDENTIFIED"):
        currentPdfData["NAME"] = "=HYPERLINK("+"\""+sourceFolderPath+"/"+pdfFileName+"\""+",\"NO_NAME\""+")"
    else:
        currentPdfData["NAME"] = personName
    currentPdfData["COURSE TYPE"] = courseType

def CSVWriter():                                                                                      # CONVERT DICT TO CSV
    columns=['NAME','COURSE TYPE','DURATION','POINTS','TOTAL']
    global isCsvHeaderWritten
    with open(outputFolderPath+"/Data/CertificateDetails.csv",'a+') as csv_file:  
        writer=csv.DictWriter(csv_file,fieldnames=columns)                                              # IMPORTING CSV FILE AND SETTING FIELDS
        if not isCsvHeaderWritten:                                                                                  # CHECKING FOR HEADER FLAG
            writer.writeheader()                                                                        # WRITING HEADER TO CSV
            isCsvHeaderWritten=True                                                                                   # SETTING FLAG
        for data in currentPdfDataList:
            if (isMarksCustomized):
                data["TOTAL"]=data["POINTS"]
            else:
                if (data["POINTS"]>=50):
                    data["TOTAL"]=data["POINTS"]                                                        # ADDING TOTAL POINTS
                    data["POINTS"]=50                                                                   # CUTTING OF POINTS ABOVE 50
                else:
                    data["TOTAL"]=data["POINTS"]
            writer.writerow(data)                                                                       # WRITING DICTIONARY DATA INTO CSV
    
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
    currentPdfData["DURATION"] = courseDuration

    # Calculate Score
    totalScore = ScoreCalculator(courseDuration)
    
    # Set Scores
    currentPdfData["POINTS"] = totalScore

def CustomizeMarks():

    global week12Score, week6Score, week3Score, week2Score, week1Score

    week12Score = int(input("INPUT MARKS FOR WEEK >= 12 WEEKS:"))
    week6Score = int(input("INPUT MARKS FOR WEEK >= 6 WEEKS:"))
    week3Score = int(input("INPUT MARKS FOR WEEK >= 3 WEEKS:"))
    week2Score = int(input("INPUT MARKS FOR WEEK >= 2 WEEKS:"))
    week1Score = int(input("INPUT MARKS FOR WEEK >= 1 WEEK :"))


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

    global sourceFolderPath, outputFolderPath, courseProviderNameListCsvFilePath, personNameListCsvFilePath, pdfFileName, currentPdfData, isMarksCustomized

    # Input Parameters
    sourceFolderPath = input("\nENTER THE SOURCE FOLDER PATH : ")
    outputFolderPath = input("ENTER THE WORKSPACE FOLDER PATH : ")
    courseProviderNameListCsvFilePath = input("ENTER COURSE NAME LIST FILE PATH : ")
    personNameListCsvFilePath = input("ENTER NAME LIST FILE PATH : ")
    isMarksCustomized = True if (input("WOULD YOU LIKE TO CUSTOMIZE THE MARKING SCHEME FOR EACH WEEK (Y/N)? [DEFAULT SCHEME : KTU]").lower() == 'y') else False

def FlushBuffers():
    global currentPdfData
    currentPdfData = {}

if __name__ == "__main__":

    # Render Main Menu
    Menu()   

    # Input Configuration
    Configuration()                                                                                           

    # Setting Up Workspace
    WorkspaceSetup(outputFolderPath)

    # Load Default Marking Scheme (KTU)
    LoadKTUScheme()

    # Customize Marking Scheme
    if isMarksCustomized: CustomizeMarks()

    # Performing PDF Search and Parsing
    for index, pdfFileName in enumerate(os.listdir(sourceFolderPath),1):

        fileExt = Path(pdfFileName).suffix.lower()

        # Update Progress
        ProgressBar(index, len(os.listdir(sourceFolderPath)))
        
        # PDF Parsing
        if fileExt == '.pdf': PDFDataExtract()
        
        # Add Up Scores Of The Same Person
        ScoreAggregator()

        # Flush Out Current-File Data Holders
        FlushBuffers()
    
    # Write Results to CSV File
    CSVWriter()