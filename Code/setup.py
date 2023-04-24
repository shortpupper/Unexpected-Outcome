import time, os
import readSettings, langHanddler, attribute, Entity

produntionBuild = True if __name__ != "__main__" or True else False
try:
    reader = readSettings.Reader()
except:
    print("Can't find file install mode.\n\n")
    # setup the files
    print("Will break/won't load if you don't make the game data")
    imp1 = input("Make Game (Y/no)> ")
    if imp1.lower() != "no":
        try:
            os.mkdir("C:/UO")
        except:
            print("Failed to make the UO dir")
        
        try:
            os.mkdir("C:/UO/lang")
        except:
            print("failed to make the lang dir")
        try:
            input(">>> contiune <<<")
            Dir = "C:/UO"
            with open(Dir + "/settings.toml", "w") as f:
                tomlFile = f"""# this is more for testting you dont need to change this\ntestString = "yes it is test"\n# save = ""\n\n# lang so you could make you're own if you wanted\nlang = "en_us"\nlangLocation = '{Dir}/lang/'"""
                f.write(tomlFile)
            with open(Dir + "/lang/en_us.json", "w") as f:
                jsonFile = """{\n\t"attribute.luck": "Luck",\n\t"attribute.health": "Health",\n\t"entity.player.name.default": "Matthew"\n}"""
                f.write(jsonFile)
        except:
            print("FAILED")
            print("Exiting")
            input(">>> Contiune <<<")
            
            time.sleep(3)
            input("END PROGRAM")
            exit()



reader = readSettings.Reader()

try:
    langer = langHanddler.LangHanddler(reader=reader)
except:
    print("langer [FAILED]")

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
