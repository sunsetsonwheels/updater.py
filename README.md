# updater.py
### Update your Python apps with Git.

**Dependencies**

1. Git for Windows/Mac/Linux/BSD: download at https://git-scm.com/

2. GitPython: install at terminal `pip3 install GitPython`

**How to use**

1. Clone this repo into your app's root directory after installing dependencies.

2. In your app: `from updater import *`

3. Edit `config.py` (more details later on...)

4. When you need to update, `updateAppNow()`. This will clone to the directory you defined in `config.py`. If you want to move your app data and configured `updater.py` from the old folder, have a look at *`config.py` guide* below.

**config.py guide**

*A guide will also be inside the `config.py`.*

`appName`: Name of your application.

`appRepo`: The address of the Git repo, e.g https://github.com/jkelol111/updater.py.git (don't forget `.git` at the end!)

`appDir`: Your app's directory (will not change after update, update it with the new one later with `configureUpdater()`)

`backupOn`: Backup on/off switch. Integers other than 0 (off) or 1 (on) will be regarded as non-valid options and will not be considered. This being on will automatically copy `config.py` from the old app to the new one.

`backupDir`: The directory to backup from the application's root folder.

**Future plans**

1. Getting this to actually work.
