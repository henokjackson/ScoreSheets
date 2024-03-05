from ui.views import LoadingScreen, MainScreen

if __name__ == "__main__":
    # Load Splash Screen
    LoadingScreen.Start()

    # Render Main Screen
    MainScreen.Start()

    ''' UNDER DEVELOPMENT !!
        # Customize Marking Scheme
        if globals.isMarksCustomized: CustomizeMarks()
    '''