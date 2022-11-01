
import sys
import pygame
from constants import *
from snake import Snake
from apple import *


class GameView():

    def __init__(self, window, clock, oScore, font):
        self.window = window
        self.clock = clock
        self.oApple = Apple()
        self.oSnake = Snake(self.window, self.oApple)
        self.oScore = oScore
        self.font = font

    def checkGameOver(self):
        if (self.oSnake.wormCoords[self.oSnake.HEAD]['x'] == -1 or self.oSnake.wormCoords[self.oSnake.HEAD]['x'] == CELLWIDTH or self.oSnake.wormCoords[self.oSnake.HEAD]['y'] == -1 or self.oSnake.wormCoords[self.oSnake.HEAD]['y'] == CELLHEIGHT):
            return "Reset Game"

        for wormBody in self.oSnake.wormCoords[1:]:
            if wormBody['x'] == self.oSnake.wormCoords[self.oSnake.HEAD]['x'] and wormBody['y'] == self.oSnake.wormCoords[self.oSnake.HEAD]['y']:
                return "Reset Game"

    def handleKeys(self, event):
        if (event.key == pygame.K_LEFT or event.key == pygame.K_a) and self.oSnake.direction != self.oSnake.RIGHT:
            self.oSnake.direction = self.oSnake.LEFT
        elif (event.key == pygame.K_RIGHT or event.key == pygame.K_d) and self.oSnake.direction != self.oSnake.LEFT:
            self.oSnake.direction = self.oSnake.RIGHT
        elif (event.key == pygame.K_UP or event.key == pygame.K_w) and self.oSnake.direction != self.oSnake.DOWN:
            self.oSnake.direction = self.oSnake.UP
        elif (event.key == pygame.K_DOWN or event.key == pygame.K_s) and self.oSnake.direction != self.oSnake.UP:
            self.oSnake.direction = self.oSnake.DOWN
        elif event.key == pygame.K_ESCAPE:
            pygame.quit()
            sys.exit()

    def draw(self):
            self.window.fill(BG_COLOR)

            for x in range(0, WINDOW_WIDTH, CELLSIZE):  # draw vertical lines
                pygame.draw.line(self.window, DARKGRAY, (x, 0), (x, WINDOW_HEIGHT))

            for y in range(0, WINDOW_HEIGHT, CELLSIZE):  # draw horizontal lines
                pygame.draw.line(self.window, DARKGRAY, (0, y), (WINDOW_WIDTH, y))

            self.oSnake.draw(self.window)

            x = self.oSnake.oApple.x * CELLSIZE
            y = self.oSnake.oApple.y * CELLSIZE
            self.oSnake.oApple.draw(self.window, x, y)


            z = len(self.oSnake.wormCoords) - 3
            self.oScore.draw(self.window, self.font, z)

            pygame.display.update()
            self.clock.tick(FRAMES_PER_SECOND)