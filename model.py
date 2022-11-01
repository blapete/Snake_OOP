

import pygame
from constants import *


class Model():

    def __init__(self):
        self.score = 0

    def draw(self, window, font, score):
        scoreSurf = font.render('Score: %s' % (score), True, WHITE)
        scoreRect = scoreSurf.get_rect()
        scoreRect.topleft = (WINDOW_WIDTH - 120, 10)
        window.blit(scoreSurf, scoreRect)