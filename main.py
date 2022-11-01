

import sys
import pygame
from constants import *
from snake import Snake
from apple import Apple
from game_view import *
from start_view import *
from end_view import *
from model import *
from controller import *


pygame.init()
clock = pygame.time.Clock()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Snake game')
BASICFONT = pygame.font.Font('freesansbold.ttf', 18)



oController = Controller(window, clock, BASICFONT)


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