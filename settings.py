import pygame as pg

BGCOLOR = (88, 88, 68)
WIDTH = 1024
HEIGHT = 768
TITLE = "Best game ever!"
TILESIZE = 32
FPS= 30

#colors
WHITE = (255,255,255)
WHITE = (0, 255, 0)
RED = (255, 0 ,0)
BLACK = (0, 0 ,0)

# player settings
PLAYER_SPEED = 30
PLAYER_ACC = 2
PLAYER_GRAV = 4
PLAYER_FRIC = -0.12
PLAYER_HIT_RECT = pg.Rect(0,0, TILESIZE-5, TILESIZE-5)
PLAYER_JUMP = 50

# mob settings
MOB_HIT_RECT = pg.Rect(0,0, TILESIZE-5, TILESIZE-5)