import random

class GameAttribute:
    def __init__(Self, Health: int, NormalLuck: float, TrueLuck: float) -> None:
        Self.HealthPoints = Health
        Self.NormalLuck   = NormalLuck
        Self.TrueLuck     = TrueLuck

    class Luck:
        def __init__(self, GameAttributeData) -> None:
            self.game_attribute = GameAttributeData
        
        def RandomEventWithTrueLuck(self, whatNumber: int, OutOfWhatNumber: int) -> bool:
            return random.randint(whatNumber, OutOfWhatNumber)*self.game_attribute.TrueLuck
        
        def RandomEventWithLuck(self, whatNumber: int, OutOfWhatNumber: int) -> bool:
            return random.randint(whatNumber, OutOfWhatNumber)*self.game_attribute.NormalLuck

    class Health:
        def __init__(self) -> None:
            pass

        def Damage(self) -> None:
            pass

    
