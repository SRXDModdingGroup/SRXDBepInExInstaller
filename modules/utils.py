import zipfile
import urllib.request

class Utils:
    def __init__(self):
        self.requestHeaders = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
        'Accept': '*/*',
        'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
        'Accept-Encoding': 'none',
        'Accept-Language': 'en-US,en;q=0.8',
        'Connection': 'keep-alive'}

    def download(self, url):
        request = urllib.request.Request(url, headers = self.requestHeaders)
        response = urllib.request.urlopen(request).read()
        return