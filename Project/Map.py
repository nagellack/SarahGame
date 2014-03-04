import Sector
import random
class Map:
    def __init__(self):
        self.sectors = []
        self.initSectors()
    
    def initSectors(self):
        for sectorid in range(5):
            numberofObstacles=random.randrange(1, 4,1)
            numberofEnemies=random.randrange(1, 4,1)
            numberofRewards = random.randrange(1, 6,1)
            sector = Sector.Sector(sectorid,numberofObstacles,numberofEnemies,numberofRewards)
            self.sectors.append(sector)
    
    def getcurrentsector(self,xvalue):
        return self.sectors[int(xvalue/600)]
        
