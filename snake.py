import pygame
import random
from constants import *


class Snake():

    UP = 'up'
    DOWN = 'down'
    LEFT = 'left'
    RIGHT = 'right'
    
    HEAD = 0

    def __init__(self, oFood):

        self.oFood = oFood

        self.x = 10
        self.y = 15
        
        self.direction = self.RIGHT
        self.snakeCoordinates = [{'x': self.x, 'y': self.y},{'x': self.x - 1, 'y': self.y}, {'x': self.x - 2, 'y': self.y}]