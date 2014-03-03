class Charactor:
    def __init__(self):
        self.name = "Sarah"
        self.x = 30
        self.absoultex = self.x
        self.y = 210
        self.steplength = 5
        self.jumpheight = 10
        self.nailcolor = "Red"
        self.image = 'Sarah.png'
        self.width = 20
        self.height = 40
        self.maximumjumpheight = 60
        self.isjumping = 0
        self.rewardcount = 0
        self.isalive = 1
        self.fighting = 0
        
        self.standingright = 'sarah.png'
        self.standingleft = 'sarahl.png'
        self.movingright = 'sarahmove.png'
        self.movingleft = 'sarahmovel.png'
        self.jumpingright = 'sarahjump.png'
        self.jumpingleft = 'sarahjumpl.png'
    
    def gravity(self, sector):
        if self.isjumping==0:
            newy = self.y+5
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
        if self.isjumping >= 9:
            self.isjumping=0
        return 1
        
    def jumpright(self,sector):
        newy = self.y - self.jumpheight #(self.isjumping/2 - (self.maximumjumpheight)**0.5 )**2-self.maximumjumpheight
        newx = self.x+self.steplength
        
        if sector.hasObstacle([newx,newy],self.width,self.height)==0:
            self.y = newy
            self.x = newx
            self.absoultex+=self.steplength
            self.image=self.jumpingright
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
            if self.x>=0:
                    self.absoultex-=self.steplength
            self.image=self.jumpingleft
        else:
            self.isjumping=0
            return 0
        self.isjumping += 1
        if self.isjumping >= 9:
            self.isjumping=0
        return 1
     
    def stopjump(self):
        self.isjumping=0  
        
    def isdying(self,sector):
        #pruefen ob enemy sie trifft 
        #wenn sie nicht kaempft dann sterben
        #wenn sie kaempft dann enemy stirbt
        for enemy in sector.enemies:
            if (self.x<=(enemy.x-self.width) or self.x>=(enemy.x+enemy.width)) or (self.y<=(enemy.y-self.height) or self.y >= (enemy.y+enemy.height)):
                self.isalive = 1
            else:
                if self.fighting:
                    self.isalive=1
                    enemy.isalive=0
                else:
                    self.isalive=0
                    return 1
        return 0
            
    
    
    def move(self,direction,sector):
        #check if with steplength 2 and jumheight 2 you can make a move in direction
        if direction == "Right":
            newx = self.x + self.steplength
            newy = self.y
            if sector.hasObstacle([newx,newy],self.width,self.height)==0:
                if sector.hasReward([newx,newy],self.width,self.height)==1:
                    self.rewardcount += 1
                self.x = newx
                self.y = newy
                self.absoultex+=self.steplength
                if self.isjumping==0:
                    if self.image!='sarahmove.png':
                        self.image='sarahmove.png'
                    else:
                        self.image='sarah.png'
            else:
                self.gravity(sector)
                self.isjumping=0
                return 0
            
        if direction == "Left":
            newx = self.x - self.steplength
            newy = self.y
            if sector.hasObstacle([newx,newy],self.width,self.height)==0:
                if sector.hasReward([newx,newy],self.width,self.height)==1:
                    self.rewardcount += 1
                self.x = newx
                if self.x>=0:
                    self.absoultex-=self.steplength
                self.y = newy
                if self.isjumping==0:
                    if self.image!='sarahmovel.png':
                        self.image='sarahmovel.png'
                    else:
                        self.image='sarahl.png'
            else:
                self.gravity(sector)
                self.isjumping=0
                return 0
            
        if direction == "Up":
            newx = self.x 
            newy = self.y - self.jumpheight #(self.isjumping/2 - (self.maximumjumpheight)**0.5 )**2-self.maximumjumpheight
            if sector.hasObstacle([newx,newy],self.width,self.height)==0:
                if sector.hasReward([newx,newy],self.width,self.height)==1:
                    self.rewardcount += 1
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
                if sector.hasReward([newx,newy],self.width,self.height)==1:
                    self.rewardcount += 1
                self.x = newx
                self.y = newy
            else:
                self.gravity(sector)
                self.isjumping=0
                return 0
                
        return 1
