import pygame
import object 
'''
    # a snake object will be made up of multiple Objects, representing the snakes body parts. 
    # there will be a sorted list of objects (body parts) of the snake
    # every time 
'''
class Snake():

    # def __init__(self):
    #           #
    #     self.snake_obj = None
    #     self.velocity = None
    #     self.direction = None
    #     self.length = None

    #     # initial snake objects
    #     self.snake_coords = None

    def __init__(self, velocity, x, y, w, h, color):
        #
        self.snake_obj = object.Object(x, y, w, h, color)

        self.velocity = velocity
        self.direction = "right"
        self.length = 2

        # initial snake objects
        self.snake_coords = [[x,y],
                             [x-16,y]]

# GET_VALUE FUNCTIONS
    def get_x(self):
        self.snake_obj.get_x()

    def get_y(self):
        self.snake_obj.get_y()

    def get_width(self):
        self.snake_obj.get_w()

    def get_height(self):
        self.snake_obj.get_h()

    def get_color(self):
        self.snake_obj.get_color()
    
    def get_velocity(self):
        if self.velocity == None:
            print("This object's velocity is undefined")
        return self.velocity
        
    def get_direction(self):
        if self.direction == None:
            print("This object's direction is undefined")
        return self.direction
    
    def get_length(self):
        if self.length == None:
            print("This object's length is undefined")
        return self.length
    
    def get_snake_coords(self):
        if self.snake_coords == None:
            print("There are no recorded coordinates for this object")
        return self.snake_coords
    
    def get_snake_obj(self):
        if self.snake_obj == None:
            print("This object has no defined Object")
        return self.snake_obj
    
# PRINT_VALUE FUNCTIONS:    
    def print_velocity(self):
        print("\nVelocity: ", self.get_velocity())

    def print_direction(self):
        print("\nDirection: ", self.get_direction())
    
    def print_length(self):
        print("\nLength: ", self.get_length())

    def print_snake_coords(self):
        print("\nSnake Coordinates: ", self.get_snake_coords())

    def print(self):
        self.snake_obj.print()
        self.print_velocity()
        self.print_direction()
        self.print_length()
        self.print_snake_coords()

#####
    def valid_direction(self, new_direction):
        if new_direction == "right" and self.direction == "left":
            return False
        elif new_direction == "down" and self.direction == "up":
            return False
        elif new_direction == "left" and self.direction == "right":
            return False
        elif new_direction == "up" and self.direction == "down":
            return False
        
        return True
        
# MOVEMENT FUNCTIONS:

    # updates location of snake on the surface using the snake_coords list
    def update(self, surface):
        
        for coord in self.snake_coords:

            # get current x and y values of the snake section being printed
            curr_x, curr_y = coord[0], coord[1]

            # rect for the current section being printed
            section_rect = pygame.Rect(curr_x, curr_y, 16,16)

            # put the snake on the surface
            pygame.draw.rect(surface, "green", section_rect)

# This function will update the snake_coords based on new direction
    # these do no print out the 
    # def move(self, direction):

    #     # reversed snake coords:
    #     # reversed_coords = self.snake_coords.reverse()
    # # loop that shifts the snake coords over
    # # - only the first coord in the list depends on the direction
    #     for i in range(self.length-1,0, -1):
    #         self.snake_coords[i] = self.snake_coords[i-1]

    #     print("current coordinates: ", self.print_snake_coords())
    #     print("current direction: ", self.get_direction())
    #     print("move to the: ", direction)

    #     # check if direction value is valid:
    #     if self.valid_direction(direction):
    #         self.direction = direction 
    #         # otherwise, current direction stays the same

    #     match(direction):
    #         case "right":
    #             # (x+16,y)
    #             self.snake_coords[0][0] += 16
                
    #         case "left":
    #             # (x-16, y)
    #             self.snake_coords[0][0] -= 16

    #         case "up":
    #             # (x, y-16)
    #             self.snake_coords[0][1] -= 16

    #         case "down":
    #             # (x, y+16)
    #             self.snake_coords[0][1] += 16
                
    #     print("new snake coordinates: ", self.print_snake_coords())
    #     # update the window with new snake coords
    #     # self.update(surface)
        
