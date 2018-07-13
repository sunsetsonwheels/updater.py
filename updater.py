def exList(ex):
    ex_str = str(ex)
    print("During the usage of updater.py, we've encountered some errors. Here's the exception:")
    print("======================================================================================")
    print(ex_str)
    print("======================================================================================")
    print("Please do the following:")
    print("- If you're getting errors about config, reread your config file.")
    print("- Make sure you have installed all the dependencies. Read README.md for more info.")
    print("If nothing works, please create a new issue on GitHub: https://github.com/jkelol111/updater.py/issues")
    exit()

try:
    from git import Repo
    from os import mkdir
    from os import name
    from shutil import rmtree
    from shutil import copy2
    from shutil import copytree
    from getpass import getuser

    import config as cfg
    appName = cfg.appName
    appRepo = cfg.appRepo
    appExecName = cfg.appExecName
    appDir = cfg.appDir
    backupOn = cfg.backupOn
    backupDir = cfg.backupDir

    configDir = str(appDir+"/config.py")
    extBackupDir =  str(appDir+backupDir)
    username = getuser()
    tmpBackupDirWin = str("C:/Users/"+username+"/.tmp_updater")
    tmpBackupDirNix = str("/home/"+username+"/.tmp_updater")

    configured = bool(False)
except Exception as e:
    exList(e)

def checkConfig():
    if appName == "Nothing":
        configured = bool(False)
    elif appRepo == "http://www.example.com/project.git":
        configured = bool(False)
    elif appExecName == "config.py":
        configured = bool(False)
    elif appDir == "Nothing":
        configured = bool(False)
    elif backupDir == "Nothing":
        configured = bool(False)
    else:
        configured = bool(True)

def backupNow():
    checkConfig()
    print("[1.5/2] Backing up your application.")
    if configured == bool(False):
        print("You have not configured your config.py. The updater will now terminate!")
        exit()
    elif configured == bool(True):
        try:
            if name == "windows":
                mkdir(tmpBackupDirWin)
                copytree(appDir, tmpBackupDirWin)
                copy2(configDir, tmpBackupDirWin)
                copytree(appDir, tmpBackupDirWin)
            elif name == "posix":
                mkdir(tmpBackupDirNix)
                copytree(appDir, tmpBackupDirNix)
                copy2(configDir, tmpBackupDirNix)
                copytree(backupDir, tmpBackupDirNix)
            else:
                print("updater.py cannot be run on your PC. The updater will now terminate!")
                exit()
        except Exception as e:
            exList(e)

def updateNow():
    checkConfig()
    if configured == bool(False):
        print("You have not configured your config.py. The updater will now terminate!")
        exit()
    elif configured == bool(True):
        try:
            print("Update/Reinstall running.")
            print("[1/2] Emptying folder of application.")
            if backupOn == bool(False):
                rmtree(appDir)
            elif backupOn == bool(True):
                backupNow()
                rmtree(appDir)
                
            print("[2/2] Downloading and installing new version of application.")
            mkdir(appDir)
            Repo.clone_from(appRepo, appDir)

            print("Update/Reinstall completed.")
        except Exception as e:
            exList(e)

def revertUpdateNow():
    if backupOn == 0:
        print("The update cannot be reverted, since nothing is backed up.")
    elif backupOn == 1:
        try:
            rmtree(appDir)
            if name == "windows":
                copytree(tmpBackupDirWin, tmpBackupDirWin)
                copy2(tmpBackupDirWin+"/config.py", tmpBackupDirWin)
                copytree(appDir, tmpBackupDirWin)
            elif name == "posix":
                mkdir(tmpBackupDirNix)
                copytree(appDir, tmpBackupDirNix)
                copy2(configDir, tmpBackupDirNix)
                copytree(backupDir, tmpBackupDirNix)
            else:
                print("updater.py cannot be run on your PC. The updater will now terminate!")
                exit()
        except Exception as e:
            exList(e)

def cleanupNow():
    try:
        if name == "windows":
            rmtree(tmpBackupDirWin)
        elif name == "posix":
            rmtree(tmpBackupDirNix)
        else:
            print("updater.py cannot be run on your PC. The updater will now terminate!")
            exit()
    except Exception as e:
        print("There isn't anything to clean up.")
        exList(e)