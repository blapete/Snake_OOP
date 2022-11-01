

import pygame
from Constants import *


class EndView():

    def __init__(self, window):
        self.window = window

    def draw(self):
        gameOverFont = pygame.font.Font('freesansbold.ttf', 150)
        gameSurf = gameOverFont.render('Game', True, WHITE)
        overSurf = gameOverFont.render('Over', True, WHITE)
        gameRect = gameSurf.get_rect()
        overRect = overSurf.get_rect()
        gameRect.midtop = (WINDOW_WIDTH / 2, 10)
        overRect.midtop = (WINDOW_WIDTH / 2, gameRect.height + 10 + 25)
        self.window.blit(gameSurf, gameRect)
        self.window.blit(overSurf, overRect)