pyinstaller ../srxdbepinexinstaller.py --onefile
if [[ "$OSTYPE" == "msys" ]]; then
    pyinstaller ../srxdbepinexinstallerui.pyw --add-data="../assets;./assets" --onefile
elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
    pyinstaller ../srxdbepinexinstallerui.pyw --add-data="../assets:./assets" --onefile
fi