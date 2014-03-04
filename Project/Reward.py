class Reward:
    def __init__(self,identity,x,y,element):
        self.identity = identity
        self.image = "Reward"+str(self.identity)+".png"
        self.x = x
        self.y = y
        self.width = 0
        self.height = 0
        self.setwidthheigt()
        # element in reward list
        self.element = element
        
    def setwidthheigt(self):
        if self.identity==1:
            self.width = 20
            self.height = 40
