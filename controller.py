import sys, pygame
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
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            else:
                self.STATE = 1

        if self.STATE == 2:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            else:
                self.STATE = 0
        
    def draw(self):

        if self.STATE == 0:
            self.oStartView.draw()

        if self.STATE == 1:
            self.STATE = self.oGameView.draw()

        if self.STATE == 2:
            self.oEndView.draw()