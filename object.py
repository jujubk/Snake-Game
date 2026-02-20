import pygame

class Object:
        
    # def __init__(self):
    #     self.x, self.y = None, None
    #     self.width, self.height = None, None
    #     self.color = None
    #     self.rect = None

    def __init__(self, x, y, w, h, color):
        # call the parent class constructor

        # child class constructor variables
        self.x, self.y = x, y
        self.w, self.h = w, h
        self.color = color
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)

# GET VALUE FUNCTIONS:
    def get_x(self):
        if self.x == None:
            print("This object's x is undefined")
        return self.x
    
    def get_y(self):
        if self.y == None:
            print("This object's y is undefined")
        return self.y
    
    def get_w(self):
        if self.w == None:
            print("This object's width is undefined")
        return self.w
    
    def get_h(self):
        if self.h == None:
            print("This object's height is undefined")
        return self.h
    
    def get_color(self):
        if self.color == None:
            print("This object's color is undefined")
        return self.color
    
# PRINT_VALUE FUNCTIONS:
    def print_x(self):
        print("\nX: ", self.get_x())

    def print_y(self):
        print("\nY: ", self.get_y())
        
    def print_w(self):
        print("\nWidth: ", self.get_w())

    def print_h(self):
        print("\nHeight: ", self.get_h())

    def print_color(self):
        print("\nColor: ", self.get_color())
    
    def print(self):
        self.print_x()
        self.print_y()
        self.print_w()
        self.print_h()
        self.print_color()

# def main():
#     obj = Object(1,2,3,4,"color")

#     obj.print()
# main()