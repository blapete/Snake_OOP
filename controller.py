

import sys
import pygame
from constants import *
from snake import Snake
from game_view import *
from start_view import *
from end_view import *
from model import *


class Controller():

    def __init__(self, window, clock, font):
        self.window = window
        self.clock = clock
        self.font = font
        self.oScore = Model()
        self.oStartView = StartView(self.window, self.font, self.clock)
        self.oGameView = GameView(self.window, self.clock, self.oScore, self.font)
        self.oEndView = EndView(self.window)
        self.oView = self.oStartView
    
    def drawPressKeyMsg(self):
        pressKeySurf = self.font.render('Press a key to play.', True, DARKGRAY)
        pressKeyRect = pressKeySurf.get_rect()
        pressKeyRect.topleft = (WINDOW_WIDTH - 200, WINDOW_HEIGHT - 30)
        self.window.blit(pressKeySurf, pressKeyRect)

    def checkForKeyPress(self):
        if len(pygame.event.get(pygame.QUIT)) > 0:
            pygame.quit()
            sys.exit()
        keyUpEvents = pygame.event.get(pygame.KEYUP)
        if len(keyUpEvents) == 0:
            return None
        if keyUpEvents[0].key == pygame.K_ESCAPE:
            pygame.quit()
            sys.exit()
        if len(keyUpEvents) != 0:
            return True
        return keyUpEvents[0].key


    def draw(self):
        self.oStartView.draw(self.window)
        while True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self.oGameView.handleKeys(event)

            self.window.fill(BG_COLOR)

            self.oGameView.oSnake.update()

            self.oGameView.draw()

            q = self.oGameView.checkGameOver()
            
            if q == "Reset Game":
                del self.oGameView.oSnake
                self.oGameView.oSnake = Snake(self.window, self.oGameView.oApple)
                break
        self.oEndView.draw()
        self.drawPressKeyMsg()
        pygame.display.update()
        pygame.time.wait(500)
        self.checkForKeyPress()

        while True:
            if self.checkForKeyPress():
                print('4')
                pygame.event.get()
                print('5')
                self.status = 0
                break