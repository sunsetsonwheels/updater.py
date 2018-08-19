# updater.py
### Update your Python apps with Git.
#### Currently supports Windows/Linux/Mac OS X

**Dependencies**

1. Git for Windows/Linux/Mac: download at https://git-scm.com/

2. GitPython: install at terminal with `pip3 install GitPython`

**How to use**

1. Download a release from: https://github.com/jkelol111/updater.py/releases into your app's root directory after installing dependencies.

2. In your app: `import updater`

3. Edit `config.py` (more details later on...)

4. When you need to update, `updateAppNow()`. This will clone to the directory you defined in `config.py`. If you want to move your configured `updater.py` from the old folder, have a look at *`config.py` guide* below.

**Additional functions**

1. `cleanupNow()`: Removes the temporary directory (.tmp_updater). Not recommended unless updating, where it will be executed by `updateNow()`.

2. `backupConfigNow()`: Backups your `config.py` to temporary directory, even when `backupOn = bool(False)` is stated in `config.py`.

3. `restoreConfigNow()`: Attempts to restore a backed up `config.py` to your application directory. Does nothing if file doesn't exist.

4. `createLauncherNow()`: Creates a launcher in a form of a `.bat` or `.sh` for easy launching of your app.

**config.py guide**

*A guide will also be inside the `config.py`.*

*You can always use `configureConfigNow(name, repo, directory, appexename, bckOn, createlauncherOn)` to configure this file.*

`appName`: Name of your application.

`appRepo`: The address of the Git repo, e.g https://github.com/jkelol111/updater.py.git (don't forget `.git` at the end!).

`appDir`: Your app's directory.

`appExecName`: Your app's Python file name (`updater.py` for example). Used to create shell scripts that an user can simply launch in order to use your app (probably redundant on Windows because `py` launcher is preinstalled).

`backupOn`: Backup on/off switch. `True` or `False` booleen. This being on will automatically copy `config.py` from the old app to the new one.

`createLaunchScriptOn`: create launcher script for supported OSes on/off switch. `True` or `False` booleen. Double-click the generated script to launch application (in most situations (!))