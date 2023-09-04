from . import *
import configparser
import os


class configManager:
    def __init__(self, configFile):
        self.configFile = configFile

    @staticmethod
    def configPath():
        path = os.path.join("config.ini")

        if not os.path.isfile(path):
            print("WHERE'S THE CONFIG? IDIOT (add some default config generator here)")

        return path

    @staticmethod
    def readConfig():
        config = configparser.ConfigParser()
        config.read(configManager.configPath())
        return config

    @staticmethod
    def loadConfig():
        config = configManager.readConfig()

        try:
            for section in config.sections():
                for name, value in config[section].items():
                    varManager.setVar(name, value, section)
        except configparser.Error:
            print("WHERE'S THE CONFIG? IDIOT (add some default config generator here)")
