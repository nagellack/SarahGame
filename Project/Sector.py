import Obstacle
import Enemy
import random
import Reward

class Sector:
    def __init__(self,identity,numObstacles,numEnemies,numRewards):
        self.identity = identity+1
        self.image = "Sector"+str(self.identity)+".png"
        self.pauseimage = "Pause.png"
        self.numObstacles = numObstacles
        self.obstacles = []
        self.initObstacles()

        # rewards
        self.numRewards = numRewards
        self.rewards = []
        self.initRewards()

        self.numEnemies= numEnemies
        self.enemies = []
        self.initEnemies()
    
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

    def initRewards(self):
        element = 0
        for i in range(self.numRewards):
            rewardid = 1
            x = 150 + i*50
            y = 190 + i*30
            self.rewards.append(Reward.Reward(rewardid,x,y,element+i))

    
    def initEnemies(self):
        for i in range(self.numEnemies):
            enemyid = i #random number
            x = random.randrange(0, 600,1)
            self.enemies.append(Enemy.Enemy(enemyid,x))
            
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
        return 0

    def hasReward(self,desiredPosition,charwidth,charheight):
        # returns 1 if it has an reward and 0 if it hasn in direction
        desx = desiredPosition[0]
        desy = desiredPosition[1]
        possibility = 0

        rewcounter = 0
        for rew in self.rewards:
            if (desx <= (rew.x-charwidth) or desx >= (rew.x+rew.width)) or (desy <= (rew.y-charheight) or desy >= (rew.y+rew.height)):
                possibility = 0
            else:
                print "hit"
                print rew
                del self.rewards[rewcounter]
                possibility = 1
            rewcounter += 1
        return possibility

            
