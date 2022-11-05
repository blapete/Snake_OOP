import pygame
from constants import *


class StartView():

    def __init__(self, window, message):

        self.window = window
        self.message = message

    def draw(self):

        startFont = pygame.font.Font('freesansbold.ttf', 40)

        snakeGameSurface = startFont.render('The Snake Game', True, WHITE)
        snakeGameRect = snakeGameSurface.get_rect()
        snakeGameRect.center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)

        self.window.blit(snakeGameSurface, snakeGameRect)

        self.message()

        return True