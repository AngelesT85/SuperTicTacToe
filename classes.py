class Field:
    
    def __init__(self, space_symbol="·") -> None:
        self.field = [[[[space_symbol for _ in range(3)] for _ in range(3)] for _ in range(3)] for _ in range(3)]
        self.BigField = [[space_symbol for _ in range(3)] for _ in range(3)]
    
    def PrintFieldConsole(self):
        field = self.field
        for BigLine in range(3):
            for BigSquare in range(3):
                for LittleLine in range(3):
                    print(" ", end="")
                    print(*field[BigLine][LittleLine][BigSquare], sep=" | ", end="")
                    print("  ┃ " if LittleLine != 2 else "\n", end="")
                for LittleLine in range(3):
                    if BigSquare != 2:
                    # print(" ", end="")
                        print(*["---", "---", "---"], sep="|", end="")
                        print(" ┃ " if LittleLine != 2 else "\n", end="")
            print("━" * 39 if BigLine != 2 else "")
    
    def attack(self, coords_big_field, coords_mini_field, who_attack):
        big_x, big_y = coords_big_field
        mini_x, mini_y = coords_mini_field
        self.field[big_y][big_x][mini_x][mini_y] = who_attack

    def TestMiniFields(self):
        for BigY in range(3):
            for BigX in range(3):
                mini_field = self.field[BigY][BigX]

                for i in range(3):
                    if mini_field[i][0] == mini_field[i][1] == mini_field[i][2] and mini_field[i][0] != "·" and self.BigField[BigY][BigX] != mini_field[i][0]:
                        self.BigField[BigY][BigX] = mini_field[i][0]
                        return None
                    elif mini_field[0][i] == mini_field[1][i] == mini_field[2][i] and mini_field[0][i] != "·" and self.BigField[BigY][BigX] != mini_field[0][i]:
                        self.BigField[BigY][BigX] = mini_field[0][i]
                        return None
                if mini_field[0][0] == mini_field[1][1] == mini_field[2][2] and mini_field[0][0] != "·" and self.BigField[BigY][BigX] != mini_field[0][0]:
                    self.BigField[BigY][BigX] = mini_field[0][0]
                    return None
                if mini_field[2][0] == mini_field[1][1] == mini_field[0][2] and mini_field[2][0] != "·" and self.BigField[BigY][BigX] != mini_field[2][0]:
                    self.BigField[BigY][BigX] = mini_field[2][0]
                    return None
                             
    def TestEndGame(self):
        for i in range(3):
            if self.BigField[i][0] == self.BigField[i][1] == self.BigField[i][2] and self.BigField[i][0] != "·":
                return True
            elif self.BigField[0][i] == self.BigField[1][i] == self.BigField[2][i] and self.BigField[0][i] != "·":
                return True
        if self.BigField[0][0] == self.BigField[1][1] == self.BigField[2][2] and self.BigField[0][0] != "·":
            return True
        if self.BigField[2][0] == self.BigField[1][1] == self.BigField[0][2] and self.BigField[2][0] != "·":
            return True
        return False
        

field = Field()
field.attack((0, 0), (1, 0), "X")
field.attack((0, 0), (1, 1), "X")
field.attack((0, 0), (1, 2), "X")
field.TestMiniFields()
print(field.TestEndGame())
field.PrintFieldConsole() 
print(field.BigField)
# Example of print field in terminal
#  · | · | ·  ┃  · | · | ·  ┃  · | · | · 
# ---|---|--- ┃ ---|---|--- ┃ ---|---|---
#  · | · | ·  ┃  · | · | ·  ┃  · | · | ·
# ---|---|--- ┃ ---|---|--- ┃ ---|---|---
#  · | · | ·  ┃  · | · | ·  ┃  · | · | ·
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  · | · | ·  ┃  · | · | ·  ┃  · | · | · 
# ---|---|--- ┃ ---|---|--- ┃ ---|---|---
#  · | · | ·  ┃  · | · | ·  ┃  · | o | x
# ---|---|--- ┃ ---|---|--- ┃ ---|---|---
#  · | · | ·  ┃  · | · | ·  ┃  · | · | ·
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  · | · | ·  ┃  · | · | ·  ┃  · | · | · 
# ---|---|--- ┃ ---|---|--- ┃ ---|---|---
#  · | · | ·  ┃  · | · | ·  ┃  · | · | ·
# ---|---|--- ┃ ---|---|--- ┃ ---|---|---
#  · | · | ·  ┃  · | · | ·  ┃  · | · | ·

