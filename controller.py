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

        # Default Start View
        self.oView = self.oStartView

    def handleEvent(self, event):

        if event.key == pygame.K_ESCAPE:
            pygame.quit()
            sys.exit()

        if self.oView == self.oStartView:
            self.oView = self.oGameView

        if self.oView == self.oGameView:
            self.oView.handleKeys(event)

        if self.oView == self.oEndView:
            self.oView = self.oStartView

    # def pressToPlayMessage():


        
    def draw(self):

        self.window.fill(BACKGROUND)

        if not self.oView.draw():
            self.oView = self.oEndView