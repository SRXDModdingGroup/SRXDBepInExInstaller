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
        request = urllib.request.Request(f"https://api.github.com/repos/bepinex/bepinex/releases")
        response = json.loads(urllib.request.urlopen(request).read())
        for release in response:
            self.downloadURLs.append(next((item["browser_download_url"] for item in release["assets"] if "x64" in item["name"]), release["assets"][0]["browser_download_url"]))
            self.downloadVersions.append(release["tag_name"])



