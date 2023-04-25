

# this might be f-ed cus what
produntionBuild     = True if __name__ != "__main__" or True else False


gameDataZipURL      = "https://github.com/shortpupper/Unexpected-Outcome/raw/main-patch-home-1/gameData.zip"



gameTest = False



# reader,langer = None
def notNewUser():
        import readSettings, langHanddler
    # try:
        global reader, langer, defaultPath, defaultGameDataPath
        # READER
        reader              = readSettings.Reader()
        # READER

        # LANGER
        langer = langHanddler.LangHanddler(reader=reader)
        # LANGER

        # for idk make setup files
        defaultPath         = reader.getSetting("defaultPath")
        defaultGameDataPath = reader.getSetting("gameDataPath")
    # except:
    #     print("[dataIsMe.notNewUser] [FAILED] Well that sucks...")
