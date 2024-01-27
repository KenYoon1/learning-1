# 1 - import packages
import pygame
from pygame.locals import * 
import sys 

from pathlib import Path

# 2 - Define constants
BLACK = (0, 0, 0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30 

BASE_PATH = Path('anime girl.png')

#pathToBall = BASE_PATH + 'images/ball.png'

# 3 - Initailize the world 
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# 4 - Load assets: iamge(s), sound(s), etc.
ballImage = pygame.image.load('anime girl.png')

# 5 - Initalize variables 

# 6 - Loop forever 
while True: 

    # 7 - Check for and hanle events 
    for event in pygame.event.get():
        # Clicked the close button? Quit pygame and end the program
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 8 - Do any "per frame" actions 
            
    # 9 - Clear the window
    window.fill(BLACK)

    # 10 - Draw all window elements 
    window.blit(ballImage, (100, 200))

    # 11 - Update the window
    pygame.display.update()

    # 12 - Slow things down a bit 
    clock.tick(FRAMES_PER_SECOND)








