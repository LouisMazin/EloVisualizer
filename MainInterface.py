from SettingsInterface import SettingsInterface
from ButtonsInterface import ButtonsInterface
from PyQt6.QtWidgets import QMainWindow,QApplication,QTabWidget
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import QTimer
import qt_material

class Interface(QMainWindow):
    def __init__(self,app,live):
        super().__init__()
        self.live = live
        self.dpi =  app.primaryScreen().devicePixelRatio()
        qt_material.apply_stylesheet(self, theme='dark_amber.xml')
        self.setStyleSheet(self.styleSheet()+"""*{background-color: transparent;color: #ffffff;border: none;padding: 0;margin: 0;line-height: 0;font-family: "Segoe UI", sans-serif;}QWidget{color: #ffffff;}QLabel{color: #ffffff;}""")
        self.initUI()
        self.buttons.update(True)
    def initUI(self):
        self.setWindowTitle("Elo Tracker")
        self.setWindowIcon(QIcon("icon.ico"))
        self.setGeometry(100,100,int(700/self.dpi),int(700/self.dpi))
        self.onglets = QTabWidget(self)
        self.buttons = ButtonsInterface(self)
        self.settings = SettingsInterface(self)
        self.onglets.addTab(self.buttons,"Boutons")
        self.onglets.addTab(self.settings,"Paramètres")
        self.setCentralWidget(self.onglets)
        self.timer = QTimer()
        self.timer.timeout.connect(self.buttons.update)
        self.updateTimer(self.live.getActualiser())
    def updateTimer(self,actualiser):
        if(self.timer.isActive()):
            self.timer.stop()
        self.timer.start(actualiser*1000)
    
def execute(live):  
    app = QApplication([])
    window = Interface(app,live)
    window.show()
    app.exec()
