from PyQt6.QtWidgets import QFrame,QPushButton,QGridLayout

class ButtonsInterface(QFrame):
    def __init__(self,parent):
        super().__init__()
        self.parent=parent
        self.live = parent.live
        self.initUI()
    
    def initUI(self):
        self.layout = QGridLayout()
        self.setLayout(self.layout)
        
        self.initButton = QPushButton("Initialiser")
        self.layout.addWidget(self.initButton,0,0)
        self.initButton.clicked.connect(self.init)
        
        self.updateButton = QPushButton("Mettre à jour")
        self.layout.addWidget(self.updateButton,0,1)
        self.updateButton.clicked.connect(self.update)
        
    def init(self):
        currentElo = self.live.getOnlineElo()
        currentGames = self.live.getOnlineGames()
        self.live.setStartElo(currentElo)
        self.live.setStartGames(currentGames)
        self.parent.settings.changeStartElo(currentElo)
        if(currentElo!=self.live.getCurrentElo()):
            self.parent.settings.changeCurrentElo(currentElo)
            self.live.setCurrentElo(currentElo)
            self.live.saveElo()
        if(currentGames!=self.live.getCurrentGames()):
            self.live.setCurrentGames(currentGames)
            self.live.saveRatio()
    def update(self,bypass=False):
        currentElo = self.live.getOnlineElo()
        currentGames = self.live.getOnlineGames()
        if(currentElo!=self.live.getCurrentElo() or bypass):
            self.parent.settings.changeCurrentElo(currentElo)
            self.live.setCurrentElo(currentElo)
            self.live.saveElo()
        if(currentGames!=self.live.getCurrentGames() or bypass):
            self.live.setCurrentGames(currentGames)
            self.live.saveRatio()