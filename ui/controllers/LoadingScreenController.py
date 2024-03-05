from config import Globals
from threading import Thread
from process_handler.InitializationProcesses import InitProcesses

def Loading(Form, ui, timer):
    loadingOptions = ["Loading assets...", "Loading coniguration...", "Clearing up cache...", "Setting up workspace...", "Loading marking schemes..." ]
    
    if Globals.loadingScreenInfoListIndex < len(loadingOptions):
        ui.loading_label.setText(loadingOptions[Globals.loadingScreenInfoListIndex])
        Globals.loadingScreenInfoListIndex = Globals.loadingScreenInfoListIndex + 1
    else:
        timer.stop()
        Form.close()
        Globals.loadingScreenInfoListIndex = 0
        return
    
def StartProcesses(app):
    # InitProcesses Thread
    InitProcesses_Thread = Thread(target = InitProcesses, name = 'InitProcessesThread - LoadingScreen')
    InitProcesses_Thread.start()
    app.exec_()
    InitProcesses_Thread.join()