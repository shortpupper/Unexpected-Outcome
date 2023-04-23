"""
file for the class LangHanddler.\n
handdels the lang.
"""
import json, readSettings

class LangHanddler:
    """
    like the name says it haddles the lang file.\n
    so you or me can make things cool.\n
    and it uses json files.
    """ 
    def __init__(self, reader: readSettings.Reader) -> None:
        self.reader = reader
        with open(self.reader.getSetting('langLocation') + self.reader.getSetting("lang") + ".json", "r") as f:
            self.langFile = json.loads(f.read())

    def getNameUsingId(self, nameId) -> str:
        """
        Used to get names in lang file.
        """
        return self.langFile.get(nameId)


if __name__ == "__main__":
    import readSettings
    print("<<<----... Running langHandler Test ...---->>>")

    reader = readSettings.Reader()
    langer = LangHanddler(reader=reader)
    
    print(langer.getNameUsingId("attribute.luck"))

    print("<<<----...   End langHandler Test   ...---->>>")
        
