# pip install pygame
try:
    import pygame as pg
except:
    import sys
    import subprocess
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pygame'])
    import pygame as pg

from images import *

def SuperTicTacToe():
    pg.init()

    screen = pg.display.set_mode((900, 900))
    screen.fill((255, 255, 255))

    screen.blit(RestartImg, (0, 0))

    num_of_moves = 0

    is_game = True
    while is_game:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                is_game = False

            elif (event.type == pg.MOUSEBUTTONDOWN) and (pg.mouse.get_pressed(num_buttons=3)[0]):
                        x, y = pg.mouse.get_pos()

                        # restart the game
                        if (158 <= x <= 866) and (55 <= y <= 167):
                            print(1)
                        

        pg.display.flip()

