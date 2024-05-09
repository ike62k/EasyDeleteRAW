import configparser
class Setting:
    def __init__(self) -> None:
        self.referense: list[str] = []
        self.target: list[str] = []
        self.__reffile: str = "config\\reference.txt"
        self.__tarfile: str = "config\\target.txt"

    def loadref(self):
        with open(self.__reffile, "r") as f:
            self.referense = f.read().splitlines()

    def loadtar(self):
        with open(self.__tarfile, "r") as f:
            self.target = f.read().splitlines()

    def loadconfig(self):
        self.config =configparser.ConfigParser()
        self.config.read("config\\config.ini", encoding="utf-8")
        self.nogui = self.config.getboolean("setting", "nogui")
        self.noconsole = self.config.getboolean("setting", "noconsole")
        self.nocheck = self.config.getboolean("setting", "nocheck")
        self.debug = self.config.getboolean("setting", "debug")