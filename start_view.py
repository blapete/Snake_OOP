import pygame
from constants import *


class StartView():

    def __init__(self, window, message):

        self.window = window
        self.message = message

    def draw(self):

        titleFont = pygame.font.Font('freesansbold.ttf', 40)

        titleSurface = titleFont.render('The Snake Game', True, WHITE)
        titleRect = titleSurface.get_rect()
        titleRect.center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)

        self.window.blit(titleSurface, titleRect)

        self.message()

        return True