import globals
from TextProcessing import ParseWeeks
from ImageProcessing import CropImage, ScaleImage

def LoadKTUScheme():
    
    # Setting Marking Scheme
    globals.week1Score = 3
    globals.week2Score = 6
    globals.week3Score = 12
    globals.week6Score = 25
    globals.week12Score = 50

def CustomizeMarks():

    # Setting Marking Scheme
    globals.week12Score = int(input("INPUT MARKS FOR WEEK > or = 12 WEEKS : "))
    globals.week6Score = int(input("INPUT MARKS FOR WEEK > or = 6 WEEKS : "))
    globals.week3Score = int(input("INPUT MARKS FOR WEEK > or = 3 WEEKS : "))
    globals.week2Score = int(input("INPUT MARKS FOR WEEK > or = 2 WEEKS : "))
    globals.week1Score = int(input("INPUT MARKS FOR WEEK > or = 1 WEEK : "))

def ScoreCalculator(courseDuration):
    
    courseDurationClone = courseDuration
    totalScore = 0

    while(courseDurationClone >= 12):
        totalScore += globals.week12Score
        courseDurationClone -= 12
        
    while(courseDurationClone >= 6):
        totalScore += globals.week6Score
        courseDurationClone -= 6

    while(courseDurationClone >= 3):
        totalScore += globals.week3Score
        courseDurationClone -= 3
    
    while(courseDurationClone >= 2):
        totalScore += globals.week2Score
        courseDurationClone -= 2
    
    while(courseDurationClone >= 1):
        totalScore += globals.week1Score
        courseDurationClone -= 1

    return totalScore

def ScoreAggregator():
    if not globals.currentPdfDataList:
        globals.currentPdfDataList.append(globals.currentPdfDataDictionary)
    else:
        IsPersonDataExisting = False

        # Aggregating Scores of Same Type of Courses Taken By The Same Person
        for index, currentPdfDataListDictionaryItem in enumerate(globals.currentPdfDataList, 0):
            if(currentPdfDataListDictionaryItem["Name"] == globals.currentPdfDataDictionary["Name"] and currentPdfDataListDictionaryItem["Course Type"] == globals.currentPdfDataDictionary["Course Type"]):
                globals.currentPdfDataDictionary["Current Score"] += currentPdfDataListDictionaryItem["Current Score"]
                globals.currentPdfDataDictionary["Duration"] += currentPdfDataListDictionaryItem["Duration"]
                globals.currentPdfDataList[index] = globals.currentPdfDataDictionary
                IsPersonDataExisting = True
                break
        # Append Data of New Person
        if not IsPersonDataExisting: globals.currentPdfDataList.append(globals.currentPdfDataDictionary)

def GetCourseDuration(preprocessedpdfCurrentPageImage):
    # Crop The Required Area 
    preprocessedpdfCurrentPageImage = CropImage(preprocessedpdfCurrentPageImage) 
    
    # Scale Image To Required Size
    preprocessedpdfCurrentPageImage = ScaleImage(preprocessedpdfCurrentPageImage)

    # Parse Course Duration From Pre-Processed Image
    courseDuration = ParseWeeks(preprocessedpdfCurrentPageImage)

    # Set Course Duration
    globals.currentPdfDataDictionary["Duration"] = courseDuration

    # Calculate Score
    totalScore = ScoreCalculator(courseDuration)
    
    # Set Scores
    globals.currentPdfDataDictionary["Current Score"] = totalScore