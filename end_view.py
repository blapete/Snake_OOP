import pygame
from constants import *


class EndView():

    def __init__(self, window, message):
        
        self.window = window
        self.message = message

    def draw(self):

        # Draw grid
        for x in range(0, WINDOW_WIDTH, CELLSIZE):
            pygame.draw.line(self.window, DARKGRAY, (x, 0), (x, WINDOW_HEIGHT))

        for y in range(0, WINDOW_HEIGHT, CELLSIZE):
            pygame.draw.line(self.window, DARKGRAY, (0, y), (WINDOW_WIDTH, y))

        endFont = pygame.font.Font('freesansbold.ttf', 65)

        gameOverSurface = endFont.render('Game Over', True, WHITE)
        gameOverRect = gameOverSurface.get_rect()
        gameOverRect.center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)

        self.window.blit(gameOverSurface, gameOverRect)
        
        self.message()

        return 2