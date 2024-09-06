from pygame.image import load

def Load(img):
    return load(f"images/{img}.png")

FieldImg = Load("Field")
TicImg = Load("Tic")
TacToeImg = Load("TacToe")
StrokeBlueImg = Load("StrokeBlue")
StrokeWhiteImg = Load("StrokeWhite")