class Charactor:
    def __init__(self):
        self.name = "Sarah"
        self.x = 30
        self.absoultex = self.x
        self.y = 210
        self.steplength = 10
        self.jumpheight = 5
        self.nailcolor = "Red"
        self.image = 'Sarah.png'
        self.width = 20
        self.height = 40
        self.maximumjumpheight = 60
        self.isjumping = 0
    
    def gravity(self, sector):
        if self.isjumping==0:
            newy = self.y+2
            if sector.hasObstacle([self.x,newy],self.width,self.height)==0:
                self.y = newy
            else:
                return 0
        return 1
    
    def jump(self,sector):
        newy = self.y - self.jumpheight #(self.isjumping/2 - (self.maximumjumpheight)**0.5 )**2-self.maximumjumpheight
        if sector.hasObstacle([self.x,newy],self.width,self.height)==0:
            self.y = newy
        else:
            self.isjumping=0
            return 0
        self.isjumping += 1
        print self.isjumping
        if self.isjumping >= 9:
            self.isjumping=0
        return 1
        
    def jumpright(self,sector):
        newy = self.y - self.jumpheight #(self.isjumping/2 - (self.maximumjumpheight)**0.5 )**2-self.maximumjumpheight
        newx = self.x+self.steplength
        
        if sector.hasObstacle([newx,newy],self.width,self.height)==0:
            self.y = newy
            self.x = newx
        else:
            self.isjumping=0
            return 0
        self.isjumping += 1
        if self.isjumping >= 9:
            self.isjumping=0
        return 1
    
    def jumpleft(self,sector):
        newy = self.y - self.jumpheight #(self.isjumping/2 - (self.maximumjumpheight)**0.5 )**2-self.maximumjumpheight
        newx = self.x-self.steplength
        
        if sector.hasObstacle([newx,newy],self.width,self.height)==0:
            self.y = newy
            self.x = newx
        else:
            self.isjumping=0
            return 0
        self.isjumping += 1
        if self.isjumping >= 9:
            self.isjumping=0
        return 1
        
    
    def move(self,direction,sector):
        #check if with steplength 2 and jumheight 2 you can make a move in direction
        if direction == "Right":
            newx = self.x + self.steplength
            newy = self.y
            if sector.hasObstacle([newx,newy],self.width,self.height)==0:
                self.x = newx
                self.y = newy
            else:
                self.gravity(sector)
                self.isjumping=0
                return 0
            
        if direction == "Left":
            newx = self.x - self.steplength
            newy = self.y
            if sector.hasObstacle([newx,newy],self.width,self.height)==0:
                self.x = newx
                self.y = newy
            else:
                self.gravity(sector)
                self.isjumping=0
                return 0
        if direction == "Up":
            newx = self.x 
            newy = self.y - self.jumpheight #(self.isjumping/2 - (self.maximumjumpheight)**0.5 )**2-self.maximumjumpheight
            if sector.hasObstacle([newx,newy],self.width,self.height)==0:
                self.x = newx
                self.y = newy
            else:
                self.gravity(sector)
                self.isjumping=0
                return 0
        if direction == "Down":
            newx = self.x 
            newy = self.y + self.jumpheight #(self.isjumping/2 - (self.maximumjumpheight)**0.5 )**2-self.maximumjumpheight
            if sector.hasObstacle([newx,newy],self.width,self.height)==0:
                self.x = newx
                self.y = newy
            else:
                self.gravity(sector)
                self.isjumping=0
                return 0
                
        return 1