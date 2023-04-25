import time, os




### file setup
produntionBuild = True if __name__ != "__main__" or True else False


defaultPath = "C:/UO/gameData" 



# this is now fed cus i need it to install as a package type thing
try:
    import readSettings, langHanddler, attribute, Entity
    reader      = readSettings.Reader()
    defaultPath = reader.getSetting("gameDataPath")
    # if NewFile: raise Exception("makeing new")
except:
    print("Couldn't find file, install mode.\n\n")
    # setup the files
    print("Will break/won't load if you don't make the game data")
    imp1 = input("Make Game (Y/no)> ")
    if imp1.lower() != "no":
        try:
            os.mkdir(defaultPath)
        except:
            print("Failed to make the UO dir")

        try:
            os.mkdir(f"{defaultPath}/lang")
        except:
            print("failed to make the lang dir")
        
        # need to change this so that I download it off of github some how?
        try:
            # make somthing here plz
            import ziperGetter
            
            ziperGetter.download_and_unzip()



            import readSettings, langHanddler, attribute, Entity
            reader = readSettings.Reader()
        except:
            print("FAILED")
            print("Exiting")
            time.sleep(3)
            exit()
    






try:
    langer = langHanddler.LangHanddler(reader=reader)
except:
    print("langer [FAILED]")

player = Entity.Entity("id_A")

player.add_attribute(attribute.Luck(1, 1))

# print(str(player.__dict__))
# print(player.Luck)







# gmae loop

gameTest = False

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
    elif imp == "5":
        print("\n0) exit/quit,  1) Show Saves,  2) Save Game,  3) load a saved game.")
        imp = input("Save/Load Game>")
        if imp == "0":
            pass
        elif imp == "1":
            os.listdir(f"{defaultPath}/saves")
        elif imp == "2":
            print("Can't name file's exit or quit else ya'll leave, and you don't type the extension.")
            imp = input("name> ")
            if imp.lower() in ["exit", "quit"]:
                pass
            else:
                # saving a game
                pass
        else:
            print("Are ya sure ya not speakin latin, eh?")
    else:
        print("Are you speaking frence??")



if __name__ == '__main__':
    print('<<<----... Running setup.py Test ...---->>>')
    
    print(str(__dict__))

    print('<<<----...   End setup.py Test   ...---->>>')