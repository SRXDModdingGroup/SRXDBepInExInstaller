from modules.args import ArgsUtils
from modules.steamutils import SteamUtils
from modules.github import GitHubUtils
# from modules.gui import GuiUtils
from modules.installer import Installer
from modules.args import ArgsUtils

def main():
    # Init Arg Vars
    uninstall = False
    # Parse Args
    argsutils = ArgsUtils()
    for index, arg in enumerate(argsutils.getArgs()):
        if arg == "uninstall":
            uninstall = True

    # Init Steam Module
    print("Getting Steam Info...")
    steamutils = SteamUtils()
    if(steamutils.gameDirectory == ""):
        steamutils.inputPathIfEmpty()
    print(f"Found Game Path: {steamutils.gameDirectory}")

    # Init Installer Module
    installer = Installer(steamutils.gameDirectory)

    if (uninstall):
        if(steamutils.gameDirectory == ""):
            steamutils.inputPathIfEmpty()
        installer.uninstall()

    # Do rest of work:
    else:
        # Init BepInEx Webpage
        print("\nGetting Info from BepInEx Bleeding Edge Website...")
        bepinutils = GitHubUtils()

        # Get Download URL
        url = bepinutils.downloadURLs[0]
        print(f"Found BepInExURL: {url}")
        # Run installer
        installer.install(bepinUrl=url, installUnityLibs=False)
try:
    main()
except Exception as e:
    print(f'Exception: "{e}"')
    input("Press any Key to Close...")


    
