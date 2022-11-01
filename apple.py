

import pygame
import random
from constants import *


class Apple():

  def __init__(self):
    print('---------------------------------------------------------------------------------setting new location 1')
    self.setNewLocation()

  def setNewLocation(self):
    print('---------------------------------------------------------------------------------setting new location 2')
    self.x = random.randint(0, CELLWIDTH - 1)
    self.y = random.randint(0, CELLHEIGHT - 1)

  def draw(self, window, x, y):
    appleRect = pygame.Rect(x, y, CELLSIZE, CELLSIZE)
    pygame.draw.rect(window, RED, appleRect)