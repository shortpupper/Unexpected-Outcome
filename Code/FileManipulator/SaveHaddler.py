import json
import setup

class SaveAndLoadHaddler():
    def __init__(self, fileName: str, Directory: str = setup.gameDataPath) -> None:
        self.fileName  = fileName
        self.DaveData  = None
        self.Directory = Directory
    
    def Save(self) -> None:
        with open(f"{self.Directory}/{self.fileName}.gameSave", "w") as f:
            f.write()
    
    def Load(self) -> None:
        with open(f"{self.Directory}/{self.fileName}.gameSave", "r") as f:
            pass

class TesterSave():
    def __init__(self) -> None:
        pass
    
    def testFunction(self):
        return "Test ran."



