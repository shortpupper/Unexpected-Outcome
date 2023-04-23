import attribute

class Entity:
    """
    yeas
    """
    def __init__(self, NameID: str, Name: str = "Mattew") -> None:
        self.NameID    = NameID
        self.Name      = Name
        self.MaxHealth = 89.4

        # attributes
        self.attribute_Health = attribute.Health(MaxHealthPoints=self.MaxHealth)
    
    def add_attribute(self, NewAttribute: attribute.GameAttribute) -> None:
        """
        Like most things say it the Entity gains a new attribute
        """
        self.__setattr__(NewAttribute.GetName(CanHaveSpace=False), NewAttribute)
    
    def tester(self) -> True:
        """
        returns true
        """
        return True



if __name__ == '__main__':
    print('<<<----... Running Entity Test ...---->>>')
    smarty = Entity(NameID="smarty.dummy")

    print("Heaklt: " + str(smarty.attribute_Health.GetHealth()))
    # comit toe damage
    smarty.attribute_Health.Damage(5.25)

    print("Healst: " + str(smarty.attribute_Health.GetHealth()))
    print('<<<----...   End Entity Test   ...---->>>')