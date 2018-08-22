# updater.py
### Update your Python apps with Git.
### Currently supports Windows/Linux/Mac (BSD testers wanted!)

**Important notice**

- Releases moving forward from 2.x.x will deprecate config.py in favour of `config.ym`l (YAML). Current `config.py` files will be converted to `config.yml` upon first update operation initiated from another app, but... if you are on Windows, see the **Some limitations as of now** section at the bottom.

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

**Some limitations as of now**

- On Windows: the path separator `\`, if present in `config.py`, will invoke errors during the initilization of `updater.py` (unicode error). **v 2.0.0 is out, but your app has to use the new `config.yml` in the first place, or else the conversion from `config.py` to `config.yml` will still invoke errors (because it still needs to import `config.py`, hence throwing that unicode error). This only happens on Windows, and it is something I cannot fix automatically within `updater.py`. By hand fix will be detailed below.**

**By hand fixes**

- The Windows path separator bug: open `config.py` and replace every backslash in `appDir` with a slash. Simple as that. Oh and switch to the new `config.yml` format while you're at it.