class Enemy:
    def __init__(self):
        self.name = "Pawlettchen"
        self.x = 400
        self.absoultex = self.x
        self.y = 210
        self.steplength = 10
        self.jumpheight = 15
        self.nailcolor = "Red"
        self.image = 'pawlettchen.png'
        self.width = 20
        self.height = 40
        self.maximumjumpheight = 60
        self.direction = "Left"

    def move(self,sector):
        print self.x
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
                
        return a