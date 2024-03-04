from config import Globals
from text_processing.TextProcessing import ParseWeeks
from image_processing.ImageProcessing import CropImage, ScaleImage

def LoadKTUScheme():
    # Setting Marking Scheme
    Globals.week1Score = 3
    Globals.week2Score = 6
    Globals.week3Score = 12
    Globals.week6Score = 25
    Globals.week12Score = 50

def CustomizeMarks():
    # Setting Marking Scheme
    Globals.week12Score = int(input("INPUT MARKS FOR WEEK > or = 12 WEEKS : "))
    Globals.week6Score = int(input("INPUT MARKS FOR WEEK > or = 6 WEEKS : "))
    Globals.week3Score = int(input("INPUT MARKS FOR WEEK > or = 3 WEEKS : "))
    Globals.week2Score = int(input("INPUT MARKS FOR WEEK > or = 2 WEEKS : "))
    Globals.week1Score = int(input("INPUT MARKS FOR WEEK > or = 1 WEEK : "))

def ScoreCalculator(courseDuration):
    courseDurationClone = courseDuration
    totalScore = 0

    while(courseDurationClone >= 12):
        totalScore += Globals.week12Score
        courseDurationClone -= 12
        
    while(courseDurationClone >= 6):
        totalScore += Globals.week6Score
        courseDurationClone -= 6

    while(courseDurationClone >= 3):
        totalScore += Globals.week3Score
        courseDurationClone -= 3
    
    while(courseDurationClone >= 2):
        totalScore += Globals.week2Score
        courseDurationClone -= 2
    
    while(courseDurationClone >= 1):
        totalScore += Globals.week1Score
        courseDurationClone -= 1

    return totalScore

def ScoreAggregator():
    if not Globals.currentPdfDataList:
        Globals.currentPdfDataList.append(Globals.currentPdfDataDictionary)
    else:
        IsPersonDataExisting = False
        # Aggregating Scores of Same Type of Courses Taken By The Same Person
        for index, currentPdfDataListDictionaryItem in enumerate(Globals.currentPdfDataList, 0):
            if(currentPdfDataListDictionaryItem["Name"] == Globals.currentPdfDataDictionary["Name"] and currentPdfDataListDictionaryItem["Course Type"] == Globals.currentPdfDataDictionary["Course Type"]):
                Globals.currentPdfDataDictionary["Current Score"] += currentPdfDataListDictionaryItem["Current Score"]
                Globals.currentPdfDataDictionary["Duration"] += currentPdfDataListDictionaryItem["Duration"]
                Globals.currentPdfDataList[index] = Globals.currentPdfDataDictionary
                IsPersonDataExisting = True
                break
        # Append Data of New Person
        if not IsPersonDataExisting: Globals.currentPdfDataList.append(Globals.currentPdfDataDictionary)

def GetCourseDuration(preprocessedpdfCurrentPageImage):
    # Crop The Required Area 
    preprocessedpdfCurrentPageImage = CropImage(preprocessedpdfCurrentPageImage) 
    
    # Scale Image To Required Size
    preprocessedpdfCurrentPageImage = ScaleImage(preprocessedpdfCurrentPageImage)

    # Parse Course Duration From Pre-Processed Image
    courseDuration = ParseWeeks(preprocessedpdfCurrentPageImage)

    # Set Course Duration
    Globals.currentPdfDataDictionary["Duration"] = courseDuration

    # Calculate Score
    totalScore = ScoreCalculator(courseDuration)
    
    # Set Scores
    Globals.currentPdfDataDictionary["Current Score"] = totalScore