import pygame

class Snake(pygame.sprite.Sprite):

    COLOR = "green"

    def __init__(self, x, y, width, height):
        self.head = pygame.Rect(x, y, width, height)
        # self.tail = pygame.Rect(x,y,width,height)

        self.vel = 0
        self.direction = "right"
        self.animation_count = 0
        self.len_in_blocks = 2

    def draw(self, direction):

        pass
    