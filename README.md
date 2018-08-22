# updater.py
### Update your Python apps with Git.
### Currently supports Windows/Linux/Mac (BSD testers wanted!)

**Some limitations as of now**

- On Windows: the path separator `\`, if present in `config.py`, will invoke errors during the initilization of `updater.py` (unicode error). **Fix slated for v 2.0, where config files will move on to YAML.**

- Unorgranized and hard to read code (sorry peeps!).

**Dependencies**

- Git for Windows/Linux/Mac: download at https://git-scm.com/

- GitPython: install at terminal with `pip3 install -U GitPython`

- PyYAML: install at terminal with `pip3 install -U PyYaml`

**How to use**

1. Download the latest release from: https://github.com/jkelol111/updater.py/releases into your app's root directory after installing dependencies (see above).

2. In your app: `import updater`

3. Edit `config.yml` (more details later on...)

4. When you need to update, `updateAppNow()`. This will clone to the directory you defined in `config.yml`. If you want to move your configured `updater.py` from the old folder, have a look at *`config.py` guide* below.

**Additional functions**

- `cleanupNow()`: Removes the temporary directory (.tmp_updater). Not recommended unless updating, where it will be executed by `updateNow()`.

- `backupConfigNow()`: Backups your `config.yml` to temporary directory, even when `backupOn = bool(False)` is stated in `config.py`.

- `restoreConfigNow()`: Attempts to restore a backed up `config.yml` to your application directory. Does nothing if file doesn't exist.

- `createLauncherNow()`: Creates a launcher in a form of a `.bat` or `.sh` for easy launching of your app.

- `configureConfigNow(appid, repo, directory, appexename, bckOn, createlauncherOn)`: Creates or modifies an existing `config.yml` file.

**config.yml guide**

*You can always use `configureConfigNow(appid, repo, directory, appexename, bckOn, createlauncherOn)` to configure this file.*

Sample `config.yml` file:

`{appDir: Nothing, appExecName: nothing.py, appIdentifier: com.sample.nothing, appRepo: 'http://www.example.com/project.git', backupOn: false, createLaunchScriptOn: false}`

Meanings of variables:

`appIdentifier`: Identifier of your application, e.g `com.sample.nothing`.

`appRepo`: The address of the Git repo, e.g https://github.com/jkelol111/updater.py.git (don't forget `.git` at the end!).

`appDir`: Your app's directory.

`appExecName`: Your app's Python file name (`updater.py` for example). Used to create shell scripts that an user can simply launch in order to use your app (probably redundant on Windows because `py` launcher is preinstalled).

`backupOn`: Backup on/off switch. `True` or `False` booleen. This being on will automatically copy `config.py` from the old app to the new one.

`createLaunchScriptOn`: create launcher script for supported OSes on/off switch. `True` or `False` booleen. Double-click the generated script to launch application (in most situations (!))