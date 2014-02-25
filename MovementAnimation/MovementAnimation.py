import pygame
import player

pygame.init()

screen = pygame.display.set_mode((640,480))
pygame.display.set_caption("Walking Animation")
clock = pygame.time.Clock()
playa = player.Player((150,150))

game_over = False

while game_over == False:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    playa.handle_event(event)
    screen.fill(pygame.Color('blue'))
    screen.blit(playa.image, playa.rect)

    pygame.display.flip()
    clock.tick(30)
    pygame.display.update()

pygame.quit()
        
