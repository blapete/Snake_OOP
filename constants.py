WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
CELLSIZE = 20

assert WINDOW_WIDTH % CELLSIZE == 0, "Window width must be a multiple of cell size."
assert WINDOW_HEIGHT % CELLSIZE == 0, "Window height must be a multiple of cell size."

CELLWIDTH = int(WINDOW_WIDTH / CELLSIZE)
CELLHEIGHT = int(WINDOW_HEIGHT / CELLSIZE)

BLACK = (0,   0,   0)
DARKGRAY = (40,  40,  40)
RED = (255,   0,   0)
DARKGREEN = (0, 155,   0)
GREEN = (0, 255,   0)
WHITE = (255, 255, 255)

BACKGROUND = BLACK