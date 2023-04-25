import os, time

def NEW_NOW(defaultGameDataPath, gameDataZipURL, defaultPath, withFILES: bool):
    try:
        os.mkdir(defaultPath)
    except FileExistsError:
        print("[17] There is all ready a file there in UO")
    except FileNotFoundError:
        print("[18] f")
    
    try:
        import ziperGetter
    except:
        print("[6] Can't import ziperGetter")


    try:
        ziperGetter.download_and_unzip(gameDataZipURL, defaultPath)
    except:
        print("[19] Can't seem to download and unpack gameData")
        print("[20] Which means your f-ed")
    # try:
    #     os.mkdir(defaultGameDataPath)
    # except FileExistsError:
    #     print("[4] There is all ready a file there in UO")
    # except FileNotFoundError:
    #     print("[16] f")
    # finally:
    #     print("[15] f")
    #     # print("Failed to make the UO dir")

    # try:
    #     os.mkdir(f"{defaultGameDataPath}/lang")
    # except FileExistsError:
    #     print("[5] There is all ready a file there in lang")
    
    if  withFILES:
        print("[1] Couldn't find file, install mode.")
        # setup the files
        print("[2] Will break/won't load if you don't make the game data")
        imp1 = input("[3] Make Game (Y/no)> ")
    else:
        imp1 = "yes" 
    if imp1.lower() != "no":
        # if withFILES:
        #     try:
        #         os.mkdir(defaultGameDataPath)
        #     except FileExistsError:
        #         print("[4] There is all ready a file there in UO")
        #         # print("Failed to make the UO dir")

        #     try:
        #         os.mkdir(f"{defaultGameDataPath}/lang")
        #     except FileExistsError:
        #         print("[5] There is all ready a file there in lang")
        #         # print("failed to make the lang dir")
        
        # need to change this so that I download it off of github some how?
        try:
            # make somthing here plz
            # try:
            #     import ziperGetter
            # except:
            #     print("[6] Can't import ziperGetter")

            # if withFILES:
            #     try:
            #         ziperGetter.download_and_unzip(gameDataZipURL, defaultPath)
            #     except:
            #         print("[7] Can't seem to download and unpack gameData")
            

            try:
                import readSettings
            except:
                print("[8] Fail to import readSettings")

            try:
                import langHanddler
            except:
                print("[9] Fail to import langHanddler")

            try:
                import attribute
            except:
                print("[10] Fail to import attribute")

            try:
                import Entity
            except:
                print("[11] Fail to import Entity")


            try:
                reader = readSettings.Reader()
            except:
                print("[12] Can't import readSettings.Reader()")
        except:
            print("[13] FAILED")
            print("[14] Exiting")
            time.sleep(3)
            exit()





if __name__ == '__main__':
    print('<<<----... Running newUser Test ...---->>>')
    
    import ziperGetter
    ziperGetter.download_and_unzip("https://github.com/shortpupper/Unexpected-Outcome/raw/main-patch-home-1/gameData.zip", "C:/UO")

    print('<<<----...   End newUser Test   ...---->>>')




