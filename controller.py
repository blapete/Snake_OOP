

import sys
import pygame
from constants import *
from model import Model
from start_view import StartView
from game_view import GameView
from end_view import EndView


class Controller():
    
    def __init__(self, window, clock, font):
        
        self.window = window
        self.clock = clock
        self.font = font

        # Model
        self.oScore = Model()

        # Views
        self.oStartView = StartView(self.window, self.font)
        self.oGameView = GameView(self.window, self.font, self.clock, self.oScore)
        self.oEndView = EndView(self.window, self.font)

        # State
        self.STATE = 0

    def handleEvent(self, event):

        if self.STATE == 0:
            if event.type == pygame.KEYDOWN:
                keyUpEvents = pygame.event.get(pygame.KEYUP)
                print(keyUpEvents)
                if keyUpEvents[0].key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                self.STATE = 1

        if self.STATE == 1:
            pass

        if self.STATE == 2:
            # pass
            print('here')
            # if len(pygame.event.get(pygame.QUIT)) > 0:
            #     pygame.quit()
            #     sys.exit()
            print('here 2')
            keyUpEvents = pygame.event.get(pygame.KEYUP)
            print(keyUpEvents)
            print('here 3')
            if len(keyUpEvents) == 0:
                return None
            print('here 4')
            print(keyUpEvents[0].key)
            print('here 5')
            if keyUpEvents[0].key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            if len(keyUpEvents) != 0:
                return 0
            return keyUpEvents[0].key

        
    def draw(self):

        if self.STATE == 0:
            self.oStartView.draw()

        if self.STATE == 1:
            self.STATE = self.oGameView.draw()
            print('here', self.STATE)

        if self.STATE == 2:
            self.oEndView.draw()