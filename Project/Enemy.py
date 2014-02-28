class Enemy:
    def __init__(self,identity,xpos):
        self.name = "Pawlettchen"
        self.x = xpos
        self.absoultex = self.x
        self.y = 210
        self.steplength = 5
        self.jumpheight = 15
        self.nailcolor = "Red"
        self.image = 'pawlettchen.png'
        self.width = 20
        self.height = 40
        self.maximumjumpheight = 60
        self.direction = "Left"
        self.alive = 1

    def move(self,sector):
        a = 1
        if self.direction == "Right":
            newx = self.x + self.steplength
            newy = self.y
            if sector.hasObstacle([newx,newy],self.width,self.height)==0:
                self.x = newx
                self.y = newy
            else:
                self.direction="Left"
                a = 0
            if newx >=600-self.width:
                self.direction="Left"
                a = 0
        
        if self.direction == "Left":
            newx = self.x - self.steplength
            newy = self.y
            if sector.hasObstacle([newx,newy],self.width,self.height)==0:
                self.x = newx
                self.y = newy
            else:
                self.direction="Right"
                a =  0
            if newx <=0:
                self.direction="Right"
                a = 0
                
        return a