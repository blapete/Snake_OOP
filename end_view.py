import pygame
from constants import *


class EndView():

    def __init__(self, window, message):
        
        self.window = window
        self.message = message

    def draw(self):

        endFont = pygame.font.Font('freesansbold.ttf', 50)

        gameOverSurface = endFont.render('Game Over', True, WHITE)
        gameOverRect = gameOverSurface.get_rect()
        gameOverRect.center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)

        self.window.blit(gameOverSurface, gameOverRect)
        
        self.message()

        return 0