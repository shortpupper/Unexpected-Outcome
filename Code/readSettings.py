import toml, os

class Reader:
    def __init__(self) -> None:
        with open(r"F:\.dev\python\projects\Unexpected-Outcome\Unexpected-Outcome\Code\settings.toml", "r") as f: 
            self.settings = toml.load(f.read())
    
    def getSetting(self, settingName: str):
        return self.settings.get(settingName)

if __name__ == "__main__":
    reader = Reader()
    print(reader.getSetting("testString"))