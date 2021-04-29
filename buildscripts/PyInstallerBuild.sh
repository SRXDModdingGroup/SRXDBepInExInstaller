pyinstaller ../srxdbepinexinstaller.py --onefile
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    pyinstaller ../srxdbepinexinstallerui.pyw --add-data="../themes;./themes" --onefile
elif [[ "$OSTYPE" == "msys" ]];
    pyinstaller ../srxdbepinexinstallerui.pyw --add-data="../themes:./themes" --onefile
fi