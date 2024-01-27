import csv
import spacy
import string
import pytesseract as OCR
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

currentPdfDataDictionary = {}
currentPdfDataList = []

sourceFolderPath = ''
courseProviderNameListCsvFilePath = ''
personNameListCsvFilePath = ''
pdfFileName = ''

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
        currentPdfDataDictionary["Name"] = "=HYPERLINK("+"\""+sourceFolderPath+"/"+pdfFileName+"\""+",\""+personName+"\""+")"
    else:
        currentPdfDataDictionary["Name"] = personName
    currentPdfDataDictionary["Course Type"] = courseType

def TextExtract(currentPageImage):
    # Read Text From Image
    text = OCR.image_to_string(currentPageImage)
    
    # Text Processing Function
    TextProcess(text)

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