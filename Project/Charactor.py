class Charactor:
    def __init__(self):
        self.name = "Sarah"
        self.x = 30
        self.y = 210
        self.steplength = 2
        self.jumpheight = 2
        self.nailcolor = "Red"
        self.image = 'Sarah.png'
        
    
    def move(self,direction,sectors):
        #check if with steplength 2 and jumheight 2 you can make a move in direction
        # return 1 if can move 0 otherwise
        return 1