
# 1
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




pygame.init()
clock = pygame.time.Clock()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Wormy')
BASICFONT = pygame.font.Font('freesansbold.ttf', 18)

oGameView = GameView()
oEndView = EndView()
oStartView = StartView()
oScore = Model()
oController = Controller()
oEndView = EndView()
oApple = Apple()
oSnake = Snake()
 

# 6
# while True:

#     # 7 - Check for and handle events
#     for event in pygame.event.get():
#         # Clicked the close button? Quit pygame and end program 
#         if event.type == pygame.QUIT:           
#             pygame.quit()  
#             sys.exit()

#     # 8 - Do any "per frame" actions
    
#     # 9 - Clear the window
#     window.fill(BLACK)
    
#     # 10 - Draw all window elements

#     # 11 - Update the window
#     pygame.display.update()

#     # 12 - Slow things down a bit
#     clock.tick(FRAMES_PER_SECOND)  # make pygame wait



# class Game():

#     def __init__(self):
#         self.snake = Snake()
#         pass

#     def draw(self):

#         screen.fill(BG_COLOR)
#         oGameView.drawGrid(screen)
#         self.snake.drawWorm(screen)

#         x = oApple.x * CELLSIZE
#         y = oApple.y * CELLSIZE
#         oApple.draw(screen, x, y)

#         z = len(self.snake.wormCoords) - 3
#         oScore.drawScore(screen, BASICFONT, z)
        
#         pygame.display.update()
#         clock.tick(FRAMES_PER_SECOND)

#     def resetGame(self):
#         del self.snake
#         self.snake = Snake()
#         oApple = Apple()
#         return True

#     def isGameOver(self):
#         if (self.snake.wormCoords[self.snake.HEAD]['x'] == -1 or self.snake.wormCoords[self.snake.HEAD]['x'] == CELLWIDTH or self.snake.wormCoords[self.snake.HEAD]['y'] == -1 or self.snake.wormCoords[self.snake.HEAD]['y'] == CELLHEIGHT):
#             return self.resetGame()

#         for wormBody in self.snake.wormCoords[1:]:
#             if wormBody['x'] == self.snake.wormCoords[self.snake.HEAD]['x'] and wormBody['y'] == self.snake.wormCoords[self.snake.HEAD]['y']:
#                 return self.resetGame()

#     def run(self):


#         while True:
#             oStartView.showStartScreen(screen, oController, clock, BASICFONT)
           
#             while True:
#                 for event in pygame.event.get():
#                     if event.type == pygame.QUIT:
#                         pygame.quit()
#                         sys.exit()
#                     elif event.type == pygame.KEYDOWN:
#                         oController.handleKeyEvents(event, self.snake)

#                 self.snake.update(oApple)

#                 self.draw()
                
#                 if self.isGameOver():
#                     break

            
#             oEndView.showGameOver(screen, oController, event, BASICFONT)


# game = Game()
# game.run()
# pygame.quit()
# sys.exit()



oController = Controller(window, clock, BASICFONT)



while True:
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            oController.handleKeyEvents(event)


    oController.draw()


    # pygame.display.update()


    # clock.tick(FRAMES_PER_SECOND)