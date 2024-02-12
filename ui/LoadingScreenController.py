from config.Configuration import SystemSetup, WorkspaceSetup, ClearCache

def InitProcesses():

    # Setup OS Parameters
    SystemSetup()

    # Clear App Cache
    ClearCache()

    # Setup Workspace Folders and Files
    WorkspaceSetup()