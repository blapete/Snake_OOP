# Packages
import sys, pygame
from constants import *
from controller import Controller

# Constants
FRAMES_PER_SECOND = 12

# Initialize pygame
pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption('Snake game')
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))


# Variables
oController = Controller(window)


# Infinite loop
while True:
    
    # Event check
    for event in pygame.event.get():
       
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            oController.handleEvent(event)

    # Clear the window
    window.fill(BLACK)

    # Draw window element
    oController.draw()

    # Update the window
    pygame.display.update()

    # Control game speed
    clock.tick(FRAMES_PER_SECOND)