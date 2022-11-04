import sys, pygame
from constants import *
from model import *
from controller import *


pygame.init()
clock = pygame.time.Clock()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Snake game')
GAME_FONT = pygame.font.Font('freesansbold.ttf', 14)


oController = Controller(window, GAME_FONT)


while True:
    
    for event in pygame.event.get():
       
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            oController.handleEvent(event)

    oController.draw()

    pygame.display.update()

    clock.tick(FRAMES_PER_SECOND)