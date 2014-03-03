import EventManager
import Charactor
import Enemy
import Map

class Game:
    def __init__(self, evManager):
        self.evManager = evManager
        self.evManager.registerListener(self)
        self.charactor = Charactor.Charactor()
        self.enemies = []
        self.mappe = Map.Map()
        #reward initialisieren
        #enemies initialisieren (Array von Enemies)
    
    def start(self):
        pass
        # muss aufgerufen werden sobald das spielt startet.
        # muss der gui das signal geben dass das spiel gestartet ist
        # daraufhin muss die gui anfangen die Welt zu erstellen
    
    def getCurrentSectors(self):
         return self.mappe.getcurrentsector(self.charactor.absoultex)
        # hier bekommt man von map die aktuellen sectoren
        # damit kann man die hintergrundbilder + die positionen der obstacles bekommen
    
    def processMoveRequest(self,direction):
        # anfragen ob es moeglich ist ein schritt weiter nach oben hinten oder hoch zu gehen
        currentS = self.getCurrentSectors()
        if self.charactor.isalive:
            if self.charactor.move(direction,currentS):
                if self.charactor.x >=600:
                    self.evManager.post("ChangeSector")
                    self.charactor.x=0
                if self.charactor.x<0:
                    self.charactor.x=0
                self.evManager.post("MoveEvent")
    
    def Notify(self, event):
        if event == "LeftRequest":
            self.processMoveRequest('Left')
        elif event == "RightRequest":
            self.processMoveRequest('Right')
        elif event == "UpRequest":
            self.processMoveRequest('Up')
        elif event == "RightUpRequest":
            self.processMoveRequest('RightUp')
        elif event == "LeftUpRequest":
            self.processMoveRequest('LeftUp')
        elif event == "DownRequest":
            self.processMoveRequest('Down')
        elif event == "Gravity":
            currentS = self.getCurrentSectors()
            if self.charactor.gravity(currentS):
                self.evManager.post("MoveEvent")
        elif event == "Jump":
            currentS = self.getCurrentSectors()
            if self.charactor.hasFeetonTheGround(currentS):
                if self.charactor.jump(currentS):
                    self.evManager.post("MoveEvent")

        elif event == "Enemy":
            currentS = self.getCurrentSectors()
            for enemy in currentS.enemies:
                enemy.move(currentS)
                #    self.evManager.post("MoveEvent")
            

        elif event == "JumpRight":
            currentS = self.getCurrentSectors()
            if self.charactor.hasFeetonTheGround(currentS):
                if self.charactor.jumpright(currentS):
                    self.evManager.post("MoveEvent")
        elif event == "JumpLeft":
            currentS = self.getCurrentSectors()
            if self.charactor.hasFeetonTheGround(currentS):
                if self.charactor.jumpleft(currentS):
                    self.evManager.post("MoveEvent")
        elif event == "Stopjump":
            self.charactor.stopjump()
        elif event == "Alive":
            currentS = self.getCurrentSectors()
            self.charactor.isdying(currentS)
        elif event == "Fighting":
            self.charactor.image = "sarahfight.png"
            self.charactor.fighting = 1
        elif event == "NOFighting":
            if self.charactor.fighting:
                self.charactor.image = "sarah.png"
                self.charactor.fighting = 0
        elif event == "Fainting":
            self.charactor.faint()
            

        
