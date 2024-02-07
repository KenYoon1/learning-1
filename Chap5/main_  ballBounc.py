# 1 - import packages
import pygame
from pygame.locals import *
import sys
import random
from Ball import *

# 2 - Define constants 
BLACK = (0, 0, 0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30

# 3 - Initalize the world 
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH))
