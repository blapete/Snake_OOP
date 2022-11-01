

import pygame
import random
from constants import *


class Snake():

    UP = 'up'
    DOWN = 'down'
    LEFT = 'left'
    RIGHT = 'right'
    HEAD = 0

    def __init__(self, oApple, window):
        self.x = random.randint(5, CELLWIDTH - 6)
        self.y = random.randint(5, CELLHEIGHT - 6)
        self.direction = self.RIGHT
        self.wormCoords = [{'x': self.x, 'y': self.y},{'x': self.x - 1, 'y': self.y}, {'x': self.x - 2, 'y': self.y}]
        self.oApple = oApple
        self.window = window

    def update(self):
        
        # print('1')
        if self.wormCoords[self.HEAD]['x'] == self.oApple.x and self.wormCoords[self.HEAD]['y'] == self.oApple.y:
            self.oApple.setNewLocation()
            print('2')
        else:
            # print('3')
            del self.wormCoords[-1] 

        if self.direction == self.UP:
            newHead = {'x': self.wormCoords[self.HEAD]['x'],'y': self.wormCoords[self.HEAD]['y'] - 1}

        elif self.direction == self.DOWN:
            newHead = {'x': self.wormCoords[self.HEAD]['x'], 'y': self.wormCoords[self.HEAD]['y'] + 1}

        elif self.direction == self.LEFT:
            newHead = {'x': self.wormCoords[self.HEAD]['x'] - 1, 'y': self.wormCoords[self.HEAD]['y']}

        elif self.direction == self.RIGHT:
            newHead = {'x': self.wormCoords[self.HEAD]['x'] + 1, 'y': self.wormCoords[self.HEAD]['y']}

        self.wormCoords.insert(0, newHead)


    def draw(self, window):
        for coord in self.wormCoords:
            x = coord['x'] * CELLSIZE
            y = coord['y'] * CELLSIZE
            wormSegmentRect = pygame.Rect(x, y, CELLSIZE, CELLSIZE)
            pygame.draw.rect(self.window, DARKGREEN, wormSegmentRect)
            wormInnerSegmentRect = pygame.Rect(x + 4, y + 4, CELLSIZE - 8, CELLSIZE - 8)
            pygame.draw.rect(self.window, GREEN, wormInnerSegmentRect)