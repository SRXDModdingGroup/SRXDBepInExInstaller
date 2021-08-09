# SRXDBepInXInstaller
A small installer written in Python that installs/uninstalls BepInEx for Spin Rhythm XD

## How to Compile
For an optimal experience, please install the Python version inside `.python-version`.

Firstly, install `pyinstaller`.
```shell
pip install pyinstaller
cd buildscripts
```

Then do if you are using a shell (Bash, Fish, etc.):
```shell
./PyInstallerBuild.sh
```

Otherwise:
For Windows:
```shell
pyinstaller ../srxdbepinexinstallerui.pyw --add-data="../assets;./assets" --onefile
```
For Linux:
```shell
pyinstaller ../srxdbepinexinstallerui.pyw --add-data="../assets:./assets" --onefile
```
