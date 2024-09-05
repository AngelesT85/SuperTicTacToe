from pygame.image import load

def Load(img):
    return load(f"images/{img}.png")


FieldImg = Load("Field")
TicImg = Load("Tic")