from config import Globals
from threading import Thread
from process_handling import InitializationProcesses

def Loading(Form, ui, timer):    
    if Globals.loadingScreenInfoListIndex < len(Globals.loadingOptions):
        ui.loading_label.setText(Globals.loadingOptions[Globals.loadingScreenInfoListIndex])
        Globals.loadingScreenInfoListIndex = Globals.loadingScreenInfoListIndex + 1
    else:
        timer.stop()
        Form.close()
        Globals.loadingScreenInfoListIndex = 0
        return
    
def ExecuteInitializationProcessesThread(app):
    InitializationProcessesThread = Thread(target = InitializationProcesses.ExecuteProcesses, name = 'Initialization Processes Thread')
    InitializationProcessesThread.start()
    app.exec_()
    InitializationProcessesThread.join()