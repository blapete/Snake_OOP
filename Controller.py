

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




class Controller():

    def __init__(self):
        pass

    def drawPressKeyMsg(self, screen, font):
        pressKeySurf = font.render('Press a key to play.', True, DARKGRAY)
        pressKeyRect = pressKeySurf.get_rect()
        pressKeyRect.topleft = (WINDOW_WIDTH - 200, WINDOW_HEIGHT - 30)
        screen.blit(pressKeySurf, pressKeyRect)

    def handleKeyEvents(self, event, snake):
        if (event.key == pygame.K_LEFT or event.key == pygame.K_a) and snake.direction != snake.RIGHT:
            snake.direction = snake.LEFT
        elif (event.key == pygame.K_RIGHT or event.key == pygame.K_d) and snake.direction != snake.LEFT:
            snake.direction = snake.RIGHT
        elif (event.key == pygame.K_UP or event.key == pygame.K_w) and snake.direction != snake.DOWN:
            snake.direction = snake.UP
        elif (event.key == pygame.K_DOWN or event.key == pygame.K_s) and snake.direction != snake.UP:
            snake.direction = snake.DOWN
        elif event.key == pygame.K_ESCAPE:
            pygame.quit()

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

        return keyUpEvents[0].key