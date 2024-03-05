import os
import signal
from config import Globals

def RefreshProgressBar(ui, timer, dialog):
    ui.process_progressBar.setValue(int(Globals.progressBarPercentage))
    ui.filename_label.setText(Globals.currentFileName)
    ui.fileno_label.setText(str(Globals.currentFileNo))
    #print("Progress Bar Updated !")

    if Globals.progressBarPercentage == 100 :
        timer.stop()
        dialog.close()
        
def Abort():
    print("Aborted !")
    os.kill(Globals.mainProcessesThreadNativeId, signal.SIGTERM)