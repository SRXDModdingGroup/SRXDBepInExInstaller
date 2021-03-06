import os
import sys

command = "python -m nuitka --onefile --plugin-enable=tk-inter  --output-dir=dist"

rootDir = ".."
fileName = "srxdbepinexinstallerui.pyw"

if sys.platform == "win32":
    rootDir = f"{rootDir}\\"
    command = f"{command} --windows-company-name=SRXDBepInExInstaller --windows-product-version=1.2.0 --windows-disable-console --windows-onefile-tempdir"
else:
    rootDir = f"{rootDir}/"

command = f"{command} {rootDir}{fileName}"

dataFiles = []

for root, dirs, files in os.walk(os.path.join(rootDir, "assets")):
    for file in files:
        filePath = os.path.join(root, file)
        dataFiles.append({"source": filePath, "output":filePath[len(rootDir):]})

for datafile in dataFiles:
    command = f'{command}  --include-data-file="{datafile["source"]}={datafile["output"]}"'

os.system(command)