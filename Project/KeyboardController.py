import pygame
from pygame.locals import *
class KeyboardController:

    def __init__(self, evManager):
        self.evManager = evManager
        self.evManager.registerListener(self)
        pygame.init()

    def Notify(self, event):
        ev=None
        if event=="TickEvent":
			#Handle Input Events
            for event in pygame.event.get():
                if event.type == KEYDOWN and event.key == K_LEFT:
                    direction = "DIRECTION_LEFT"
                    ev = "LeftRequest"

        if ev:
            self.evManager.post( ev )
