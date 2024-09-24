#recrache un fichier txt / fichier png (max 500px) avec le nombre de points elo sur chess.com gagné/perdu de la soirée
import requests,Import
from PIL import Image
class Live:
    def __init__(self):
        self.startElo = 0
        self.currentElo = 0
        self.startGames = (0,0,0)
        self.currentGames = (0,0,0)
        self.pseudo = "MyrialB"
        self.gameMode = "chess_rapid"
        self.colorPositif = (0,255,0,255)
        self.colorNegatif = (255,0,0,255)
        self.colorNeutral = (255,255,255,255)
        self.actualiser = 60
    def setStartElo(self,elo):
        self.startElo = elo
    def setCurrentElo(self,elo):
        self.currentElo = elo
    def setPseudo(self,pseudo):
        self.pseudo = pseudo
    def setGameMode(self,gameMode):
        self.gameMode = gameMode
    def setColorPositif(self,color : tuple[int,int,int,int]):
        self.colorPositif = tuple(map(int,color.split(",")))
    def setColorNegatif(self,color : tuple[int,int,int,int]):
        self.colorNegatif = tuple(map(int,color.split(",")))
    def setColorNeutral(self,color : tuple[int,int,int,int]):
        self.colorNeutral = tuple(map(int,color.split(",")))
    def setActualiser(self,actualiser):
        self.actualiser = actualiser
    def setStartGames(self,games):
        self.startGames = games
    def setCurrentGames(self,games):
        self.currentGames = games
    def getStartElo(self):
        return self.startElo
    def getCurrentElo(self):
        return self.currentElo
    def getPseudo(self):
        return self.pseudo
    def getGameMode(self):
        return self.gameMode
    def getColorPositif(self):
        return ",".join(map(str,self.colorPositif))
    def getColorNegatif(self):
        return ",".join(map(str,self.colorNegatif))
    def getColorNeutral(self):
        return ",".join(map(str,self.colorNeutral))
    def getActualiser(self):
        return self.actualiser
    def getStartGames(self):
        return self.startGames
    def getCurrentGames(self):
        return self.currentGames
    def saveElo(self):
        text = str(self.currentElo-self.startElo)
        start = text[0]
        if(start=="-"):
            color = self.colorNegatif
        elif(start=="0"):
            color = self.colorNeutral
        else:
            color = self.colorPositif
            text = "+"+text
        with open("./assets/elo.txt","w") as file:
            file.write(text)
        Image.new('RGBA',(10,10), color).save("./assets/backgroundElo.png")
    def saveRatio(self):
        wins,draws,loses = (self.currentGames[0]-self.startGames[0],self.currentGames[1]-self.startGames[1],self.currentGames[2]-self.startGames[2])
        text = str(wins)+"W / "+str(draws)+"D / "+str(loses)+"L"
        value = wins-loses
        if(value<0):
            color = self.colorNegatif
        elif(value>0):
            color = self.colorPositif
        else:
            color = self.colorNeutral
        with open("./assets/ratio.txt","w") as file:
            file.write(text)
        Image.new('RGBA',(10,10), color).save("./assets/backgroundRatio.png")
    def getOnlineElo(self):
        try:
            return requests.get("https://api.chess.com/pub/player/"+self.pseudo+"/stats", headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}).json()[self.gameMode]["last"]["rating"]
        except Exception as e:
            return None
    def getOnlineGames(self):
        try:
            return (requests.get("https://api.chess.com/pub/player/"+self.pseudo+"/stats", headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}).json()[self.gameMode]["record"]["win"],requests.get("https://api.chess.com/pub/player/"+self.pseudo+"/stats", headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}).json()[self.gameMode]["record"]["draw"],requests.get("https://api.chess.com/pub/player/"+self.pseudo+"/stats", headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}).json()[self.gameMode]["record"]["loss"])
        except Exception as e:
            return None
    def saveOptions(self):
        options={}
        options["pseudo"]=self.pseudo
        options["gameMode"]=self.gameMode
        options["colorPositif"]=",".join(map(str,self.colorPositif))
        options["colorNegatif"]=",".join(map(str,self.colorNegatif))
        options["colorNeutral"]=",".join(map(str,self.colorNeutral))
        options["actualiser"]=self.getActualiser()
        Import.setOptions(options)