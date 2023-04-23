import attribute

class Entity:
    def __init__(self, NameID: str, Name: str = "Mattew") -> None:
        self.NameID    = NameID
        self.Name      = Name
        self.MaxHealth = 89.4

        # attributes
        self.game_attribute_Health = attribute.Health(MaxHealthPoints=self.MaxHealth)



if __name__ == '__main__':
    print('<<<----... Running Entity Test ...---->>>')
    smarty = Entity(NameID="smarty.dummy")

    print("Heaklt: " + str(smarty.game_attribute_Health.GetHealth()))
    # comit toe damage
    smarty.game_attribute_Health.Damage(5.25)

    print("Healst: " + str(smarty.game_attribute_Health.GetHealth()))
    print('<<<----...   End Entity Test   ...---->>>')