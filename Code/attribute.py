import random, langHanddler, readSettings

class GameAttribute:
    """
    Attribute template for things will be used in mods when I Get that far
    Right now not much is made, Just skeletons
    """
    def __init__(self, GameID: str, reader: readSettings.Reader, langHanddler: langHanddler.LangHanddler()) -> None:
        self.GameId       = GameID
        self.reader       = reader
        self.langHanddler = langHanddler
    
    def GetId(self) -> str:
        return self.GameId
    
    def GetName(self) -> str:
        """
        returns the lang name so if you need a diffrent lang you can
        """
        return langHanddler.langer



    

class Luck(GameAttribute("attribute.luck")):
    def __init__(self, NormalLuck: float, TrueLuck: float) -> None:
        self.NormalLuck   = NormalLuck
        self.TrueLuck     = TrueLuck
    
    def RandomEventWithTrueLuck(self, whatNumber: int, OutOfWhatNumber: int) -> bool:
        return random.randint(whatNumber, OutOfWhatNumber)*self.TrueLuck
    
    def RandomEventWithLuck(self, whatNumber: int, OutOfWhatNumber: int) -> bool:
        return random.randint(whatNumber, OutOfWhatNumber)*self.NormalLuck


class Health(GameAttribute("attribute.health")):
    def __init__(self) -> None:
        pass

    def Damage(self) -> None:
        pass
