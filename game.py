# pip install pygame
try:
    import pygame as pg
except:
    import sys
    import subprocess
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pygame'])
    import pygame as pg

# import all images in PGfuncs.py
from PGfuncs import *

def SuperTicTacToe():
    pg.init()

    screen = pg.display.set_mode((1024, 1024))
    screen.fill((255, 255, 255))
    screen.blit(FieldImg, (0, 0))
    figures = (TicImg, TacToeImg)
    num_of_moves = 0

    is_game = True
    while is_game:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                is_game = False
            

            elif (event.type == pg.MOUSEBUTTONDOWN) and pg.mouse.get_pressed()[0]:
                x, y = pg.mouse.get_pos()

                num_of_moves = UserMove((x, y), num_of_moves, figures, screen)

        pg.display.flip()

SuperTicTacToe()
# 168 312
# 232 312

# 143 287
# 368 287 
#400