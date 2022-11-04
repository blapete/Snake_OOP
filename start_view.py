import pygame
from constants import *


class StartView():

    def __init__(self, window, font, message):

        self.window = window
        self.font = font
        self.message = message

        self.titleFont = pygame.font.Font('freesansbold.ttf', 50)
        self.titleSurface = self.titleFont.render('Snake game', True, WHITE)

    def draw(self):

        startViewTitleRect = self.titleSurface.get_rect()
        startViewTitleRect.center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
        self.window.blit(self.titleSurface, startViewTitleRect)

        # pressKeySurface = self.font.render('Press a key to play.', True, DARKGRAY)
        # pressKeyRect = pressKeySurface.get_rect()
        # pressKeyRect.topleft = (WINDOW_WIDTH - 200, WINDOW_HEIGHT - 30)
        # self.window.blit(pressKeySurface, pressKeyRect)
        self.message()

        return True