import sys, pygame
from constants import *
from Model.model import Model
from Views.start_view import StartView
from Views.game_view import GameView
from Views.end_view import EndView


BACKGROUND_COLOR = BLACK

# Handles user input events
class Controller():
    
    def __init__(self, window):

        self.window = window
        self.font = pygame.font.Font('freesansbold.ttf', 14)
        self.message = self.pressToPlayMessage

        # Model
        self.oModel = Model()

        # Views
        self.oStartView = StartView(self.window, self.message)
        self.oGameView = GameView(self.window, self.font, self.oModel)
        self.oEndView = EndView(self.window, self.message)

        # To control the current view
        self.oViewArray = [self.oStartView, self.oGameView, self.oEndView]
        self.current_view = 0

        # Default Start View / object state
        self.oView = self.oViewArray[self.current_view]

    def change_view(self):
        self.current_view = 1 if self.oView == self.oStartView else 0 if self.oView == self.oEndView else 2
        self.oView = self.oViewArray[self.current_view]      

    def handleEvent(self, event):

        if event.key == pygame.K_ESCAPE:
            pygame.quit()
            sys.exit()

        if self.oView == self.oStartView or self.oView == self.oEndView:
            self.change_view()

        if self.oView == self.oGameView:
            self.oView.change_direction(event)

    def pressToPlayMessage(self):

        messageSurface = self.font.render('Press a key to play', True, WHITE)
        messageRect = messageSurface.get_rect()
        messageRect.topleft = (WINDOW_WIDTH - 200, WINDOW_HEIGHT - 30)
        self.window.blit(messageSurface, messageRect)

    def draw(self):

            self.current_view = self.oView.draw()

            if self.current_view == 2 and self.oView == self.oGameView:
                self.change_view()
                self.oView.draw()