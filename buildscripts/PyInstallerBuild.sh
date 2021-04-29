pyinstaller ../srxdbepinexinstaller.py --onefile
if [[ "$OSTYPE" == "msys" ]]; then
    pyinstaller ../srxdbepinexinstallerui.pyw --add-data="../themes;./themes" --onefile
elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
    pyinstaller ../srxdbepinexinstallerui.pyw --add-data="../themes:./themes" --onefile
fi