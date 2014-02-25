import pygame
import Game
class PygameView:
    def __init__(self, evManager,game):
        self.evManager = evManager
        self.evManager.registerListener( self )
        self.game = game
        pygame.init()
        self.screen = pygame.display.set_mode((600,400))
        
        self.sector = self.game.mappe.sectors[0]
        self.screen.blit(pygame.image.load(self.sector.image),[0,0,600,400])
        
        self.character = self.game.charactor
        self.charimage = pygame.image.load(self.character.image)
        self.charrect = self.charimage.get_rect()
        self.charrect.topleft = (self.character.x,self.character.y)
        self.screen.blit(self.charimage,self.charrect)
        
        obstacles = self.sector.obstacles
        for obst in obstacles:
            obstimage = pygame.image.load(obst.image)
            obstrect = obstimage.get_rect()
            obstrect.topleft = (obst.x,obst.y)
            
            self.screen.blit(obstimage, obstrect)
        
        
        pygame.display.flip()

		
    def Notify(self, event):
        if event == 'MoveEvent':
            self.charrect.topleft = (self.character.x,self.character.y)
            self.screen.blit(pygame.image.load(self.sector.image),[0,0,600,400])
            self.screen.blit(self.charimage,self.charrect)
            obstacles = self.sector.obstacles
            for obst in obstacles:
                obstimage = pygame.image.load(obst.image)
                obstrect = obstimage.get_rect()
                obstrect.topleft = (obst.x,obst.y)
            
                self.screen.blit(obstimage, obstrect)
            pygame.display.flip()
            pygame.display.update()
            
            