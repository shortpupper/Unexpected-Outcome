import random, setup

class GameAttribute:
    """
    Attribute template for things will be used in mods when I Get that far
    Right now not much is made, Just skeletons
    """
    def __init__(self, GameID: str, *args) -> None:
        self.GameId       = GameID

        self.Args         = args
        # this should be improved
        # ^^^^^^^^^^^^^^^^^^^^^^^ - I did kind of i think
        self.reader       = setup.reader
        self.langHanddler = setup.langer
    
    def GetId(self) -> str:
        return self.GameId
    
    def GetName(self, CanHaveSpace: bool = True) -> str:
        """
        returns the lang name so if you need a diffrent lang you can
        """
        name = self.langHanddler.getNameUsingId(self.GameId)
        return name if CanHaveSpace else name.replace(" ", "_")



    

class Luck(GameAttribute):
    def __init__(self, NormalLuck: float, TrueLuck: float) -> None:
        super().__init__(GameID="attribute.luck")
        self.NormalLuck   = NormalLuck
        self.TrueLuck     = TrueLuck
    
    def __str__(self) -> str:
        return self.GameId
    
    def RandomEventWithLuck(self, whatNumber: int, OutOfWhatNumber: int, IsTrueLuck=False) -> bool:
        """
        makes the 1/800 change with a normal luck of 1.5 very Low and 0.5.\n
        To something like a 1/1200, 1/400
        """
        outa = (OutOfWhatNumber*(self.NormalLuck if not IsTrueLuck else self.TrueLuck))
        return True if (outa <= 1) or random.randint(whatNumber, outa) == outa else False

    def TestHealth(self):
        """
        This is test code so ignore it. \n
        If you want to know i'm trying to figer out,\n
        how Luck may influcnce health weird to explane it like this.
        """
        return Health().Damage(1)


class Health(GameAttribute):
    def __init__(self, MaxHealthPoints: float, CurrentHealthPoints: float = None) -> None:
        super().__init__("attribute.health")


        self.MaxHealthPoints = 100
        self.HealthPoints    = CurrentHealthPoints if CurrentHealthPoints != None else MaxHealthPoints
        self.IsDead          = False
        self.IsFullDead      = False
    
    def __str__(self) -> str:
        return self.GameId

    def Damage(self, amount: float) -> None:
        self.HealthPoints -= amount
        if self.HealthPoints <= 0:
            self.IsDead = True
        elif not self.IsFullDead and self.HealthPoints > 0:
            self.IsDead = True
    
    def GetHealth(self) -> float:
        return self.HealthPoints




if __name__ == '__main__':
    print('<<<----... Running attribute Test ...---->>>')
    # lower is better odds
    luck = Luck(NormalLuck=1, TrueLuck=1)
    print(luck.RandomEventWithLuck(1, 20))
    print(luck.RandomEventWithLuck(1, 20, IsTrueLuck=True))
    print(str(luck))

    print("Health Stuff")
    health = Health(MaxHealthPoints=100, CurrentHealthPoints=50)
    print(f"You have '{health.GetHealth()}' HealthPoints")
    #take some damage
    health.Damage(9)
    print(f"You have '{health.GetHealth()}' HealthPoints")

    print('<<<----...   End attribute Test   ...---->>>')
# else:
#     print("name:" + str(__name__))