import os
import sys

command = "python -m nuitka --standalone --onefile --plugin-enable=tk-inter"

rootDir = ".."

if sys.platform == "win32":
    rootDir = f"{rootDir}\\"
    command = f"{command} --mingw64"
    command = f"{command} --windows-company-name=SRXDBepInExInstaller --windows-product-version=1.2.5 --windows-disable-console"
else:
    rootDir = f"{rootDir}/"

command = f"{command} {rootDir}srxdbepinexinstallerui.pyw"

dataFiles = []

for root, dirs, files in os.walk(os.path.join(rootDir, "themes")):
    for file in files:
        filePath = os.path.join(root, file)
        dataFiles.append({"source": filePath, "output":filePath[len(rootDir):]})

for datafile in dataFiles:
    command = f'{command}  --include-data-file="{datafile["source"]}={datafile["output"]}"'

os.system(command)