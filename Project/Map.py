import Sector

class Map:
    def __init__(self):
        self.sectors = []
        self.initSectors()
    
    def initSectors(self):
        for sectorid in range(10):
            numberofObstacles=1 #sollte random nummer 0-3 sein
            sector = Sector.Sector(sectorid,numberofObstacles)
            self.sectors.append(sector)