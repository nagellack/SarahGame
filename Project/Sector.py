import Obstacle

class Sector:
    def __init__(self,id,numObstacles):
        self.id = id
        self.imgae = "Sector"+str(id)+".png"
        self.obstacles = []
        self.initObstacles()
    
    def initObstacles(self):
        for i in range self.numObstacles:
            obstid = 1 #random number
            self.obstacles.add(Obstacle(obstid))
            
    def hasObstacle(direction):
        # returns 1 if it has an obstacle and 0 if it hasn in direction 
        return 0
            