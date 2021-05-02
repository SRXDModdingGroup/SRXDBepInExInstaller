import zipfile
import urllib.request
import tempfile
import os
import shutil
import pathlib

class DownloadUtils:
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
        return response

    def saveResponseAsTempFile(self, response):
        new_file, filePath = tempfile.mkstemp()
        os.write(new_file, response)
        os.close(new_file)
        return new_file, filePath

    def unzipTo(self, inputFilePath, outputPath):
        
        with zipfile.ZipFile(inputFilePath, 'r') as zip_ref:
            zip_ref.extractall(outputPath)
        return
    
    def deleteFile(self, filePath):
        os.remove(filePath)
        return
    def recursiveDeleteFolder(self, filePath):
        shutil.rmtree(filePath)
        return

    # Makes everything easier to download and unzip
    def downloadFileAndUnzip(self, url, outputDirPath):
        try:
            # Get and Save File
            downloadedFile = self.download(url)
            fileObject, tempZipPath = self.saveResponseAsTempFile(downloadedFile)
            print(f"Saved Temp Zip: {tempZipPath}")

            # Unzip File to 
            self.unzipTo(tempZipPath, f"{outputDirPath}")
            print(f"Unzipped: {tempZipPath} => {outputDirPath}")

            # Deletes temp zip
            self.deleteFile(tempZipPath)
            print(f"Deleted: {tempZipPath}")
        except Exception as e:
            raise Exception("Could not Download:\n"+e)
        return

