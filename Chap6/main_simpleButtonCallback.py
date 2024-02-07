# pygame demo 9 - 3-button test with callbacks

# 1 - Import packages
import pygame
from pygame.locals import *
from SimpleButton import * 
import sys

# 2 - Define constants
GRAY = (200, 200, 200)
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 100
FRAMES_PER_SECOND = 30

# Define a function to be used as a "callback"
def myCallBackFunction():
    print('User pressed Button B, called myCallBackFunction')

# Define a class with a method to be used as a "callback"
class CallBackTest(): 

    def myMethod(self):
        print('User Pressed ButtonC, called myMethod of the CallBackTest object')

# 3 Initalize the world 
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# 4 - Load assets: image(s), sound(s), etc.

# 5 - 








