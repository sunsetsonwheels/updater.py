def exList(ex):
    ex_str = str(ex)
    print("During the usage of updater.py, we've encountered some errors. Here's the traceback:")
    print("======================================================================================")
    print(ex_str)
    print("======================================================================================")
    print("Please do the following:")
    print("- If you're getting errors about config, reread your config file.")
    print("- Make sure you have installed all the dependencies. Read README.md for more info.")
    print("If nothing works, please create a new issue on GitHub: https://github.com/jkelol111/updater.py/issues")

try:
    import git
    import os
    from shutil import rmtree
    import config as cfg
    appName = cfg.appName
    appRepo = cfg.appRepo
    appDir = cfg.appDir
    backupOn = cfg.backupOn
    backupDir = cfg.backupDir
except Exception as e:
    exList(e)

def ConfigUtils():
    print(appName)

def updateNow():
    print("working on porting the code from tkbillboard.py's updater. stay tuned, gotta go to bed.")
    try:
        print("Update/Reinstall running.")
        print("[1/2] Downloading new version of application.")
        git.Git(appDir).clone(appRepo)
        print("[2/2] Downloading and installing new version of application")
        os.mkdir(app_path)
        print("Update/Reinstall completed.")
    except Exception as e:
        exList(e)