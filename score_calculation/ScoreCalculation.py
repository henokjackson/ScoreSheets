currentPdfDataDictionary = {}
currentPdfDataList = []

week12Score = 0
week6Score = 0 
week3Score = 0 
week2Score = 0 
week1Score = 0

def LoadKTUScheme():
    global week12Score, week6Score, week3Score, week2Score, week1Score
    
    # Setting Marking Scheme
    week1Score = 3
    week2Score = 6
    week3Score = 12
    week6Score = 25
    week12Score = 50

def CustomizeMarks():
    global week12Score, week6Score, week3Score, week2Score, week1Score

    # Setting Marking Scheme
    week12Score = int(input("INPUT MARKS FOR WEEK > or = 12 WEEKS : "))
    week6Score = int(input("INPUT MARKS FOR WEEK > or = 6 WEEKS : "))
    week3Score = int(input("INPUT MARKS FOR WEEK > or = 3 WEEKS : "))
    week2Score = int(input("INPUT MARKS FOR WEEK > or = 2 WEEKS : "))
    week1Score = int(input("INPUT MARKS FOR WEEK > or = 1 WEEK : "))

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
        totalScore += week3Score
        courseDurationClone -= 3
    
    while(courseDurationClone >= 2):
        totalScore += week2Score
        courseDurationClone -= 2
    
    while(courseDurationClone >= 1):
        totalScore += week1Score
        courseDurationClone -= 1

    return totalScore

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