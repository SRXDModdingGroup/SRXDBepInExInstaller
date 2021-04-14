from html.parser import HTMLParser
import urllib.request

class BepInExUtils:
    def __init__(self):
        self.baseBepinexUrl = "https://builds.bepis.io"
        self.requestHeaders = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
        'Accept-Encoding': 'none',
        'Accept-Language': 'en-US,en;q=0.8',
        'Connection': 'keep-alive'}
        self.downloadURLs = []
        self.initDownloadURLs()

    def initDownloadURLs(self):
        request = urllib.request.Request(f"{self.baseBepinexUrl}/projects/bepinex_be", headers = self.requestHeaders)
        response = str(urllib.request.urlopen(request).read())

        parser = HTMLParser()
        parser.handle_starttag = self.handle_starttag
        parser.feed(response)

    def handle_starttag(self, tag, attrs):
        bepinexSite = self.baseBepinexUrl
        if (attrs.__len__() > 0):
            if (attrs[0][0] == "class"):
                if (attrs[0][1] == "artifact-link" and "BepInEx_UnityIL2CPP_x64" in attrs[2][1]):
                    self.downloadURLs.append(f"{bepinexSite}{attrs[2][1]}")


