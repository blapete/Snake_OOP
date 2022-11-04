import pygame
from constants import *


class EndView():

    def __init__(self, window, font, message):
        
        self.window = window
        self.font = font
        self.message = message


    def draw(self):

        font = pygame.font.Font('freesansbold.ttf', 50)
        game = font.render('Game', True, WHITE)
        over = font.render('Over', True, WHITE)
        gameRect = game.get_rect()
        overRect = over.get_rect()
        gameRect.midtop = (WINDOW_WIDTH / 2, 10)
        overRect.midtop = (WINDOW_WIDTH / 2, gameRect.height + 10 + 25)
        self.window.blit(game, gameRect)
        self.window.blit(over, overRect)
        
        self.message()