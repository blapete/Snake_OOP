import sys, pygame
from constants import *
from snake import Snake
from food import Food


class GameView():

    def __init__(self, window, font, oModel):

        self.window = window
        self.font = font
        self.oModel = oModel

        self.oFood = Food()
        self.oSnake = Snake(self.window, self.oFood)
        
        self.STATE = 1

    def checkGameOver(self):
        if (self.oSnake.snakeCoordinates[self.oSnake.HEAD]['x'] == -1 or 
            self.oSnake.snakeCoordinates[self.oSnake.HEAD]['x'] == CELLWIDTH or 
            self.oSnake.snakeCoordinates[self.oSnake.HEAD]['y'] == -1 or 
            self.oSnake.snakeCoordinates[self.oSnake.HEAD]['y'] == CELLHEIGHT):
            return "Reset Game"

        for snakeBody in self.oSnake.snakeCoordinates[1:]:
            if snakeBody['x'] == self.oSnake.snakeCoordinates[self.oSnake.HEAD]['x'] and snakeBody['y'] == self.oSnake.snakeCoordinates[self.oSnake.HEAD]['y']:
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

        '''
        Draw game window, snake, apple
        '''

        self.oSnake.update()

        # Draw game window
        for x in range(0, WINDOW_WIDTH, CELLSIZE):  # draw vertical lines
            pygame.draw.line(self.window, DARKGRAY, (x, 0), (x, WINDOW_HEIGHT))

        for y in range(0, WINDOW_HEIGHT, CELLSIZE):  # draw horizontal lines
            pygame.draw.line(self.window, DARKGRAY, (0, y), (WINDOW_WIDTH, y))

        # Draw Snake
        self.oSnake.draw(self.window)

        # Draw Food
        x = self.oSnake.oFood.x * CELLSIZE
        y = self.oSnake.oFood.y * CELLSIZE
        foodRect = pygame.Rect(x, y, CELLSIZE, CELLSIZE)
        pygame.draw.rect(self.window, RED, foodRect)

        z = len(self.oSnake.snakeCoordinates) - 3
        self.oModel.draw(self.window, self.font, z)

        gameStatus = self.checkGameOver()

        if gameStatus == "Reset Game":
            del self.oSnake
            self.oSnake = Snake(self.window, self.oFood)
            self.STATE = 2
            return False
        else:
            return True