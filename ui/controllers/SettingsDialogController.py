from config import Globals
from multiprocessing import cpu_count

def ApplySettings(ui):
    noOfThreads = int(ui.noofthreads_lineEdit.text())
    if noOfThreads > cpu_count():
        ui.ThreadCountExceededErrorMessage()
    else:
        Globals.noOfThreads = noOfThreads
        Globals.markingSchemeFilePath = ui.markingschemefile_lineEdit.text()
        Globals.outputFileName = ui.outputfilename_lineEdit.text()