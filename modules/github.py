import urllib.request
import re
import json

class GitHubUtils:
    def __init__(self):
        self.baseUrl = "https://api.github.com"
        self.downloadURLs = []
        self.downloadVersions = []
        try:
            self.initDownloadURLs()
        except:
            print(f"{self.baseUrl} could not be accessed.")

    def initDownloadURLs(self):
        def validate_name(name: str) -> bool:
            return "x64" in name and "linux" not in name and "macos" not in name

        request = urllib.request.Request(f"https://api.github.com/repos/bepinex/bepinex/releases")
        response = json.loads(urllib.request.urlopen(request).read())
        for release in response:
            self.downloadURLs.append(next((item["browser_download_url"] for item in release["assets"] if validate_name(item["name"])), release["assets"][0]["browser_download_url"]))
            self.downloadVersions.append(release["tag_name"])



