import Sector

class Map:
    def __init__(self):
        self.sectors = []
        self.initSectors()
    
    def initSectors(self):
        for sectorid in range(5):
            numberofObstacles=1 #sollte random nummer 0-3 sein
<<<<<<< HEAD
            numberofEnemies=3
            numberofRewards = 2
            sector = Sector.Sector(sectorid,numberofObstacles,numberofEnemies,numberofRewards)
=======
            numberofEnemies=1
            sector = Sector.Sector(sectorid,numberofObstacles,numberofEnemies)
>>>>>>> fa2bdd049ba40796b137ebefd948c94b4bc6d248
            self.sectors.append(sector)
    
    def getcurrentsector(self,xvalue):
        return self.sectors[int(xvalue/600)]
        
