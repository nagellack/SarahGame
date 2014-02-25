class Charactor:
    def __init__(self):
        self.name = "Sarah"
        self.x = 30
        self.absoultex = self.x
        self.y = 210
        self.steplength = 2
        self.jumpheight = 2
        self.nailcolor = "Red"
        self.image = 'Sarah.png'
        
    
    def move(self,direction,sector):
        #check if with steplength 2 and jumheight 2 you can make a move in direction
        # return 1 if can move 0 otherwise
        if direction == "Right":
            self.x += self.steplength
        if direction == "Left":
            self.x -= self.steplength
        return 1