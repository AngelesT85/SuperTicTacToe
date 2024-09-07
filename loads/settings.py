import json
from loads.images import *

with open("settings.json", "r", encoding="utf-8") as settings:
    settings = json.load(settings)

    UserFigure = settings["User figure"]
    UserFirstMove = settings["User first move"]
    if UserFigure == "o":
        PGfigures = (TacToeImg, TicImg)
        PGBigFigures = (BigTacToeImg, BigTicImg)
        figures = ("o", "x")
    else:
        PGfigures = (TicImg, TacToeImg)
        PGBigFigures = (BigTicImg, BigTacToeImg)
        figures = ("x", "o")

    if not UserFirstMove:
        PGfigures = PGfigures[::-1]
        PGBigFigures = PGBigFigures[::-1]
        figures = figures[::-1]


    