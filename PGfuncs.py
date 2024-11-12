from loads.images import *
from loads.settings import PGfigures, figures, PGBigFigures
from classes import Field
import pygame as pg

def RestartGame():
    field = Field()
    num_of_moves = 0
    screen = pg.display.set_mode((1024, 1024))
    screen.fill((255, 255, 255))
    screen.blit(FieldImg, (0, 0))
    screen.blit(RestartImg, (0, 0))
    return field, num_of_moves, screen

def Move(coords, num_of_moves, screen, field, move_coords):
    x, y = coords
    for BigX in range(3):
        for BigY in range(3):

            # is clicked in the square in which enemy send you
            if move_coords:
                if (BigX, BigY) != move_coords:
                    continue
            
            # find big square in which clicked
            if (143 + 256*BigX <= x <= 367 + 257*BigX) and (287 + 256*BigY <= y <= 511 + 257*BigY):
                
                # coords of left up angle of little square where user clicked
                AngleLeft_x, AngleUp_y = 168 + 256*BigX, 312 + 256*BigY

                for LitX in range(3):
                    for LitY in range(3):
                        minX = AngleLeft_x + 64*LitX
                        maxX = (AngleLeft_x + 48) + 64*LitX

                        minY = AngleUp_y + 64*LitY
                        maxY = (AngleUp_y + 48) + 64*LitY
                        
                        # find mini square in which clicked
                        if (minX <= x <= maxX) and (minY <= y <= maxY):
                            result = field.attack((BigX, BigY), (LitX, LitY), figures[num_of_moves % 2])

                            if not result[0]:
                                move_coords = tuple()

                            print(result)

                            if result[0]:
                                PGfigure = PGfigures[num_of_moves % 2]
                                field.PrintFieldConsole()
                                field.PrintBigField()
                                screen.blit(PGfigure, (minX, minY))
                            
                                if move_coords:
                                    screen.blit(StrokeWhiteImg, (144 + 256*BigX, 288 + 256*BigY))

                                if result[1]:
                                    screen.blit(PGBigFigures[num_of_moves % 2], (144 + 256*BigX, 288 + 256*BigY))

                                    if result[2]:

                                        return "WIN"
                                
                                                                # if cell where we send enemy is full
                                if field.BigField[LitX][LitY] != "·":
                                    move_coords = tuple()
                                    screen.blit(BigBlueStrokeImg, (0, 0))
                                    num_of_moves += 1
                                    return num_of_moves, True, move_coords
                                
                                else:
                                    move_coords = (LitX, LitY)
                                    
                                screen.blit(BigWhiteStrokeImg, (0, 0))
                                screen.blit(StrokeBlueImg, (144 + 256*LitX, 288 + 256*LitY))
                                num_of_moves += 1

                                return num_of_moves, True, move_coords

                        
    return num_of_moves, False, move_coords

def BotMove():
    pass