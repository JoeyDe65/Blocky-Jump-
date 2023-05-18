#File created by Joey De Marco

TITLE = "BLOCKY JUMP!"
WIDTH = 480
HEIGHT = 600
FPS = 60
FONT_NAME = 'arial'
HS_FILE = "highscore.txt"

# Player properties
PLAYER_ACC = 2
PLAYER_FRICTION = -0.3
PLAYER_JUMP = 20
PLAYER_GRAV = 0.8

# Starting platforms
PLATFORM_LIST = [(0, HEIGHT - 40, WIDTH, 40, "bouncy"),
                 (WIDTH / 2 - 50, HEIGHT * 3 / 4, 100, 20, "bouncy"),
                 (125, HEIGHT - 350, 100, 20, "bouncy"),
                 (350, 200, 100, 20, "bouncy"),
                 (175, 100, 50, 20, "bouncy")]

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255,50,50)
GREEN = (70, 100, 100)
BLUE = (50,50,255)
YELLOW = (255, 120, 240)
LIGHTBLUE = (20, 50, 200)
BGCOLOR = LIGHTBLUE