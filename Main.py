import Import,Live,os,MainInterface

if __name__ == "__main__":
    if not os.path.exists("assets"):
        os.mkdir("assets")
    live = Live.Live()
    values = Import.getOptions()
    live.setPseudo(values["pseudo"])
    live.setColorPositif(values["colorPositif"])
    live.setColorNegatif(values["colorNegatif"])
    live.setColorNeutral(values["colorNeutral"])
    live.setGameMode(values["gameMode"])
    live.setStartElo(live.getOnlineElo())
    live.setCurrentElo(live.getOnlineElo())
    live.setActualiser(values["actualiser"])
    live.setCurrentGames(live.getOnlineGames())
    live.setStartGames(live.getOnlineGames())
    MainInterface.execute(live)