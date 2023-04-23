import readSettings, langHanddler, attribute, Entity

reader = readSettings.Reader()
langer = langHanddler.LangHanddler(reader=reader)

player = Entity.Entity("id_A")

player.add_attribute(attribute.Luck(1, 1))

# print(str(player.__dict__))
# print(player.Luck)

gameTest = True

while gameTest:
    print("\n\n0) Exit/Quit, 1) self Harm, 2) check Health, 3) roll die, 4) set luck")
    imp = input("what to Do?> ")
    if imp == "exit" or imp == "0":
        break
    elif imp == "1":
        imp = input("How much?\n>")
        try:
            print(player.Name + " damaged them self by: " + str(float(imp)))
            player.attribute_Health.Damage(float(imp))
        except:
            print("That value is wroung try again.")
    elif imp == "2":
        print("Your hp is: " + str(player.attribute_Health.GetHealth()))
    elif imp == "3":
        print("You got " + ("Lucky" if player.Luck.RandomEventWithLuck(1, 2) else "UnLucky"))
    elif imp == "4":
        print("lower the better")
        imp = input("How much?\n>")
        try:
            player.Luck.NormalLuck = float(imp)
        except:
            print("That value is wroung try again.")
