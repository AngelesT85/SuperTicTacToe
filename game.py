# pip install pygame
try:
    import pygame as pg
except:
    import sys
    import subprocess
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pygame'])
    import pygame as pg

from loads.images import *

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
                for BigX in range(3):
                    for BigY in range(3):
                        if (143 + 257*BigX <= x <= 368 + 257*BigX) and (287 + 257*BigY <= y <= 512 + 257*BigY):
                            print(1)

        pg.display.flip()

SuperTicTacToe()
# 168 312
# 232 312

# 143 287
# 368 287 
#400