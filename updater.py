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
    import os
    from shutil import rmtree
    import config as cfg
    appName = cfg.appName
    appRepo = cfg.appRepo
    appExecName = cfg.appExecName
    appDir = cfg.appDir
    backupOn = cfg.backupOn
    backupDir = cfg.backupDir
except Exception as e:
    exList(e)

def updateNow():
    print("[!] This program is extremely unstable. Exceptions are nearly certain to occur.")
    if appRepo == "http://www.example.com/project.git":
        print("You have not configured your config.py. The updater will now terminate!")
        exit()
    else:
        try:
            print("Update/Reinstall running.")
            print("[1/3] Emptying folder of application.")
            rmtree(appDir)
            print("[2/3] Downloading new version of application.")
            os.mkdir(appDir)
            Repo.clone_from(appRepo, appDir)
            print("[3/3] Installing new version of application.")
            #newAppDir = os.path.abspath(appDir+"/"+appExecName) 
            #exec(newAppDir)
            print("Update/Reinstall completed.")
        except Exception as e:
            exList(e)