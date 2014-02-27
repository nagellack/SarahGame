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
            if self.jumpstarted != 0:
                ev = "UpRequest"
                if self.jumpstarted<7:
                    self.jumpstarted+=1
                else:
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
                    print 'right'
                if event.type == KEYDOWN and event.key == K_UP:
                    ev = "UpRequest"
                    if self.jumpstarted == 0:
                        self.jumpstarted = 1
                                                                 
        if ev:
            self.evManager.post( ev )
