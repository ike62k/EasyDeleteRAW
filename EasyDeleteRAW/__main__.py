import os
import glob
from .setting import Setting

class selecter:
    def __init__(self):
        self.setting = Setting()
        self.setting.loadref()
        self.setting.loadtar()
        self.setting.loadconfig()
        #print(self.setting.referense)
        #print(self.setting.target)
        
    def delete(self,directory:str):
        with glob.glob(directory + "\\*") as files:
            for i in files:
                if os.path.splitext(i)[1] in self.setting.target:
                    for j in self.setting.referense:
                        if not os.path.isfile(os.path.splitext(i)[0] + j):
                            os.remove(i)

App = selecter()
App.delete(input("Directory: "))