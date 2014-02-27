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
        boden = Obstacle.Obstacle(-1,0,250)
        boden.width = 600
        boden.height = 150
        self.obstacles.append(boden)
            
    def hasObstacle(self,desiredPosition,charwidth,charheight):
        # returns 1 if it has an obstacle and 0 if it hasn in direction 
        desx = desiredPosition[0]
        desy = desiredPosition[1]
        possibility = 0
        
        for obst in self.obstacles:
            if (desx<=(obst.x-charwidth) or desx>=(obst.x+obst.width)) or (desy<=(obst.y-charheight) or desy >= (obst.y+obst.height)):
                possibility = 0
            else:
                return 1
        return possibility
        
            