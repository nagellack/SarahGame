import Obstacle

class Sector:
    def __init__(self,identity,numObstacles):
        self.identity = 1 #identity
        self.image = "Sector"+str(self.identity)+".png"
        self.numObstacles = numObstacles
        self.obstacles = []
        self.initObstacles()
    
    def initObstacles(self):
        for i in range(self.numObstacles):
            obstid = 1 #random number
            x = 300
            y = 190
            self.obstacles.append(Obstacle.Obstacle(obstid,x,y))
            
    def hasObstacle(desiredPosition):
        # returns 1 if it has an obstacle and 0 if it hasn in direction 
        return 0
            