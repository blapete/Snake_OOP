
# 1
import sys
import pygame
from Constants import *
from snake import Snake
from apple import Apple
from GameView import *
from StartView import *
from EndView import *
from Model import *
from Controller import *




pygame.init()
clock = pygame.time.Clock()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Wormy')
BASICFONT = pygame.font.Font('freesansbold.ttf', 18)

oGameView = GameView()
oEndView = EndView()
oStartView = StartView()
oScore = Model()
oController = Controller()
oEndView = EndView()
oApple = Apple()
oSnake = Snake()
 



oController = Controller(window, clock, BASICFONT)



while True:
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            oController.handleKeyEvents(event)


    oController.draw()