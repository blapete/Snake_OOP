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
        self.oSnake = Snake(self.oFood)

    def game_over(self):

        if (self.oSnake.snakeCoordinates[self.oSnake.HEAD]['x'] == -1 or 
            self.oSnake.snakeCoordinates[self.oSnake.HEAD]['x'] == CELLWIDTH or 
            self.oSnake.snakeCoordinates[self.oSnake.HEAD]['y'] == -1 or 
            self.oSnake.snakeCoordinates[self.oSnake.HEAD]['y'] == CELLHEIGHT):
            return True

        for snakeBody in self.oSnake.snakeCoordinates[1:]:
            if snakeBody['x'] == self.oSnake.snakeCoordinates[self.oSnake.HEAD]['x'] and snakeBody['y'] == self.oSnake.snakeCoordinates[self.oSnake.HEAD]['y']:
                return True

    def change_direction(self, event):

        if (event.key == pygame.K_LEFT) and self.oSnake.direction != self.oSnake.RIGHT:
            self.oSnake.direction = self.oSnake.LEFT
        elif (event.key == pygame.K_RIGHT) and self.oSnake.direction != self.oSnake.LEFT:
            self.oSnake.direction = self.oSnake.RIGHT
        elif (event.key == pygame.K_UP) and self.oSnake.direction != self.oSnake.DOWN:
            self.oSnake.direction = self.oSnake.UP
        elif (event.key == pygame.K_DOWN) and self.oSnake.direction != self.oSnake.UP:
            self.oSnake.direction = self.oSnake.DOWN

    def draw_score(self):

        currentScore = self.oModel.getScore() # getter
        scoreSurface = self.font.render('Score: %s' % (currentScore), True, WHITE)
        scoreRect = scoreSurface.get_rect()
        scoreRect.topleft = (WINDOW_WIDTH - 120, 10)
        self.window.blit(scoreSurface, scoreRect)

    def draw_food(self):

        x = self.oSnake.oFood.x * CELLSIZE
        y = self.oSnake.oFood.y * CELLSIZE
        foodRect = pygame.Rect(x, y, CELLSIZE, CELLSIZE)
        pygame.draw.rect(self.window, RED, foodRect)

    def draw_snake(self):

        for coord in self.oSnake.snakeCoordinates:

            x = coord['x'] * CELLSIZE
            y = coord['y'] * CELLSIZE

            snakeSegmentRect = pygame.Rect(x, y, CELLSIZE, CELLSIZE)
            pygame.draw.rect(self.window, DARKGREEN, snakeSegmentRect)

            snakeInnerSegmentRect = pygame.Rect(x + 4, y + 4, CELLSIZE - 8, CELLSIZE - 8)
            pygame.draw.rect(self.window, GREEN, snakeInnerSegmentRect)

    def draw(self):

        if self.game_over():
            del self.oSnake
            self.oSnake = Snake(self.oFood)
            self.oSnake.oFood.generateNewFoodObject()
            
            return 2

        if self.oSnake.snakeCoordinates[self.oSnake.HEAD]['x'] == self.oFood.x and self.oSnake.snakeCoordinates[self.oSnake.HEAD]['y'] == self.oFood.y:
            self.oFood.generateNewFoodObject()
        else:
            del self.oSnake.snakeCoordinates[-1]

        if self.oSnake.direction == self.oSnake.UP:
            newHead = {'x': self.oSnake.snakeCoordinates[self.oSnake.HEAD]['x'],'y': self.oSnake.snakeCoordinates[self.oSnake.HEAD]['y'] - 1}
        elif self.oSnake.direction == self.oSnake.DOWN:
            newHead = {'x': self.oSnake.snakeCoordinates[self.oSnake.HEAD]['x'], 'y': self.oSnake.snakeCoordinates[self.oSnake.HEAD]['y'] + 1}
        elif self.oSnake.direction == self.oSnake.LEFT:
            newHead = {'x': self.oSnake.snakeCoordinates[self.oSnake.HEAD]['x'] - 1, 'y': self.oSnake.snakeCoordinates[self.oSnake.HEAD]['y']}
        elif self.oSnake.direction == self.oSnake.RIGHT:
            newHead = {'x': self.oSnake.snakeCoordinates[self.oSnake.HEAD]['x'] + 1, 'y': self.oSnake.snakeCoordinates[self.oSnake.HEAD]['y']}

        self.oSnake.snakeCoordinates.insert(0, newHead)

        currentScore = len(self.oSnake.snakeCoordinates) - 3
        self.oModel.setScore(currentScore) # setter

        # Draw game window
        for x in range(0, WINDOW_WIDTH, CELLSIZE):
            pygame.draw.line(self.window, DARKGRAY, (x, 0), (x, WINDOW_HEIGHT))

        for y in range(0, WINDOW_HEIGHT, CELLSIZE):
            pygame.draw.line(self.window, DARKGRAY, (0, y), (WINDOW_WIDTH, y))

        self.draw_snake()

        self.draw_food()

        self.draw_score()

        return 1