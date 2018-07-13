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
    #import yaml
    import config as cfg
    appName = cfg.appName
    appRepo = cfg.appRepo
    appExecName = cfg.appExecName
    appDir = cfg.appDir
    backupOn = cfg.backupOn
    backupDir = cfg.backupDir
except Exception as e:
    exList(e)

def cleanupNow():
    if name == "windows":
        tmpBackupDirWin = str("C:/Users/"+username+"/.tmp_updater")
        rmtree(tmpBackupDirWin)
    elif name == "posix":
        tmpBackupDirNix = str("~/.tmp_updater")
        rmtree(tmpBackupDirNix)

def backupNow():
    exConfigDir = join(appDir+"config.py")
    exBackupDir = join(appDir+backupDir)
    username = getuser()
    if name == "windows":
        tmpBackupDirWin = str("C:/Users/"+username+"/.tmp_updater")
        mkdir(tmpBackupDirWin)
        copy2(exConfigDir, tmpBackupDirWin)
        copytree(exBackupDir, tmpBackupDirWin)
    elif name == "posix":
        tmpBackupDirNix = str("/home/"+username+"/.tmp_updater")
        mkdir(tmpBackupDirNix)
        copy2(exConfigDir, tmpBackupDirNix)
        copytree(exBackupDir, tmpBackupDirNix)
    else:
        print("updater.py cannot be run on your PC. The updater will now terminate!")
        exit()

def updateNow():
    print("[!] This program is extremely unstable. Exceptions are nearly certain to occur.")
    if appRepo == "http://www.example.com/project.git":
        print("You have not configured your config.py. The updater will now terminate!")
        exit()
    else:
        try:
            print("Update/Reinstall running.")
            print("[1/3] Emptying folder of application.")
            if backupOn == 0:
                rmtree(appDir)
            elif backupOn == 1:
                backupNow()
                rmtree(appDir)
                
            print("[2/3] Downloading new version of application.")
            mkdir(appDir)
            Repo.clone_from(appRepo, appDir)

            print("[3/3] Installing new version of application.")
            rmtree(appDir+"/.git")

            #newAppDir = os.path.abspath(appDir+"/"+appExecName) 
            #exec(newAppDir)
            print("Update/Reinstall completed.")
        except Exception as e:
            exList(e)

def removeUpdateNow():
    if backupOn == 0:
        print("The update cannot be reverted, since nothing is backed up.")
    elif backupOn == 1:
        rmtree(appDir)