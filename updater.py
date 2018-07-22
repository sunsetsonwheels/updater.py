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

def logger(log, subcat):
    try:
        if log == "cleanup":
            if subcat == "begin":
                print("[i] Deleting your temporary update files.")
            elif subcat == "done":
                print("[i] Done deleting your temporary update files.")
            elif subcat == "none":
                print("[!] There is nothing to clean.")
        elif log == "update":
            if subcat == "begin":
                print("[i] Update/Reinstall commence.")
            elif subcat == "step1":
                print("[1/3] Emptying folder of application.")
            elif subcat == "step1.5":
                print("[1.5/3] Backing up config.py of application.")
            elif subcat == "step2":
                print("[2/3] Downloading and installing new version of application.")
            elif subcat == "step2.5":
                print("[2.5/3] Restoring app configuration files.")
            elif subcat == "step3":
                print("[3/3] Downloading and installing updater.py for application.")
            elif subcat == "done":
                print("[i] Update/Reinstall completed.")
        elif log == "restore":
            if subcat == "begin":
                print("[i] Restoring your config.py.")
            if subcat == "done":
                print("[i] Done restoring your config.py.")
            if subcat == "none":
                print("[!] There is no config.py to restore.")
        elif log == "backup":
            if subcat == "begin":
                print("[i] Backing up your config.py.")
            if subcat == "done":
                print("[i] Done backing up your config.py.")
            if subcat == "none":
                print("[!] There is no config.py to back up.")
        elif log == "notSupported":
            print("[!] Your OS does not support updater.py. The updater will now exit!")
        elif log == "notConfigured":
            print("[!] You have not configured your config.py. The updater will now terminate!")
    except:
        print("logger does not have that!")

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

    configFile = str(appDir+"/config.py")
    updaterFile = str(appDir+"/updater.py")
    username = getuser()
    tmpBackupDirWin = str("C:/Users/"+username+"/.tmp_updater")
    tmpBackupDirNix = str("/home/"+username+"/.tmp_updater")
    tmpBackupDirOSX = str("/Users/"+username+"/.tmp_updater")

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

def cleanupNow():
    try:
        logger("cleanup", "begin")
        if system() == "Windows":
            if isdir(tmpBackupDirWin) == bool(True):
                rmtree(tmpBackupDirWin, onerror=onerrorPatch)
            elif isdir(tmpBackupDirWin) == bool(False):
                logger("cleanup", "none")
        elif system() == "Linux":
            if isdir(tmpBackupDirNix) == bool(True):
                rmtree(tmpBackupDirNix)
            elif isdir(tmpBackupDirNix) == bool(False):
                logger("cleanup", "none")
        elif system() == "Darwin":
            if isdir(tmpBackupDirOSX) == bool(True):
                rmtree(tmpBackupDirOSX)
            elif isdir(tmpBackupDirOSX) == bool(False):
                logger("cleanup", "none")
        else:
            logger("notSupported", "")
        logger("cleanup", "done")
    except Exception as e:
        exList(e)

def restoreConfigNow():
    try:
        logger("restore", "begin")
        if system() == "Windows":
            bckconfigFileWin = str(tmpBackupDirWin+"/config.py")
            if isfile(bckconfigFileWin) == bool(True):
                copy2(bckconfigFileWin, appDir)
            elif isfile(bckconfigFileWin) == bool(False):
                logger("restore", "none")
        elif system() == "Linux":
            bckconfigFileNix = str(tmpBackupDirNix+"/config.py")
            if isfile(bckconfigFileNix) == bool(True):
                copy2(bckconfigFileNix, appDir)
            elif isfile(bckconfigFileNix) == bool(False):
                logger("restore", "none")
        elif system() == "Darwin":
            bckconfigFileOSX = str(tmpBackupDirOSX+"/config.py")
            if isfile(bckconfigFileOSX) == bool(True):
                copy2(bckconfigFileOSX, appDir)
            elif isfile(bckconfigFileOSX) == bool(False):
                logger("restore", "none")
        else:
            logger("notSupported", "")
        logger("restore", "done")
    except Exception as e:
        exList(e)

def backupConfigNow():
    cleanupNow()
    try:
        logger("backup", "begin")
        if system() == "Windows":
            mkdir(tmpBackupDirWin)
            if isfile(configFile) == bool(True):
                copy2(configFile, tmpBackupDirWin)
            elif isfile(configFile) == bool(False):
                logger("backup", "none")
        elif system() == "Linux":
            mkdir(tmpBackupDirNix)
            if isfile(configFile) == bool(True):
                copy2(configFile, tmpBackupDirNix)
            elif isfile(configFile) == bool(False):
                logger("backup", "none")
        elif system() == "Darwin":
            mkdir(tmpBackupDirWin)
            if isfile(configFile) == bool(True):
                copy2(configFile, tmpBackupDirWin)
            elif isfile(configFile) == bool(False):
                logger("backup", "none")
        else:
            logger("notSupported", "")
        logger("backup", "done")
    except Exception as e:
        exList(e)

def updateUpdaterNow():
    updaterRepoGit = str("https://github.com/jkelol111/updater.py.git")
    try:
        logger("updateUpdater", "begin")
        if isfile(updaterFile) == bool(True):
            remove(updaterFile)
        if system() == "Windows":
            updaterUpdatedDirWin = str(tmpBackupDirWin+"/updaterpy")
            if isdir(updaterUpdatedDirWin) == bool(True):
                rmtree(updaterUpdatedDirWin, onerror=onerrorPatch)
            mkdir(updaterUpdatedDirWin)
            Repo.clone_from(updaterRepoGit, updaterUpdatedDirWin)
            updaterUpdatedFileWin = str(updaterUpdatedDirWin+"/updater.py")
            copy2(updaterUpdatedFileWin, appDir)
        elif system() == "Linux":
            updaterUpdatedDirNix = str(tmpBackupDirNix+"/updaterpy")
            if isdir(updaterUpdatedDirNix) == bool(True):
                rmtree(updaterUpdatedDirNix)
            mkdir(updaterUpdatedDirNix)
            Repo.clone_from(updaterRepoGit, updaterUpdatedDirNix)
            updaterUpdatedFileNix = str(updaterUpdatedDirNix+"/updater.py")
            copy2(updaterUpdatedFileNix, appDir)
        elif system() == "Darwin":
            updaterUpdatedDirOSX = str(tmpBackupDirOSX+"/updaterpy")
            if isdir(updaterUpdatedDirOSX) == bool(True):
                rmtree(updaterUpdatedDirOSX)
            mkdir(updaterUpdatedDirOSX)
            Repo.clone_from(updaterRepoGit, updaterUpdatedDirOSX)
            updaterUpdatedFileOSX = str(updaterUpdatedDirOSX+"/updater.py")
            copy2(updaterUpdatedFileOSX, appDir)
        logger("updateUpdater", "done")          
    except Exception as e:
        logger("notSupported", "")
        exList(e)

def updateNow():
    checkConfig()
    if configured == bool(False):
        logger("notConfigured", "")
        exit()
    elif configured == bool(True):
        try:
            logger("update", "begin")

            logger("update", "step1")
            if backupOn == bool(True):
                logger("update", "step1.5")
                backupConfigNow()
            rmtree(appDir, onerror=onerrorPatch)

            logger("update", "step2")
            mkdir(appDir)
            Repo.clone_from(appRepo, appDir)

            if backupOn == bool(True):
                logger("update", "step2.5")
                restoreConfigNow()

            logger("update", "step3")
            updateUpdaterNow()

            logger("update", "done")
        except Exception as e:
            exList(e)

def configureConfigNow(name, repo, directory, bckOn):
    try:
        configFileWrite = open(configFile, 'w')
        configFileWrite.write("appName = '"+name+"'")
        configFileWrite.write("appRepo = '"+repo+"'")
        configFileWrite.write("appDir = '"+directory+"'")
        configFileWrite.write("backupOn = "+bckOn)
        configFileWrite.close()
    except Exception as e:
        exList(e)