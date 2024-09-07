# pip install pygame
try:
    import pygame as pg
except:
    from sys import executable
    from subprocess import check_call
    check_call([executable, '-m', 'pip', 'install', 'pygame'])
    import pygame as pg

# import all images in PGfuncs.py
from PGfuncs import *
from classes import * 
from loads.settings import * 

def SuperTicTacToe():
    pg.init()

    screen = pg.display.set_mode((1024, 1024))
    screen.fill((255, 255, 255))
    screen.blit(FieldImg, (0, 0))
    screen.blit(RestartImg, (0, 0))

    num_of_moves = 0
    field = Field()
    user_move = False

    move_coords = tuple()

    is_game = True
    while is_game:

        for event in pg.event.get():
            if event.type == pg.QUIT:
                is_game = False
            
            elif (event.type == pg.MOUSEBUTTONDOWN) and pg.mouse.get_pressed()[0]:
                x, y = pg.mouse.get_pos()

                # restart game
                if (158 <= x <= 865) and (117 <= y <= 228):
                    field, num_of_moves, screen = RestartGame()
                
                # user move
                result = UserMove((x, y), num_of_moves, screen, field, move_coords)
                num_of_moves = result[0]
                user_move = result[1]
                move_coords = result[2]
        
        # bot move 
        if user_move:
            pass

        pg.display.flip()

SuperTicTacToe()
# 168 312
# 232 312

# 143 287
# 368 287 
#400