# pip install pygame
try:
    import pygame as pg
except:
    import sys
    import subprocess
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pygame'])
    import pygame as pg

def SuperTicTacToe():
    pg.init()

    screen = pg.display.set_mode((900, 900))
    screen.fill((255, 255, 255))

    num_of_moves = 0

    is_game = True
    while is_game:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                is_game = False
        
        pg.display.flip()

