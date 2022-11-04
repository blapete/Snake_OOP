import pygame
from constants import *


class EndView():

    def __init__(self, window, message):
        
        self.window = window
        self.message = message

    def draw(self):

        endFont = pygame.font.Font('freesansbold.ttf', 50)

        gameSurface = endFont.render('Game', True, WHITE)
        gameRect = gameSurface.get_rect()
        gameRect.midtop = (WINDOW_WIDTH / 2, 10)

        overSurface = endFont.render('Over', True, WHITE)
        overRect = overSurface.get_rect()
        overRect.midtop = (WINDOW_WIDTH / 2, gameRect.height + 10 + 25)

        self.window.blit(gameSurface, gameRect)
        self.window.blit(overSurface, overRect)
        
        self.message()