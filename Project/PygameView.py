import pygame
from pygame.locals import *
import Game

class PygameView:
    def __init__(self, evManager,game):
        self.evManager = evManager
        self.evManager.registerListener( self )
        self.game = game
        pygame.init()
        self.screen = pygame.display.set_mode((600,400),DOUBLEBUF)
        self.screen.set_alpha(None)
        self.sectorcount = 0
        self.sector = self.game.mappe.sectors[self.sectorcount]
        self.sectorimg = pygame.image.load(self.sector.image)
        self.screen.blit(self.sectorimg,[0,0,600,400])

        self.ispause = 0
        self.pauseimg = pygame.image.load(self.sector.pauseimage)
        
        self.character = self.game.charactor
        self.charimage = pygame.image.load(self.character.image)
        
        self.ambulancename = "ambulance1.png"
                
        self.charrect = self.charimage.get_rect()
        self.charrect.topleft = (self.character.x,self.character.y)
        
        self.win = 0
            
        pygame.display.flip()

		
    def Notify(self, event):
        
        if event == "TickEvent":
            if self.game.ispause == 1:
                self.screen.blit(self.pauseimg,[0,0,600,400])
            elif self.win:
                self.screen.blit(self.sectorimg,self.charrect,self.charrect)
                self.screen.blit(self.sectorimg,[0,0,600,400])
                self.charimage = pygame.image.load(self.character.image)
                self.screen.blit(self.charimage,self.charrect)
            else:
                self.screen.blit(self.sectorimg,self.charrect,self.charrect)
                self.screen.blit(self.sectorimg,[0,0,600,400])
                self.charimage = pygame.image.load(self.character.image)
                if self.character.ambulancex < self.character.x:
                    self.screen.blit(self.charimage,self.charrect)
                    
                obstacles = self.sector.obstacles
                for obst in obstacles:
                    obstimage = pygame.image.load(obst.image)
                    obstrect = obstimage.get_rect()
                    obstrect.topleft = (obst.x,obst.y)
                    self.screen.blit(self.sectorimg,obstrect,obstrect)
                    self.screen.blit(obstimage, obstrect)
    
                rewards = self.sector.rewards
                for rew in rewards:
                    rewimage = pygame.image.load(rew.image)
                    rewrect = rewimage.get_rect()
                    rewrect.topleft = (rew.x,rew.y)
                    self.screen.blit(self.sectorimg,rewrect,rewrect)
                    self.screen.blit(rewimage, rewrect)
                
                
                enemies = self.sector.enemies
                for  enemy in enemies:
                    if enemy.alive:
                        enemimage = pygame.image.load(enemy.image)
                        enemrect = enemimage.get_rect()
                        enemrect.topleft = (enemy.x,enemy.y)
                        self.screen.blit(self.sectorimg,enemrect,enemrect)
                        self.screen.blit(enemimage,enemrect)
                        
                if self.character.isalive:
                    self.screen.blit(self.charimage,self.charrect)
                else:
    
                    self.evManager.post('Fainting')
                    ambulanceimg = pygame.image.load(self.ambulancename)
                    ambrect = ambulanceimg.get_rect()
                    ambrect.topleft = (self.character.ambulancex,194)
                    self.screen.blit(self.sectorimg,ambrect,ambrect)
                    self.screen.blit(ambulanceimg,ambrect)
                    if self.ambulancename == "ambulance1.png":
                        self.ambulancename = "ambulance2.png"
                    else:
                        self.ambulancename = "ambulance1.png"
                    if self.character.ambulancex>=600:
                        font = pygame.font.Font(None, 36)
                        text = font.render('Press R to Restart', 1, (10, 10, 10))
                        textpos = text.get_rect(centerx=self.screen.get_width()/2)
                        self.screen.blit(text, textpos)
                    


            pygame.display.flip()
    
        if event == 'MoveEvent':
            self.charrect.topleft = (self.character.x,self.character.y)
            
        if event == 'ChangeSector':
            self.sectorcount+=1
            if self.sectorcount<8:
                self.sector = self.game.mappe.sectors[self.sectorcount]
                self.sectorimg = pygame.image.load(self.sector.image)
            else:
                self.sectorimg = pygame.image.load("Party.png")
                self.win=1
                pygame.mixer.init()
                pygame.mixer.music.load("indaclub.mp3")
                pygame.mixer.music.play()
                

            
            
