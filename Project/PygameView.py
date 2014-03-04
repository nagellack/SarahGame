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

        self.ispause = self.game.ispause
        self.pauseimg = pygame.image.load(self.sector.pauseimage)
        
        self.character = self.game.charactor
        self.charimage = pygame.image.load(self.character.image)
        
        self.ambulancename = "ambulance1.png"
                
        self.charrect = self.charimage.get_rect()
        self.charrect.topleft = (self.character.x,self.character.y)
            
        pygame.display.flip()

		
    def Notify(self, event):
        
        if event == "TickEvent":
            if self.game.ispause == 1:
                self.screen.blit(self.pauseimg,[0,0,600,400])
                font = pygame.font.Font(None, 36)
                text1 = font.render(str(self.character.reward1), 1, (255, 255, 10))
                text2 = font.render(str(self.character.reward2), 1, (255, 255, 10))
                textRect1 = text1.get_rect()
                textRect2 = text2.get_rect()
                textRect1.centerx = 200
                textRect1.centery = 200
                textRect2.centerx = 200
                textRect2.centery = 250
                self.screen.blit(text1,textRect1)
                self.screen.blit(text2,textRect2)
                rewimage1 = pygame.image.load('Reward1.png')
                rewimage2 = pygame.image.load('Reward2.png')
                rewrect1 = rewimage1.get_rect()
                rewrect2 = rewimage2.get_rect()
                rewrect1.topleft = (230,180)
                rewrect2.topleft = (230,230)
                self.screen.blit(self.pauseimg,rewrect1,rewrect1)
                self.screen.blit(self.pauseimg,rewrect2,rewrect2)
                self.screen.blit(rewimage1, rewrect1)
                self.screen.blit(rewimage2, rewrect2)

                print self.character.reward1
                print self.character.reward2
                print "--------------------"
            else:
                self.screen.blit(self.sectorimg,self.charrect,self.charrect)
                self.screen.blit(self.sectorimg,[0,0,600,400])
                self.charimage = pygame.image.load(self.character.image)
                if self.character.ambulancex < self.character.x:
                    self.screen.blit(self.charimage,self.charrect)
                
                
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

            pygame.display.flip()
    
        if event == 'MoveEvent':
            self.charrect.topleft = (self.character.x,self.character.y)
            
        if event == 'ChangeSector':
            self.sectorcount+=1
            if self.sectorcount<10:
                self.sector = self.game.mappe.sectors[self.sectorcount]
                self.sectorimg = pygame.image.load(self.sector.image)
            else:
                self.sectorimg = pygame.image.load("party.png")

            
            
