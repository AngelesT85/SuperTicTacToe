from random import randint, choice

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
        print(mini_x, mini_y)
        if self.field[big_y][big_x][mini_y][mini_x] == "·":
            self.field[big_y][big_x][mini_y][mini_x] = who_attack
            return True, self.TestMiniFields(coords=(big_y, big_x)), self.TestEndGame()
        else:
            return False, False, False

    def TestMiniFields(self, testing_all=False, coords=None):
        if testing_all:
            for BigY in range(3):
                for BigX in range(3):
                    mini_field = self.field[BigY][BigX]

                    for i in range(3):
                        if mini_field[i][0] == mini_field[i][1] == mini_field[i][2] and mini_field[i][0] != "·" and self.BigField[BigY][BigX] != mini_field[i][0]:
                            self.BigField[BigY][BigX] = mini_field[i][0]
                            return True
                        elif mini_field[0][i] == mini_field[1][i] == mini_field[2][i] and mini_field[0][i] != "·" and self.BigField[BigY][BigX] != mini_field[0][i]:
                            self.BigField[BigY][BigX] = mini_field[0][i]
                            return True
                    if mini_field[0][0] == mini_field[1][1] == mini_field[2][2] and mini_field[0][0] != "·" and self.BigField[BigY][BigX] != mini_field[0][0]:
                        self.BigField[BigY][BigX] = mini_field[0][0]
                        return True
                    if mini_field[2][0] == mini_field[1][1] == mini_field[0][2] and mini_field[2][0] != "·" and self.BigField[BigY][BigX] != mini_field[2][0]:
                        self.BigField[BigY][BigX] = mini_field[2][0]
                        return True
            return False
        else:
            mini_field = self.field[coords[1]][coords[0]]
            for i in range(3):
                if mini_field[i][0] == mini_field[i][1] == mini_field[i][2] and mini_field[i][0] != "·" and self.BigField[BigY][BigX] != mini_field[i][0]:
                    self.BigField[BigY][BigX] = mini_field[i][0]
                    return True
                elif mini_field[0][i] == mini_field[1][i] == mini_field[2][i] and mini_field[0][i] != "·" and self.BigField[BigY][BigX] != mini_field[0][i]:
                    self.BigField[BigY][BigX] = mini_field[0][i]
                    return True
            if mini_field[0][0] == mini_field[1][1] == mini_field[2][2] and mini_field[0][0] != "·" and self.BigField[BigY][BigX] != mini_field[0][0]:
                self.BigField[BigY][BigX] = mini_field[0][0]
                return True
            if mini_field[2][0] == mini_field[1][1] == mini_field[0][2] and mini_field[2][0] != "·" and self.BigField[BigY][BigX] != mini_field[2][0]:
                self.BigField[BigY][BigX] = mini_field[2][0]
                return True
            return False
                             
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
        

class AI:
    def __init__(self) -> None:
        self.tactics_field = [[None for _ in range(3)] for _ in range(3)]

    def BotChoice(self, Field, coords, player_symbol, bot_symbol):
        field = Field.field[coords[1]][coords[0]]
        field_elements = ""
        for i in field:
            for j in i:
                field_elements += j
        print(field_elements)
        num_pl = field_elements.count(player_symbol)
        print(field)
        num_b = field_elements.count(bot_symbol)
        if num_pl + num_b == 0:
            return randint(0, 2), randint(0, 2)
        
        elif num_b == 1 and num_pl == 0:
            print("---------------------")
            coords_first_bot_attack = None
            for i in range(3):
                for j in range(3):
                    if field[i][j] == bot_symbol:
                        coords_first_bot_attack = (j, i)
                        break
            
            if (coords_first_bot_attack[0] == coords_first_bot_attack[1]) and (coords_first_bot_attack[0] == 3 - coords_first_bot_attack[1] + 1):
                choice_bot = randint(1, 4)
            elif coords_first_bot_attack[0] == coords_first_bot_attack[1]:
                choice_bot = randint(1, 3)
            else:
                choice_bot = randint(1, 2)

            if choice_bot == 1:
                print(1)
                self.tactics_field[coords[1]][coords[0]] = "horizon"
                x_coords = [0, 1, 2]
                del x_coords[coords_first_bot_attack[0]]
                return choice(x_coords), coords_first_bot_attack[1]
            elif choice_bot == 2:
                print(2)
                self.tactics_field[coords[1]][coords[0]] = "vertical"
                y_coords = [0, 1, 2]
                del y_coords[coords_first_bot_attack[1]]
                return coords_first_bot_attack[0], choice(y_coords)
            elif choice_bot == 3:
                print(3)
                self.tactics_field[coords[1]][coords[0]] = "main_diagonal"
                main_coords = [0, 1, 2]
                del main_coords[coords_first_bot_attack[0]]
                pos = choice(main_coords)
                return pos, pos
            elif choice_bot == 4:
                print(4)
                self.tactics_field[coords[1]][coords[0]] = "side diagonal"
                side_diagonal = [(0, 2), (1, 1), (2, 0)]
                del side_diagonal[coords_first_bot_attack[0]]
                return side_diagonal[0], side_diagonal[1]
        elif num_b == 2 and num_pl == 0:
            return "A", "A"



field = Field()
bot = AI()
a = bot.BotChoice(field, (0, 0), "O", "X")
field.attack((0, 0), a, "X")
b = bot.BotChoice(field, (0, 0), "O", "X")
field.attack((0, 0), b, "X")
print(a, b)
field.TestMiniFields(testing_all=True)
print(field.TestEndGame())
field.PrintFieldConsole() 
print(field.BigField)
print(bot.tactics_field)
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

