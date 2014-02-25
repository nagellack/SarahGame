import EventManager
import Charactor

class Game:
    def __init__(self, evManager):
        self.evManager = evManager
        self.evManager.RegisterListener(self)
        self.charactor = Charactor()
        #map initialisieren
        #reward initialisieren
        #enemies initialisieren (Array von Enemies)
    
    def start(self):
        # muss aufgerufen werden sobald das spielt startet.
        # muss der gui das signal geben dass das spiel gestartet ist
        # daraufhin muss die gui anfangen die Welt zu erstellen
    
    def getCurrentSectors(self):
        # hier bekommt man von map die aktuellen sectoren
        # damit kann man die hintergrundbilder + die positionen der obstacles bekommen
    
    def processMoveRequest(self,direction,sectors):
        # anfragen ob es möglich ist ein schritt weiter nach oben hinten oder hoch zu gehen
        if self.charactor.move:
            evManager.post("MoveEvent")
    
    def Notify(self, event):
        pass
