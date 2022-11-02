import pygame
from constants import *


class StartView():

    def __init__(self, window, font):
        self.window = window
        self.font = font
        self.titleFont = pygame.font.Font('freesansbold.ttf', 50)
        self.titleSurf1 = self.titleFont.render('Snake game', True, WHITE)
        self.degrees1 = 0

    def draw(self):
        self.window.fill(BACKGROUND)

        theRect = self.titleSurf1.get_rect()
        theRect.center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
        self.window.blit(self.titleSurf1, theRect)

        pressKeySurf = self.font.render('Press a key to play.', True, DARKGRAY)
        pressKeyRect = pressKeySurf.get_rect()
        pressKeyRect.topleft = (WINDOW_WIDTH - 200, WINDOW_HEIGHT - 30)
        self.window.blit(pressKeySurf, pressKeyRect)