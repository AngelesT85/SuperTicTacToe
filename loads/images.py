from pygame.image import load

def Load(img):
    return load(f"images/{img}.png")

FieldImg = Load("Field")

TicImg = Load("Tic")
TacToeImg = Load("TacToe")
BigTicImg = Load("BigTic")
BigTacToeImg = Load("BigTacToe")

StrokeBlueImg = Load("StrokeBlue")
StrokeWhiteImg = Load("StrokeWhite")
BigBlueStrokeImg = Load("BigBlueStroke")
BigWhiteStrokeImg = Load("BigWhiteStroke")

RestartImg = Load("Restart")