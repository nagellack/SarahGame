import pygame

class Player(pygame.sprite.Sprite):

    def __init__(self, position):

        self.sheet = pygame.image.load('walkingman.png')
        self.sheet.set_clip(pygame.Rect(0,0,30,30))
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect()
        self.rect.topleft = position
        self.frame = 0
        self.left_states = {0:(0,0,30,30),1:(31,0,30,30)}
        self.right_states = {0:(0,30,30,30),1:(31,31,30,30)}

    def get_frame(self, frame_set):
        
        self.frame += 1
        if self.frame > (len(frame_set)-1):
            self.frame=0
        return frame_set[self.frame]

    def clip(self, clipped_rect):
        if type(clipped_rect) is dict:
            self.sheet.set_clip(pygame.Rect(self.get_frame(clipped_rect)))
        else:
            self.sheet.set_clip(pygame.Rect(clipped_rect))
        return clipped_rect

    def update(self, direction):
        if direction == 'left':
            self.clip(self.left_states)
            self.rect.x -=5

        if direction == 'right':
            self.clip(self.right_states)
            self.rect.x +=5

        if direction == 'stand_left':
            self.clip(self.left_states[0])

        if direction == 'stand_right':
            self.clip(self.right_states[0])

        self.image = self.sheet.subsurface(self.sheet.get_clip())

    def handle_event(self, event):
        if event.type == pygame.QUIT:
            game_over=True

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:

                self.update('left')

            if event.key == pygame.K_RIGHT:
                self.update('right')

        if event.type == pygame.KEYUP:

            if event.key == pygame.K_LEFT:
                self.update('stand_left')

            if event.key == pygame.K_RIGHT:
                self.update('stand_right')
            
    
