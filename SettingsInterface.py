from PyQt6.QtWidgets import QFrame,QPushButton,QGridLayout,QLabel,QLineEdit,QComboBox
from PyQt6.QtGui import QShortcut, QKeySequence

class SettingsInterface(QFrame):
    def __init__(self,parent):
        super().__init__()
        self.parent=parent
        self.live = parent.live
        self.gameModes = {"chess_bullet":"Bullet","chess_blitz":"Blitz","chess_rapid":"Rapide"}
        self.initUI()
        
    def initUI(self):
        self.layout = QGridLayout()
        self.setLayout(self.layout)
        
        self.shortcut = QShortcut(QKeySequence("Ctrl+S"),self)
        self.shortcut.activated.connect(self.apply)
        
        self.couleurPositif = QGridLayout()
        self.textCouleurPositif = QLabel("Couleur positive : ")
        self.valeurCouleurPositif = QLineEdit()
        self.valeurCouleurPositif.setText(str(self.live.getColorPositif()))
        self.couleurPositif.addWidget(self.textCouleurPositif,0,0)
        self.couleurPositif.addWidget(self.valeurCouleurPositif,0,1)
        
        self.couleurNegatif = QGridLayout()
        self.textCouleurNegatif = QLabel("Couleur négative : ")
        self.valeurCouleurNegatif = QLineEdit()
        self.valeurCouleurNegatif.setText(str(self.live.getColorNegatif()))
        self.couleurNegatif.addWidget(self.textCouleurNegatif,0,0)
        self.couleurNegatif.addWidget(self.valeurCouleurNegatif,0,1)
        
        self.couleurNeutre = QGridLayout()
        self.textCouleurNeutre = QLabel("Couleur neutre : ")
        self.valeurCouleurNeutre = QLineEdit()
        self.valeurCouleurNeutre.setText(str(self.live.getColorNeutral()))
        self.couleurNeutre.addWidget(self.textCouleurNeutre,0,0)
        self.couleurNeutre.addWidget(self.valeurCouleurNeutre,0,1)
        
        self.elosandGameMode = QGridLayout()
        
        self.eloDebut = QGridLayout()
        self.textEloDebut = QLabel("Elo de départ : ")
        self.valeurEloDebut = QLineEdit()
        self.valeurEloDebut.setText(str(self.live.getStartElo()))
        self.eloDebut.addWidget(self.textEloDebut,0,0)
        self.eloDebut.addWidget(self.valeurEloDebut,0,1)
        
        self.eloActuel = QGridLayout()
        self.textEloActuel = QLabel("Elo actuel : ")
        self.valeurEloActuel = QLineEdit()
        self.valeurEloActuel.setText(str(self.live.getCurrentElo()))
        self.eloActuel.addWidget(self.textEloActuel,0,0)
        self.eloActuel.addWidget(self.valeurEloActuel,0,1)
        
        self.gameMode = QGridLayout()
        self.textGameMode = QLabel("Mode de jeu : ")
        self.valeurGameMode = QComboBox()
        self.valeurGameMode.addItems(self.gameModes.values())
        self.valeurGameMode.setCurrentText(self.gameModes[self.live.getGameMode()])
        self.valeurGameMode.currentTextChanged.connect(self.live.setGameMode)
        self.gameMode.addWidget(self.textGameMode,0,0)
        self.gameMode.addWidget(self.valeurGameMode,0,1)
        
        self.elosandGameMode.addLayout(self.eloDebut,0,0)
        self.elosandGameMode.addLayout(self.eloActuel,0,1)
        self.elosandGameMode.addLayout(self.gameMode,0,2)
        
        self.pseudoAndActualiser = QGridLayout()
        
        self.pseudo = QGridLayout()
        self.textPseudo = QLabel("Pseudo : ")
        self.valeurPseudo = QLineEdit()
        self.valeurPseudo.setText(self.live.getPseudo())
        self.pseudo.addWidget(self.textPseudo,0,0)
        self.pseudo.addWidget(self.valeurPseudo,0,1)
        
        self.actualiser = QGridLayout()
        self.textActualiser = QLabel("Actualiser toute les : ")
        self.valueActualiser = QLineEdit()
        self.valueActualiser.setText(str(self.live.getActualiser()))
        self.s = QLabel("secondes.")
        self.actualiser.addWidget(self.textActualiser,0,0)
        self.actualiser.addWidget(self.valueActualiser,0,1)
        self.actualiser.addWidget(self.s,0,2)
        
        self.pseudoAndActualiser.addLayout(self.pseudo,0,0)
        self.pseudoAndActualiser.addLayout(self.actualiser,0,2)
        
        self.appliquer = QPushButton("Appliquer")
        self.appliquer.clicked.connect(self.apply)
        
        
        self.layout.addLayout(self.couleurPositif,0,0)
        self.layout.addLayout(self.couleurNegatif,1,0)
        self.layout.addLayout(self.couleurNeutre,2,0)
        self.layout.addLayout(self.elosandGameMode,4,0)
        self.layout.addLayout(self.pseudoAndActualiser,6,0)
        self.layout.addWidget(self.appliquer,7,0)
        
    def apply(self):
        self.live.setColorPositif(self.valeurCouleurPositif.text())
        self.live.setColorNegatif(self.valeurCouleurNegatif.text())
        self.live.setColorNeutral(self.valeurCouleurNeutre.text())
        actualiser = int(self.valueActualiser.text())
        self.live.setActualiser(actualiser)
        self.parent.updateTimer(actualiser)
        lastPseudo = self.live.getPseudo()
        self.live.setPseudo(self.valeurPseudo.text())
        
        gamemode = list(self.gameModes.keys())[list(self.gameModes.values()).index(self.valeurGameMode.currentText())]
        currentElo = self.live.getOnlineElo()
        if(currentElo is None):
            self.live.setPseudo(lastPseudo)
            currentElo = self.live.getOnlineElo()
            self.valeurPseudo.setText(lastPseudo)
        if(self.live.getGameMode() != gamemode or self.valeurPseudo.text() != lastPseudo):
            self.live.setGameMode(gamemode)
            self.live.setStartElo(currentElo)
            self.live.setCurrentElo(currentElo)
            self.valeurEloDebut.setText(str(currentElo))
            self.valeurEloActuel.setText(str(currentElo))
            self.parent.buttons.init()
        else:
            self.live.setStartElo(int(self.valeurEloDebut.text()))
            self.live.setCurrentElo(int(self.valeurEloActuel.text()))
            self.parent.buttons.update()
            
        self.live.saveOptions()
        
    def setGameMode(self,gameMode):
        self.live.setGameMode(self.gameModes[self.gameModes.keys()[self.gameModes.values().index(gameMode)]])

    def changeCurrentElo(self,elo):
        self.valeurEloActuel.setText(str(elo))
    
    def changeStartElo(self,elo):
        self.valeurEloDebut.setText(str(elo))