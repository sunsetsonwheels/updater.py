# updater.py
### Update your Python apps with Git.

**Dependencies**

1. Git for Windows/Mac/Linux/BSD: download at https://git-scm.com/

2. GitPython: install at terminal `pip3 install GitPython`

**How to use**

1. Clone this repo into your app's root directory after installing dependencies.

2. In your app: `from updater import *`

3. `configureUpdater("*appname*", "*linkonGitHub*", "*appdirectory*")` in your app, or edit `config.py` (more details later on...)

4. When you need to update, `updateAppNow()`. This will create a new folder freshly cloned from you Git repo and leave the old one with `updater.py` and `config.py`intact. If you want to move your app data and configured `updater.py` from the old folder, have a look at *config.py savagery* below.

**config.py guide**

*Some options are not available in configureUpdater, so edit them manually here. A guide will also be inside the `config.py`.*

`appName`: Name of your application.

`appRepo`: The address of the Git repo, e.g https://github.com/jkelol111/updater.py.git (don't forget `.git` at the end!)

`appDir`: Your app's directory (will not change after update, update it with the new one later with `configureUpdater()`)

`backupOn`: Backup on/off switch. Integers other than 0 (off) or 1 (on) will be regarded as non-valid options and will not be considered. This being on will automatically copy `config.py` from the old app to the new one.

`backupDir`: Choose a folder to automatically copy to the new app, e.g `.../app/data` (not `.../app/` because then it means you are copying the whole old app anyways, and `updater.py` is still running inside that folder.)

`logLevel`: How detailed is the updater's log. (this might be useful for nothing, because `try:` and `except Exception as e` is already sitting there to spew errors.)

**Future plans**

1. Actually putting this on GitHub.
