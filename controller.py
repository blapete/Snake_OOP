

import sys
import pygame
from constants import *
from snake import Snake
from apple import Apple
from game_view import *
from start_view import *
from end_view import *
from model import *







class Controller():

    def __init__(self, window, clock, font):
        self.window = window
        self.clock = clock
        self.font = font
        self.status = 0

        self.oScore = Model()
        self.oApple = Apple()
        self.oSnake = Snake(self.oApple, self.window)

        self.oStartView = StartView(self.window, self.font, self.clock)
        self.oGameView = GameView(self.window, self.clock, self.oSnake, self.oApple, self.oScore, font)
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
        # print(keyUpEvents)
                  
        if len(keyUpEvents) == 0:
            return None

        # if keyUpEvents[0].key == pygame.K_ESCAPE:
            # pygame.quit()
            # sys.exit()

        if len(keyUpEvents) != 0:
            return True

        return keyUpEvents[0].key


    def draw(self):

        if self.status == 0:
            print("status:", self.status)
            self.oStartView.draw(self.window)
        
        self.status = 1

        if self.status == 1:
            print("status:", self.status)
            self.window.fill(BG_COLOR)
            print('here')
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    elif event.type == pygame.KEYDOWN:
                        self.oGameView.handleKeyEvents(event)

                self.oSnake.update()

                self.oGameView.draw()

                q = self.oGameView.isGameOver()
                if q == "Reset Game":
                    print(q)
                    print('done')
                    del self.oSnake
                    self.oSnake = Snake(self.oApple, self.window)
                    self.oApple = Apple()
                    break

        self.status = 2

        if self.status == 2:
            print("status:", self.status)
            self.oEndView.draw()
            self.drawPressKeyMsg()
            pygame.display.update()
            pygame.time.wait(500)
            self.checkForKeyPress()

            while True:
                if self.checkForKeyPress():
                    print('1')
                    pygame.event.get()
                    print('2')
                    self.status = 0
                    break

        # print('3')
        # print('done')
        # pygame.quit()
        # sys.exit()