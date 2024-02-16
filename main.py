from ui import LoadingScreen, MainScreen
from file_handling.FileIO import CSVWriter
from score_calculation.ScoreCalculation import CustomizeMarks
if __name__ == "__main__":
    # Load Splash Screen
    LoadingScreen.Start()

    # Render Main Screen
    MainScreen.Start()

    ''' UNDER DEVELOPMENT !!
        # Customize Marking Scheme
        if globals.isMarksCustomized: CustomizeMarks()
    '''
    
    # Write Results to CSV File
    CSVWriter()