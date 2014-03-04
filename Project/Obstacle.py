class Obstacle:
    def __init__(self,identity,x,y):
        self.identity = identity
        self.image = "Obstacle"+str(identity)+".png"
        self.x = x
        self.y = y
        self.width = 0
        self.height = 0
        self.setwidthheigt()
        
    def setwidthheigt(self):
        if self.identity==1:
            self.width = 30
            self.height = 60
            self.y = 250-self.height