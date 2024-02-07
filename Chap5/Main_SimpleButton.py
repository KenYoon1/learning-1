# 1 - Import Packages 
import pygame
from pygame.locals import * 
import sys 
import random

from Ball import * 
from SimpleButton import * 

# 2 - Define constants 
BLACK = (0, 0, 0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30 

# 3 - Initialize the world 
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock() 

# 4 - Load assets: image(s), sound(s), etc. 

# 5 - Initialize variables 
oButton = SimpleButton(window, (150, 30), 
                       'images/bottonUp.png',
                       'images/buttonDown.png')

# 6 - Look forever 
while True: 

    # 7 - Check for and handle events 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
        if oButton.handleEvent(event): 
            print('User has clicked the button')

    # 8 - do any "per frame" actions 

    # 9 - Clear the window before drawing it again 
    window.fill(GRAY)

    # 10 - Draw the window elements 
    oButton.draw()

    # 11 - Update the window 
    pygame.display.update() 

    # 12 - Slow things down a bit 
    clock.tick(FRAMES_PER_SECOND)
