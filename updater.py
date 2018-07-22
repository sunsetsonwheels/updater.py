def exList(ex):
    ex_str = str(ex)
    from platform import python_version
    print("During the usage of updater.py, we've encountered some errors. Here's the exception:")
    print("======================================================================================")
    print(ex_str)
    print("======================================================================================")
    print("System information:")
    print("======================================================================================")
    print(System)
    print("======================================================================================")
    print("Please do the following:")
    print("- If you're getting errors about config, reread your config file.")
    print("- Make sure you have installed all the dependencies. Read README.md for more info.")
    print("If nothing works, please create a new issue on GitHub: https://github.com/jkelol111/updater.py/issues")
    exit()

try:
    from git import Repo

    from platform import system

    from os import mkdir
    from os.path import isdir
    from os.path import isfile
    from os import remove
    from os import access
    from os import W_OK
    from os import chmod
    from stat import S_IWUSR

    from shutil import rmtree
    from shutil import copy2
    
    from getpass import getuser

    import config as cfg
    appName = cfg.appName
    appRepo = cfg.appRepo
    appDir = cfg.appDir
    backupOn = cfg.backupOn

    configDir = str(appDir+"/config.py")
    updaterDir = str(appDir+"/updater.py")
    username = getuser()
    tmpBackupDirWin = str("C:/Users/"+username+"/.tmp_updater")
    tmpBackupDirNix = str("/home/"+username+"/.tmp_updater")

    configured = bool(False)
except Exception as e:
    exList(e)

def onerrorPatch(func, path, exc_info):
    if not access(path, W_OK):
        chmod(path, S_IWUSR)
        func(path)

def checkConfig():
    global configured
    if appName == "Nothing":
        configured = bool(False)
    elif appRepo == "http://www.example.com/project.git":
        configured = bool(False)
    elif appDir == "Nothing":
        configured = bool(False)
    else:
        configured = bool(True)

def cannotRun():
    print("[!] updater.py cannot be run on your PC. The updater will now terminate!")
    exit()

def cleanupNow():
    try:
        if name == "nt":
            if isdir(tmpBackupDirWin) == bool(True):
                rmtree(tmpBackupDirWin, onerror=onerrorPatch)
        elif name == "posix":
            if isdir(tmpBackupDirNix) == bool(True):
                rmtree(tmpBackupDirNix)
        else:
            cannotRun()
    except Exception as e:
        print("There isn't anything to clean up.")
        exList(e)

def restoreConfigNow():
    try:
        if name == "nt":
            if isdir(tmpBackupDirWin) == bool(True):
                bckConfigDirWin = str(tmpBackupDirWin+"/config.py")
                copy2(bckConfigDirWin, appDir)
        elif name == "posix":
            if isdir(tmpBackupDirNix) == bool(True):
                bckConfigDirNix = str(tmpBackupDirNix+"/config.py")
                copy2(bckConfigDirNix, appDir)
        else:
            cannotRun()
    except Exception as e:
        exList(e)

def backupConfigNow():
    cleanupNow()
    try:
        if name == "nt":
            mkdir(tmpBackupDirWin)
            copy2(configDir, tmpBackupDirWin)
        elif name == "posix":
            mkdir(tmpBackupDirNix)
            copy2(configDir, tmpBackupDirNix)
        else:
            cannotRun()
    except Exception as e:
        exList(e)

def updateUpdaterNow():
    updaterRepoGit = str("https://github.com/jkelol111/updater.py.git")
    if isfile(updaterDir) == bool(True):
        remove(updaterDir)
    if name == "nt":
        updaterUpdatedDirWin = str(tmpBackupDirWin+"/updaterpy")
        if isdir(updaterUpdatedDirWin) == bool(True):
            rmtree(updaterUpdatedDirWin, onerror=onerrorPatch)
        mkdir(updaterUpdatedDirWin)
        Repo.clone_from(updaterRepoGit, updaterUpdatedDirWin)
        updaterUpdatedFileWin = str(updaterUpdatedDirWin+"/updater.py")
        copy2(updaterUpdatedFileWin, appDir)
    elif name == "posix":
        updaterUpdatedDirNix = str(tmpBackupDirNix+"/updaterpy")
        if isdir(updaterUpdatedDirNix) == bool(True):
            rmtree(updaterUpdatedDirNix)
        mkdir(updaterUpdatedDirNix)
        Repo.clone_from(updaterRepoGit, updaterUpdatedDirNix)
        updaterUpdatedFileNix = str(updaterUpdatedDirNix+"/updater.py")
        copy2(updaterUpdatedFileNix, appDir)

def updateNow():
    checkConfig()
    if configured == bool(False):
        print("You have not configured your config.py. The updater will now terminate!")
        exit()
    elif configured == bool(True):
        try:
            print("Update/Reinstall running.")
            print("[1/3] Emptying folder of application.")
            if backupOn == bool(True):
                print("[1.5/3] Backing up config.py of application.")
                backupConfigNow()
            rmtree(appDir, onerror=onerrorPatch)

            print("[2/3] Downloading and installing new version of application.")
            mkdir(appDir)
            Repo.clone_from(appRepo, appDir)

            if backupOn == bool(True):
                print("[2.5/3] Restoring app configuration files.")
                restoreConfigNow()

            print("[3/3] Downloading and installing updater.py for application.")
            updateUpdaterNow()

            print("Update/Reinstall completed.")
        except Exception as e:
            exList(e)

def configureConfigNow(name, repo, directory, bckOn):
    try:
        configFileWrite = open(configDir, 'w')
        configFileWrite.write("appName = '"+name+"'")
        configFileWrite.write("appRepo = '"+repo+"'")
        configFileWrite.write("appDir = '"+directory+"'")
        configFileWrite.write("backupOn = "+bckOn)
        configFileWrite.close()
    except Exception as e:
        exList(e)