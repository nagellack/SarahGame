import Sector

class Map:
    def __init__(self):
        self.sectors = []
        self.initSectors()
    
    def initSectors(self):
        for i in range(10):
            numberofObstacles=3 #sollte random nummer 0-3 sein
            sector = Sector(i,numberofObstacles)
            self.sectors.add(sector)