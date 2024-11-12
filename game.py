# pip install pygame
try:
    import pygame as pg
except:
    from sys import executable
    from subprocess import check_call
    check_call([executable, '-m', 'pip', 'install', 'pygame'])
    import pygame as pg

from random import randint
from time import sleep

# import all images in PGfuncs.py
from PGfuncs import *
from classes import Field
from loads.settings import * 


def SuperTicTacToe(UserFirstMove):
    pg.init()
    
    screen = pg.display.set_mode((1024, 1024))
    screen.fill((255, 255, 255))
    screen.blit(FieldImg, (0, 0))
    screen.blit(RestartImg, (0, 0))

    num_of_moves = 0
    field = Field()
    user_move = False
    Play = True
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
                    Play = True
                    move_coords = tuple()
                
                elif UserFirstMove and Play:
                    # user move
                    result = Move((x, y), num_of_moves, screen, field, move_coords)

                    if result == "WIN":
                        Play = False
                        break

                    else:
                        num_of_moves = result[0]
                        user_move = result[1]
                        move_coords = result[2]

                        if move_coords:
                            if field.BigField[move_coords[0]][move_coords[1]] != "·":
                                move_coords = tuple()

                        pg.display.flip()
                else:
                    UserFirstMove = True
                print(Play)
        
        # bot move 
        if Play and AI and user_move:
            sleep(3)
            if move_coords:
                col, string = field.BotChoice(move_coords, figures[num_of_moves % 2], figures[(num_of_moves % 2) - 1])

                BigX, BigY = 168 + 256*move_coords[0], 312 + 256*move_coords[1]
                LitX, LitY = BigX + 64*col, BigY + 64*string

                print(LitX, LitY)
                num_of_moves, _, move_coords = Move((LitX, LitY), num_of_moves, screen, field, move_coords)

            else:
                while True:
                    RandomBigX = randint(0, 2)
                    RandomBigY = randint(0, 2)
                    if field.BigField[RandomBigY][RandomBigX] == "·":
                        break
                col, string = field.BotChoice((RandomBigX, RandomBigY), figures[num_of_moves % 2], figures[(num_of_moves % 2) - 1])

                BigX, BigY = 168 + 256*RandomBigX, 312 + 256*RandomBigY
                LitX, LitY = BigX + 64*col, BigY + 64*string

                num_of_moves, _, move_coords = Move((LitX, LitY), num_of_moves, screen, field, move_coords)

            print(move_coords)
            user_move = False
            pg.display.flip()

            

        pg.display.flip()

SuperTicTacToe(UserFirstMove)
# 168 312
# 232 312

# 143 287
# 368 287 
#400