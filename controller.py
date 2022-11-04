import sys, pygame
from constants import *
from model import Model
from start_view import StartView
from game_view import GameView
from end_view import EndView


class Controller():
    
    def __init__(self, window, font):
        
        self.window = window
        self.font = font

        # Model
        self.oScore = Model()

        # Views
        self.oStartView = StartView(self.window, self.font)
        self.oGameView = GameView(self.window, self.font, self.oScore)
        self.oEndView = EndView(self.window, self.font)

        # State
        self.STATE = 0

    def handleEvent(self, event):

        if event.key == pygame.K_ESCAPE:
            pygame.quit()
            sys.exit()

        if self.STATE == 0:
            self.STATE += 1

        if self.STATE == 1:
            self.oGameView.handleKeys(event)

        if self.STATE == 2:
            self.oGameView.STATE = 1
            self.STATE -=2

        
    def draw(self):

        if self.STATE == 0:
            self.oStartView.draw()

        if self.STATE == 1:
            self.oGameView.draw()
            self.STATE = self.oGameView.STATE

        if self.STATE == 2:
            self.oEndView.draw()