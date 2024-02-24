import os
from config import globals
def Banner():
    os.system(globals.clearScreenCommand)
    print("█"*50)
    print("██"+"\t"*6+"██")
    print("██"+"\t"*2+"ScoreSheets v1.0"+"\t"*2+"██")
    print("██"+"\t"*6+"██")
    print("█"*50)

def ProgressBar(current, total):
    os.system(globals.clearScreenCommand)
    progress = (current / total) * 10
    print("Progress: [", "█" * int(progress), " " * (10 - int(progress)), "\b] ~ ", int(progress * 10), "%")
    print("\nItem No. --> ", current, "\nFilename --> ", globals.pdfFileName)

    return int(progress * 10), globals.pdfFileName, int(current)