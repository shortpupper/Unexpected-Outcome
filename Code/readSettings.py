"""
file for the reader class
"""

import toml, os

class Reader:
    """
    a reader class to read toml files makes it make sentce to me
    """
    def __init__(self) -> None:
        with open("F:/.dev/python/projects/Unexpected-Outcome/Unexpected-Outcome/Code/settings.toml", "r") as f: 
            self.settings = toml.load(f)
    
    def getSetting(self, settingName: str):
        """
        Like the name implies you ask for a setting useing the name
        """
        return self.settings.get(settingName)

if __name__ == "__main__":
    print("<<<----... Running readSettings Test ...---->>>")

    reader = Reader()
    print(reader.getSetting("testString"))

    print("<<<----...   End readSettings Test   ...---->>>")