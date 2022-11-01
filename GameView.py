
import sys
import pygame
from Constants import *
from snake import Snake
from apple import Apple


class GameView():

    def __init__(self):
        pass

    def drawGrid(self, screen):
        for x in range(0, WINDOW_WIDTH, CELLSIZE):  # draw vertical lines
            pygame.draw.line(screen, DARKGRAY, (x, 0), (x, WINDOW_HEIGHT))

        for y in range(0, WINDOW_HEIGHT, CELLSIZE):  # draw horizontal lines
            pygame.draw.line(screen, DARKGRAY, (0, y), (WINDOW_WIDTH, y))
