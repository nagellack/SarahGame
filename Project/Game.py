import EventManager
import Charactor
import Map

class Game:
    def __init__(self, evManager):
        self.evManager = evManager
        self.evManager.registerListener(self)
        self.charactor = Charactor.Charactor()
        self.mappe = Map.Map()
        #reward initialisieren
        #enemies initialisieren (Array von Enemies)
    
    def start(self):
        pass
        # muss aufgerufen werden sobald das spielt startet.
        # muss der gui das signal geben dass das spiel gestartet ist
        # daraufhin muss die gui anfangen die Welt zu erstellen
    
    def getCurrentSectors(self):
        pass
        # hier bekommt man von map die aktuellen sectoren
        # damit kann man die hintergrundbilder + die positionen der obstacles bekommen
    
    def processMoveRequest(self,direction):
        # anfragen ob es moeglich ist ein schritt weiter nach oben hinten oder hoch zu gehen
        sectors = self.getCurrentSectors()
        if self.charactor.move(direction,sectors):
            self.evManager.post("MoveEvent")
    
    def Notify(self, event):
        if event == "LeftRequest":
            self.processMoveRequest('left')
