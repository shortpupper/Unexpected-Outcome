import time, os



if __name__ == '__main__':
    print('<<<----... Running test setup.py Test ...---->>>')
    
    
    print("Yellow?")

    # import dataIsMe
    # dataIsMe.notNewUser()

    print('<<<----...   End test setup.py Test   ...---->>>')




### file setup


if __name__ == '__main__':
    print('<<<----... Running set Test ...---->>>')
        
    defaultPath         = "C:/UO"
    defaultGameDataPath = defaultPath + "/gameData" 
    # this is now fed cus i need it to install as a package type thing
    import newUser

    try:
        print("[START] try")
        import dataIsMe
        dataIsMe.notNewUser()
        newUser.NEW_NOW(defaultGameDataPath=defaultGameDataPath,
                         defaultPath=defaultPath,
                           gameDataZipURL=dataIsMe.gameDataZipURL,
                            withFILES=False)
        
        print("[FINAL SETUP] Your good to go")
    except:
        print("[START] except")
        import dataIsMe
        newUser.NEW_NOW(defaultGameDataPath=defaultGameDataPath,
                         defaultPath=defaultPath,
                           gameDataZipURL=dataIsMe.gameDataZipURL,
                           withFILES=True)
        
        print("[FINAL SETUP] Should be setup")
    
    print('<<<----...   End set Test   ...---->>>')







# player = Entity.Entity("id_A")

# player.add_attribute(attribute.Luck(1, 1))

# print(str(player.__dict__))
# print(player.Luck)





# gmae loop



while dataIsMe.gameTest:
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
            os.listdir(f"{defaultGameDataPath}/saves")
        elif imp == "2":
            print("Can't name file's 'exit' or 'quit' else ya'll leave, and you don't type the extension.")
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

    print('<<<----...   End setup.py Test   ...---->>>')