import pygame
import random
from constants import *


class Snake():

    UP = 'up'
    DOWN = 'down'
    LEFT = 'left'
    RIGHT = 'right'
    HEAD = 0

    def __init__(self, window, oApple):

        self.window = window
        self.oApple = oApple
        
        self.x = random.randint(5, CELLWIDTH - 6)
        self.y = random.randint(5, CELLHEIGHT - 6)
        self.direction = self.RIGHT
        self.snakeCoordinates = [{'x': self.x, 'y': self.y},{'x': self.x - 1, 'y': self.y}, {'x': self.x - 2, 'y': self.y}]
        
    def update(self):

        if self.snakeCoordinates[self.HEAD]['x'] == self.oApple.x and self.snakeCoordinates[self.HEAD]['y'] == self.oApple.y:
            self.oApple.setNewLocation()
        else:
            del self.snakeCoordinates[-1] 
        if self.direction == self.UP:
            newHead = {'x': self.snakeCoordinates[self.HEAD]['x'],'y': self.snakeCoordinates[self.HEAD]['y'] - 1}
        elif self.direction == self.DOWN:
            newHead = {'x': self.snakeCoordinates[self.HEAD]['x'], 'y': self.snakeCoordinates[self.HEAD]['y'] + 1}
        elif self.direction == self.LEFT:
            newHead = {'x': self.snakeCoordinates[self.HEAD]['x'] - 1, 'y': self.snakeCoordinates[self.HEAD]['y']}
        elif self.direction == self.RIGHT:
            newHead = {'x': self.snakeCoordinates[self.HEAD]['x'] + 1, 'y': self.snakeCoordinates[self.HEAD]['y']}
        self.snakeCoordinates.insert(0, newHead)

    def draw(self, window):

        for coord in self.snakeCoordinates:

            x = coord['x'] * CELLSIZE
            y = coord['y'] * CELLSIZE

            wormSegmentRect = pygame.Rect(x, y, CELLSIZE, CELLSIZE)
            pygame.draw.rect(self.window, DARKGREEN, wormSegmentRect)
            
            wormInnerSegmentRect = pygame.Rect(x + 4, y + 4, CELLSIZE - 8, CELLSIZE - 8)
            pygame.draw.rect(self.window, GREEN, wormInnerSegmentRect)