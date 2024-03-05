from score_calculation.ScoreCalculation import LoadKTUScheme
from config.Configuration import SystemSetup, WorkspaceSetup, ClearCache

def InitProcesses():
    # Setup OS Parameters
    SystemSetup()

    # Clear App Cache
    ClearCache()
    
    # Setup Workspace Folders and Files
    WorkspaceSetup()

    # Load Default Marking Scheme (KTU)
    LoadKTUScheme()