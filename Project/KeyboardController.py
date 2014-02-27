import pygame
from pygame.locals import *
class KeyboardController:

    def __init__(self, evManager):
        self.evManager = evManager
        self.evManager.registerListener(self)
        pygame.init()
        pygame.key.set_repeat(1, 10)
        self.jumpstarted = 0

    def Notify(self, event):
        ev=None
        if event=="TickEvent":
            self.evManager.post('Gravity')
            if self.jumpstarted!=0:
                key = pygame.key.get_pressed()
                ev = 'Jump'
                if key[K_RIGHT]:
                    ev="RightUpRequest"
                if key[K_LEFT]:
                    ev="LeftUpRequest"
                self.evManager.post(ev)
                self.jumpstarted +=1
                if self.jumpstarted==10:
                    self.jumpstarted=0
            for event in pygame.event.get():
                if event.type == KEYDOWN and event.key == K_LEFT:
                    direction = "DIRECTION_LEFT"
                    ev = "LeftRequest"
                if event.type == QUIT:
                    ev = QuitEvent()
                if event.type == KEYDOWN and event.key == K_ESCAPE:
                    ev = QuitEvent()
                if event.type == KEYDOWN and event.key == K_RIGHT:
                    ev = "RightRequest" 
                if event.type == KEYDOWN and event.key == K_UP:
                    if self.jumpstarted==0:
                        self.jumpstarted = 1
                if event.type == KEYDOWN and event.key == K_DOWN:
                    ev='DownRequest' 
                                                                 
        if ev:
            self.evManager.post( ev )
