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

week12_marks = 0
week6_marks = 0 
week3_marks = 0 
week2_marks = 0 
week1_marks = 0

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
    
def TextExtract(img):
    text = OCR.image_to_string(img)                                                                       # IMAGE TO TEXT
    TextProcess(text)                                                                                   # CALLING TEXT PROCESSING FUNCTION

def PointCALC(week):                                                                                    # POINT CALCULATOR
    points=0
    while(week>=12):
        points+=int(week12_marks)
        week-=12
    while(week>=6):
        points+=int(week6_marks)
        week-=6
    while(week>=3):
        points+=int(week3_marks)
        week-=3
    while(week>=2):
        points+=int(week2_marks)
        week-=2
    while(week>=1):
        points+=int(week1_marks)
        week-=1
    currentPdfData["POINTS"]=points                                                                               # APPENDING POINT TO DICT

def CropImage(img):                                                                                    # IMAGE CROPPING
    _,img_h=img.size
    return img.crop((0,0,600,img_h))                                                                    # RETURNING PIL OBJECT OF CROPPED IMAGE

def ScaleImage(img):                                                                                   # IMAGE SCALING FUNCTION
    img_w,img_h=img.size                                                                                # DETERMINE IMAGE SIZE
    bg=Image.new('RGB',(1080,1080),'white')                                                             # CREATE WHITE BACKGROUND
    img_w=int(img_w/5)                                                             
    img_h=int(img_h/5)
    img=img.resize((img_w,img_h))                                                                       # RESIZE THE IMAGE BY A FACTOR OF 10
    bg_w,bg_h=bg.size                                                                                   # DETERMINE BACKGROUND IMAGE SIZE
    offset=(int((bg_w-img_w)/2),int((bg_h-img_h)/2))                                                    # CALCULATE OFFSET
    bg.paste(img,offset)                                                                                # PASTE RESIZED IMAGE TO WHITE BACKGROUND
    return bg

def ParseWeeks(img):                                                                                    # WEEKS READING FUNCTION
    text=OCR.image_to_string(img,config='--psm 6')                                                      # SETTING PYTESSERACT TO psm6 CONFIGUTAION TO READ LARGE FONTS
    large=0
    for word in text:
        if word.isnumeric():                                                                            # CHECKING IF THE READ DATA CONTAINS A NUMBER (WEEK)
            if large<int(word):
                large=int(word)                                                                         # FINDING THE LARGEST NUMBER
    return large                                                                                        # RETURNING THE LARGEST NO.OF WEEKS

def ParseCourseDuration(img):

    # Crop The Required Area 
    img = CropImage(img) 
    
    # Scale Image To Required Size
    img = ScaleImage(img)

    # Parse Course Duration From Pre-Processed Image
    week=READ_WEEKS(img)                                                                                # CALLING WEEK READING FUNCTION
    currentPdfData["DURATION"]=week                                                                               # APPENDING DURATION TO DICT
    PointCALC(week)                                                                                     # CALLING POINT CALCULATING FUNCTION

def CustomizeMarks():

    global week12_marks, week6_marks, week3_marks, week2_marks, week1_marks
    week12_marks=input("INPUT MARKS FOR WEEK >= 12 WEEKS:")
    week6_marks=input("INPUT MARKS FOR WEEK >= 6 WEEKS:")
    week3_marks=input("INPUT MARKS FOR WEEK >= 3 WEEKS:")
    week2_marks=input("INPUT MARKS FOR WEEK >= 2 WEEKS:")
    week1_marks=input("INPUT MARKS FOR WEEK >= 1 WEEK :")


def ImagePreProcess(pdfCurrentPageImg):
    # Increase Image Contrast
    pdfCurrentPageImg = ImageEnhance.Contrast(pdfCurrentPageImg).enhance(imgContrastEnhanceFactor)

    # Increase Image Sharpness
    pdfCurrentPageImg = ImageEnhance.Sharpness(pdfCurrentPageImg).enhance(imgSharpnessEnhanceFactor)

    # Convert Image To Grayscale
    pdfCurrentPageImg = pdfCurrentPageImg.convert('L')

    # Correct Image Orientation
    angle = OCR.image_to_osd(pdfCurrentPageImg)
    angle = angle.split("\n")
    rot = [int(i) for i in angle[2].split() if i.isdigit()]
    pdfCurrentPageImg = pdfCurrentPageImg.rotate(rot[0],expand = True)

    # Return Pre-Processed Image
    return pdfCurrentPageImg

def PDFDataExtract():
    # Setting Up PDF Reader
    pdfReader = PyPDF2.PdfReader(open(sourceFolderPath+"/"+pdfFileName,mode="rb"),strict=False)

    # Converting All Pages of PDF To List of Images
    pdfPagesImgList = PDF.convert_from_path(sourceFolderPath+"/"+pdfFileName,thread_count=multiprocessing.cpu_count(),dpi=200,strict=False)

    # Processing Each Page
    for pdfCurrentPageNumber,pdfCurrentPageImg in enumerate(pdfPagesImgList,1):

        # Checking For First-Page and Last-Page
        if pdfCurrentPageNumber == len(pdfReader.pages) or pdfCurrentPageNumber == 1:
            # Pre-Processing The Image
            preprocessedPdfCurrentPageImg = ImagePreProcess(pdfCurrentPageImg)

            # Extract Info From First-Page
            if pdfCurrentPageNumber == 1: TextExtract(preprocessedPdfCurrentPageImg)
            # Extract Info From Last-Page
            elif pdfCurrentPageNumber == len(pdfReader.pages): ParseCourseDuration(preprocessedPdfCurrentPageImg)

def LoadKTUScheme():
    global week12_marks, week6_marks, week3_marks, week2_marks, week1_marks
    week1_marks=3
    week2_marks=6
    week3_marks=12
    week6_marks=25
    week12_marks=50

def Configuration():
    global sourceFolderPath, outputFolderPath, courseProviderNameListCsvFilePath, personNameListCsvFilePath, pdfFileName, currentPdfData, isMarksCustomized

    sourceFolderPath=input("\nENTER THE SOURCE FOLDER PATH : ")
    outputFolderPath=input("ENTER THE WORKSPACE FOLDER PATH : ")
    courseProviderNameListCsvFilePath=input("ENTER COURSE NAME LIST FILE PATH : ")
    personNameListCsvFilePath=input("ENTER NAME LIST FILE PATH : ")
    isMarksCustomized= True if (input("WOULD YOU LIKE TO CUSTOMIZE THE MARKING SCHEME FOR EACH WEEK (Y/N)? [DEFAULT SCHEME : KTU]").lower() == 'y') else False

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

        fileExt=Path(pdfFileName).suffix.lower()

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