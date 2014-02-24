#SarahGame

import pygame, sys 
from pygame.locals import * 


class Game(object):
    def main(self, screen):
        clock = pygame.time.Clock() 
        image=pygame.image.load('myman.png') #image of my main man
        x_spot=320
        y_spot=140
        floor=240
        jump=0
        while True: # main game loop
            clock.tick(30) #limiting to 30 frames a second
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN and event.key ==  pygame.K_SLASH:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN and event.key ==  pygame.K_LEFT:
                    x_spot-=10
                if event.type == pygame.KEYDOWN and event.key ==  pygame.K_RIGHT:
                    x_spot+=10
                if event.type == pygame.KEYDOWN and event.key ==  pygame.K_UP:
                    jump=1
                    count=0
                
            if jump==1:
                j=15
                y_spot+=((count-j)^2+j^2)
                count+=1
                if y_spot >= floor:
                    jump=0
                    count=0
                    y_spot= floor
                print y_spot
            pygame.display.update()
            screen.fill((200,200,200))
            screen.blit(image,(x_spot,y_spot))
            pygame.display.flip
                        

if __name__ == '__main__':
    pygame.init() 
    screen = pygame.display.set_mode((400, 300))
    pygame.display.set_caption('Sarah Game') 
    Game().main(screen)

