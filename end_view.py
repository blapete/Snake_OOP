import pygame
from constants import *


class EndView():

    def __init__(self, window, font):
        self.window = window
        self.font = font

    def pressKeyMessage(self):
        pressKeySurf = self.font.render('Press a key to play.', True, DARKGRAY)
        pressKeyRect = pressKeySurf.get_rect()
        pressKeyRect.topleft = (WINDOW_WIDTH - 200, WINDOW_HEIGHT - 30)
        self.window.blit(pressKeySurf, pressKeyRect)

    def draw(self):
        font = pygame.font.Font('freesansbold.ttf', 150)
        game = font.render('Game', True, WHITE)
        over = font.render('Over', True, WHITE)
        gameRect = game.get_rect()
        overRect = over.get_rect()
        gameRect.midtop = (WINDOW_WIDTH / 2, 10)
        overRect.midtop = (WINDOW_WIDTH / 2, gameRect.height + 10 + 25)
        self.window.blit(game, gameRect)
        self.window.blit(over, overRect)
        self.pressKeyMessage()