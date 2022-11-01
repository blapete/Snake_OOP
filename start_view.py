

import sys
import pygame
from constants import *


class StartView():

    def __init__(self, window, font, clock):
        self.window = window
        self.font = font
        self.clock = clock


    def draw(self, clock):
        titleFont = pygame.font.Font('freesansbold.ttf', 50)
        titleSurf1 = titleFont.render('Snake game', True, WHITE)
        degrees1 = 0


        while True:

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    return False
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
            self.window.fill(BG_COLOR)

            theRect = titleSurf1.get_rect()
            theRect.center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
            self.window.blit(titleSurf1, theRect)

            pressKeySurf = self.font.render('Press a key to play.', True, DARKGRAY)
            pressKeyRect = pressKeySurf.get_rect()
            pressKeyRect.topleft = (WINDOW_WIDTH - 200, WINDOW_HEIGHT - 30)
            self.window.blit(pressKeySurf, pressKeyRect)
            pygame.display.update()
            self.clock.tick(FRAMES_PER_SECOND)
