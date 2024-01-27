import os

clearScreenCommand = ''
pdfFileName = ''

def Banner():
    os.system(clearScreenCommand)
    print("█"*50)
    print("██"+"\t"*6+"██")
    print("██"+"\t"*2+"ScoreSheets v1.0"+"\t"*2+"██")
    print("██"+"\t"*6+"██")
    print("█"*50)

def ProgressBar(current, total):
    os.system(clearScreenCommand)
    progress = (current/total)*10
    print("Progress: [", "█"*int(progress), " "*(10-int(progress)), "\b] ~", int(progress*10), "%")
    print("\nItem No. => ", current, "\nFilename => ", pdfFileName)