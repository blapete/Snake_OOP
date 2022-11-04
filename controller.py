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
        self.message = self.pressToPlayMessage

        # Model
        self.oModel = Model()

        # Views
        self.oStartView = StartView(self.window, self.message)
        self.oGameView = GameView(self.window, self.font, self.oModel)
        self.oEndView = EndView(self.window, self.message)

        # Default Start View - "controller object's state"
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

    def pressToPlayMessage(self):

        messageSurface = self.font.render('Press a key..', True, WHITE)
        messageRect = messageSurface.get_rect()
        messageRect.topleft = (WINDOW_WIDTH - 200, WINDOW_HEIGHT - 30)
        self.window.blit(messageSurface, messageRect)

    def draw(self):

        self.window.fill(BACKGROUND)

        if not self.oView.draw():
            self.oView = self.oEndView