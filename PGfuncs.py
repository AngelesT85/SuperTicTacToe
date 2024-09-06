from loads.images import *

def UserMove(coords, num_of_moves, figures, screen):
    x, y = coords
    for BigX in range(3):
        for BigY in range(3):
            if (143 + 256*BigX <= x <= 367 + 257*BigX) and (287 + 256*BigY <= y <= 511 + 257*BigY):
                
                # coords of left up angle of little square where user clicked
                AngleLeft_x, AngleUp_y = 168 + 256*BigX, 312 + 256*BigY


                for LitX in range(3):
                    for LitY in range(3):
                        minX = AngleLeft_x + 64*LitX
                        maxX = (AngleLeft_x + 48) + 64*LitX

                        minY = AngleUp_y + 64*LitY
                        maxY = (AngleUp_y + 48) + 64*LitY
                        if (minX <= x <= maxX) and (minY <= y <= maxY):
                            screen.blit(figures[num_of_moves % 2], (minX, minY))
                            num_of_moves += 1
                            return num_of_moves
    return num_of_moves