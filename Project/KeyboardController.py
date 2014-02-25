import pygame
from pygame.locals import *
class KeyboardController:

    def __init__(self, evManager):
        self.evManager = evManager
        self.evManager.registerListener(self)
        pygame.init()
        pygame.key.set_repeat(1, 10)

    def Notify(self, event):
        ev=None
        if event=="TickEvent":
			#Handle Input Events
            for event in pygame.event.get():
                if event.type == KEYDOWN and event.key == K_LEFT:
                    direction = "DIRECTION_LEFT"
                    ev = "LeftRequest"
                elif event.type == QUIT:
                    ev = QuitEvent()
                elif event.type == KEYDOWN and event.key == K_ESCAPE:
                    ev = QuitEvent()
                elif event.type == KEYDOWN and event.key == K_RIGHT:
                        ev = "RightRequest"                     
        if ev:
            self.evManager.post( ev )
