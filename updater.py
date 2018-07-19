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

try:
    from git import Repo
    from os import mkdir
    from os import name
    from shutil import rmtree
    from shutil import copy2
    from getpass import getuser

    import config as cfg
    appName = cfg.appName
    appRepo = cfg.appRepo
    appExecName = cfg.appExecName
    appDir = cfg.appDir
    backupOn = cfg.backupOn

    configDir = str(appDir+"/config.py")
    username = getuser()
    tmpBackupDirWin = str("C:/Users/"+username+"/.tmp_updater")
    tmpBackupDirNix = str("/home/"+username+"/.tmp_updater")

    configured = bool(False)
except Exception as e:
    exList(e)

def checkConfig():
    global configured
    if appName == "Nothing":
        configured = bool(False)
    elif appRepo == "http://www.example.com/project.git":
        configured = bool(False)
    elif appExecName == "config.py":
        configured = bool(False)
    elif appDir == "Nothing":
        configured = bool(False)
    else:
        configured = bool(True)

def restoreConfigNow():
    try:
        if name == "windows":
            bckConfigDirWin = str(tmpBackupDirWin+"/config.py")
            copy2(bckConfigDirWin, appDir)
        elif name == "posix":
            bckConfigDirNix = str(tmpBackupDirNix+"/config.py")
            copy2(bckConfigDirNix, appDir)
        else:
            print("updater.py cannot be run on your PC. The updater will now terminate!")
            exit()
    except Exception as e:
        print("There isn't anything to clean up.")
        exList(e)

def backupConfigNow():
    print("[1.5/2] Backing up your configuration file.")
    if name == "windows":
        mkdir(tmpBackupDirWin)
        copy2(configDir, tmpBackupDirWin)
    elif name == "posix":
        mkdir(tmpBackupDirNix)
        copy2(configDir, tmpBackupDirNix)
    else:
        print("updater.py cannot be run on your PC. The updater will now terminate!")
        exit()
    rmtree(appDir)

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
                backupConfigNow()

            print("[2/2] Downloading and installing new version of application.")
            mkdir(appDir)
            Repo.clone_from(appRepo, appDir)

            print("[2.5/2] Restoring app configuration files.")
            restoreConfigNow()

            print("Update/Reinstall completed.")
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

def configureConfigNow(name, repo, dir, bckOn):
    print("[!] This function does not work yet!")