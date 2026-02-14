import pygame
import random
###

# 
class Dot:

    def __init__(self):

        self.width = 16
        self.height = 16    
        self.color = "white"
        self.x = 0
        self.y = 0

        self.dot = pygame.Rect(self.x,self.y, self.width, self.height)

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def set_color(self, color):
        self.color = color

    def set_x(self,x):
        self.x = x

    def set_y(self, y):
        self.y = y

    # draw the dot on the specified surface
    def draw(self, surface):
        pygame.draw.ellipse(surface, self.color, self.dot, self.width)

# updates the dot position
    # randomizes_coords
    # draw the dot on the surface
    def update(self, surface, x_low, x_high, y_low, y_high):
        
        self.randomize_coords(x_low, x_high, y_low, y_high)
        
        self.draw(surface)

    # get random value in certain given range
    @classmethod
    def random_val(low, high):
        return random.randrange(low, high)

    # randomize the coordinates of the dot
    def randomize_coords(self, x_low, x_high, y_low, y_high):

        # x = Dot.random_val(x_low, x_high)
        # y = Dot.random_val(y_low, y_high)

        x = random.randrange(x_low, x_high)
        y = random.randrange(y_low, y_high)

        self.set_x(x)
        self.set_y(y)
        # print("x,y = ", self.x, self.y)
# 
