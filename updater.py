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
    infosg = str("[i]")
    warnsg = str("[!]")
    try:
        if log == "cleanup":
            if subcat == "begin":
                print(infosg+" Deleting your temporary update files.")
            elif subcat == "done":
                print(infosg+" Done deleting your temporary update files.")
            elif subcat == "none":
                print(warnsg+" There is nothing to clean.")
        elif log == "update":
            if subcat == "begin":
                print(infosg+" Update/Reinstall commence.")
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
                print(infosg+" Update/Reinstall completed.")
        elif log == "restore":
            if subcat == "begin":
                print(infosg+" Restoring your config.py.")
            elif subcat == "done":
                print(infosg+" Done restoring your config.py.")
            elif subcat == "none":
                print(warnsg+" There is no config.py to restore.")
        elif log == "backup":
            if subcat == "begin":
                print(infosg+" Backing up your config.py.")
            elif subcat == "done":
                print(infosg+" Done backing up your config.py.")
            elif subcat == "none":
                print(warnsg+" There is no config.py to back up.")
        elif log == "updateupdater":
            if subcat == "begin":
                print(infosg+" Downloading and installing updater.py for application.")
            elif subcat == "done":
                print(infosg+" Done downloading and installing updater.py for application.")
            elif subcat == "error":
                print(warnsg+" Cannot download and install updater.py for application.")
        elif log == "createlauncher":
            if subcat == "begin":
                print(infosg+" Creating your application launcher.")
            elif subcat == "done":
                print(infosg+" Done creating your application launcher.")
            elif subcat == "error":
                print(warnsg+" Cannot create a launcher file.")
        elif log == "init":
            if subcat == "loadYaml":
                print(infosg+" Loaded configuration from config.yml.")
            elif subcat == "loadOldCfg":
                print(infosg+" Loaded configuration from config.py")
                print(warnsg+" This method of configuring updater.py will be deprecated soon. Please move on to the new config.yml format ASAP.")
        elif log == "notSupported":
            print(warnsg+" Your OS does not support updater.py. The updater will now exit!")
        elif log == "notConfigured":
            print(warnsg+" You have not configured your config.py. The updater will now terminate!")
    except:
        print(warnsg+"logger does not have that!")

try:
    from git import Repo

    from platform import system

    from os import mkdir
    from os.path import isdir
    from os.path import isfile
    from os.path import dirname
    from os.path import join
    from os.path import realpath
    from os import remove
    from os import access
    from os import W_OK
    from os import chmod
    from stat import S_IWUSR
    from stat import S_IXUSR
    from yaml import load
    from yaml import dump

    from shutil import rmtree
    from shutil import copy2
    
    from getpass import getuser

    with open(dirname(realpath(__file__))+"/config.yml", 'r') as config_file:
        config_contents = load(config_file)
    appName = config_contents["appName"]
    appRepo = config_contents["appRepo"]
    appDir = config_contents["appDir"]
    appExecName = config_contents["appExecName"]
    backupOn = config_contents["backupOn"]
    createLaunchScriptOn = config_contents["createLaunchScriptOn"]
    logger("init", "loadYaml")

    configFile = str(appDir+"/config.yml")
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
    elif appExecName == str("Nothing.py"):
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
        logger("updateupdater", "begin")
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
        else:
            logger("notSupported", "")
        logger("updateupdater", "done")          
    except Exception as e:
        logger("updateupdater", "error")
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

            if createLaunchScriptOn == bool(True):
                createLauncherNow()

            logger("update", "done")
        except Exception as e:
            exList(e)

def createLauncherNow():
    try:
        logger("createlauncher", "begin")
        launchScriptGenericDir = str(appDir+"/"+appName)
        if system() == "Windows":
            launchScriptWinDir = str(launchScriptGenericDir+".bat")
            launchScriptWin = open(launchScriptGenericDir+".bat", "w+")
            launchScriptWin.write("python "+appExecName+"\n")
            launchScriptWin.write("pause")
            launchScriptWin.close()
        elif system() == "Linux" or system() == "Darwin":
            launchScriptNixDir = str(launchScriptGenericDir+".sh")
            launchScriptNix = open(launchScriptGenericDir+".sh", "w+")
            launchScriptNix.write("python "+appExecName+"\n")
            launchScriptNix.write("read")
            launchScriptNix.close()
            chmod(launchScriptNixDir, S_IXUSR)
        else:
            logger("notSupported", "")
        logger("createlauncher", "done")
    except Exception as e:
        logger("createlauncher", "error")
        exList(e)

def createConfigNow(name, repo, directory, appExeName, bckOn, createCfgOn):
    try:
        config_dict = dict(
            appName = name,
            appRepo = repo,
            appDir = directory,
            appExecName = appExeName,
            backupOn = bckOn,
            createLaunchScriptOn = createCfgOn
        )
        with open(dirname(realpath(__file__))+"/config.yml", "w") as config_file:
            dump(config_dict, config_file)
    except Exception as e:
        print(str(e))
        exit()

def about():
	print("COnfiguration file version")

#createConfigNow("Nothing", "http://www.example.com/project.git", "Nothing", "Nothing.py", False, False)