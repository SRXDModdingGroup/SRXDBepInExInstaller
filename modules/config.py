import configparser
import os

class ConfigUtils:
    def __init__(self, configLocation):
        self.configLocation = configLocation
        try:
            if (not os.path.exists(configLocation)):
                print("Creating Config File")
                with open(configLocation, mode='w', encoding="utf-8-sig"):
                    os.utime(configLocation, None)
            self.cfgparse = configparser.SafeConfigParser()
            self.cfgparse.optionxform = str
            self.cfgparse.read(configLocation, encoding="utf-8-sig")
        except:
            self.errormessage()
        return
    def errormessage(self):
        print("Config File Could no be Edited.")
    def setAttr(self, section, key, value):
        try:
            with open(self.configLocation, 'w', encoding="utf-8-sig") as configfile:
                if (not section in self.cfgparse.sections() and not self.cfgparse.has_option(section, key)):
                    self.cfgparse.add_section(section)
                    self.cfgparse.set(section, key, value)
                    self.cfgparse.write(configfile)
                elif (self.cfgparse.get(section, key) != value):
                    self.cfgparse.set(section, key, value)
                    self.cfgparse.write(configfile)
        except:
            self
        return

    def getAttr(self, section, key):
        keyvalue = None
        try:
            keyvalue = self.cfgparse.get(section, key)
        except:
            self.errormessage()
        return keyvalue
          
    