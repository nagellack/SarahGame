import pygame
import Game
class PygameView:
    def __init__(self, evManager,game):
        self.evManager = evManager
        self.evManager.registerListener( self )
        self.game = game
        pygame.init()
        screen = pygame.display.set_mode((600,400))
        
        sector1 = self.game.mappe.sectors[0]
        screen.blit(pygame.image.load(sector1.image),[0,0,600,400])
        
        character = self.game.charactor
        charimage = pygame.image.load(character.image)
        charrect = charimage.get_rect()
        charrect.topleft = (character.x,character.y)
        screen.blit(charimage,charrect)
        
        obstacles = sector1.obstacles
        for obst in obstacles:
            obstimage = pygame.image.load(obst.image)
            obstrect = obstimage.get_rect()
            obstrect.topleft = (obst.x,obst.y)
            
            screen.blit(obstimage, obstrect)
        
        
        pygame.display.flip()

		
    def Notify(self, event):
        if event == 'MoveEvent':
            print 'im mooving mooving'