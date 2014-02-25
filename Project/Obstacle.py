class Obstacle:
    def __init__(self,id):
        self.id = id
        self.image = "Sector"+str(id)+".png"
        self.x = 0
        self.y = 0
        self.width = 0
        self.height = 0
        self.setxywidthheigt()
        
    def setxywidthheigt():
        pass