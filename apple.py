

import pygame
import random
from Constants import *


class Apple():

  def __init__(self):
    self.setNewLocation()

  def setNewLocation(self):
    self.x = random.randint(0, CELLWIDTH - 1)
    self.y = random.randint(0, CELLHEIGHT - 1)

  def draw(self, window, x, y):
    appleRect = pygame.Rect(x, y, CELLSIZE, CELLSIZE)
    pygame.draw.rect(window, RED, appleRect)