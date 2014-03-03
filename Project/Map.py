import Sector

class Map:
    def __init__(self):
        self.sectors = []
        self.initSectors()
    
    def initSectors(self):
        for sectorid in range(5):
            numberofObstacles=1 #sollte random nummer 0-3 sein
            numberofEnemies=3
            numberofRewards = 2
            sector = Sector.Sector(sectorid,numberofObstacles,numberofEnemies,numberofRewards)
            self.sectors.append(sector)
    
    def getcurrentsector(self,xvalue):
        return self.sectors[int(xvalue/600)]
        
