# updater.py
### Update your Python apps with Git.

**Dependencies**

1. GitPython: `pip3 install GitPython`

**How to use**

1. Clone this repo into your app's root directory after installing dependencies.

2. In your app: `from updater import *`

3. `configureUpdater("*appname*", "*linkonGitHub*")` in your app, or edit `config.py` (more details later on...)

4. When you need to update: `exit()` and `updateAppNow()` in your app (make sure Step 3 is done, or this will just spew an error and quit out. And remember that `exit()` or else this will just spew an error and quit out.)

**config.py savagery**

`appName`: Name of your application (does nothing but indentification)

`appRepo`: The address of the Git repo, e.g https://github.com/jkelol111/updater.py.git (don't forget `.git` at the end!)

`logLevel`: How detailed is the updater's log. (this might be useful for nothing, because `try:` and `except Exception as e` is already sitting there to spew errors.)

**Future plans**

1. Actually putting this on GitHub.
