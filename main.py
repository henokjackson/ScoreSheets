from ui.views import LoadingScreen, MainScreen

if __name__ == "__main__":
    # Load Splash Screen
    LoadingScreen.Render()

    # Render Main Screen
    MainScreen.Render()

    ''' UNDER DEVELOPMENT !!
        # Customize Marking Scheme
        if globals.isMarksCustomized: CustomizeMarks()
    '''