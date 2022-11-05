import random
from constants import *


class Food():

  def __init__(self):

    self.x = None
    self.y = None

    self.generateNewFoodObject()

  def generateNewFoodObject(self):

    self.x = random.randint(0, CELLWIDTH - 1)
    self.y = random.randint(0, CELLHEIGHT - 1)