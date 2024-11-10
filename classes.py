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
             
    def attack(self, coords_big_field, coords_mini_field, who_attack): #атаковать куда-то кем-то
        big_x, big_y = coords_big_field
        mini_x, mini_y = coords_mini_field
        if self.field[big_y][big_x][mini_y][mini_x] == "·" and self.BigField[big_y][big_x] == "·":
            self.field[big_y][big_x][mini_y][mini_x] = who_attack
            return True, self.TestMiniFields(coords=(big_y, big_x)), self.TestEndGame()
        else:
            return False, False, False

    def TestMiniFields(self, testing_all=False, coords=None): # возвращает Тру или Фалзе в зависимости от того закончилась ли игра (для маленьких полей)
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
            mini_field = self.field[coords[0]][coords[1]]
            for i in range(3):
                if mini_field[i][0] == mini_field[i][1] == mini_field[i][2] and mini_field[i][0] != "·" and self.BigField[coords[0]][coords[1]] != mini_field[i][0]:
                    self.BigField[coords[0]][coords[1]] = mini_field[i][0]
                    return True
                elif mini_field[0][i] == mini_field[1][i] == mini_field[2][i] and mini_field[0][i] != "·" and self.BigField[coords[0]][coords[1]] != mini_field[0][i]:
                    self.BigField[coords[0]][coords[1]] = mini_field[0][i]
                    return True
            if mini_field[0][0] == mini_field[1][1] == mini_field[2][2] and mini_field[0][0] != "·" and self.BigField[coords[0]][coords[1]] != mini_field[0][0]:
                self.BigField[coords[0]][coords[1]] = mini_field[0][0]
                return True
            if mini_field[2][0] == mini_field[1][1] == mini_field[0][2] and mini_field[2][0] != "·" and self.BigField[coords[0]][coords[1]] != mini_field[2][0]:
                self.BigField[coords[0]][coords[1]] = mini_field[2][0]
                return True
            return False
                             
    def TestEndGame(self): # возвращает Тру или Фалзе в зависимости от того закончилась ли игра (для больших полей)
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

    def BotChoice(self, coords, player_symbol, bot_symbol): # возвращает col и string в мальньком поле, в котором атакует бот
        field = self.field[coords[1]][coords[0]]

        field_elements = ""
        for i in field:
            for j in i:
                field_elements += j
        num_pl = field_elements.count(player_symbol)
        num_b = field_elements.count(bot_symbol)

        if (num_pl + num_b == 0) or (num_pl == 1 and num_b == 0):
            while True:
                coords = randint(0, 2), randint(0, 2)
                if field[coords[0]][coords[1]] == "·":
                    return coords[1], coords[0]
        
        elif num_b == 1 and num_pl == 0:
            end_attack = self.SecondAttack(field, bot_symbol)
            return end_attack
    
        elif num_b == num_pl == 1:
            coords_bot_attack = None
            coords_player_attack = None
            for i in range(3):
                for j in range(3):
                    if field[i][j] == bot_symbol:
                        coords_bot_attack = (j, i)
                    elif field[i][j] == player_symbol:
                        coords_player_attack = (j, i)
            
            main = coords_bot_attack[0] == coords_bot_attack[1] and coords_player_attack[0] != coords_player_attack[1]
            side = (coords_bot_attack in [(0, 2), (1, 1), (2, 0)]) and (coords_player_attack not in [(0, 2), (1, 1), (2, 0)])
            horizon = coords_bot_attack[0] != coords_player_attack[0]
            vertical = coords_bot_attack[1] != coords_player_attack[1]
            list_choices = [main, side, horizon, vertical]
            list_choices_names = ["m", "s", "h", "v"]
            choice_bot = choice([list_choices_names[i] for i in range(4) if list_choices[i]])

            if choice_bot == "m":
                while True:
                    pos = randint(0, 2)
                    if field[pos][pos] == "·":
                        return pos, pos
            elif choice_bot == "s":
                while True:
                    pos = choice([(0, 2), (1, 1), (2, 0)])
                    if field[pos[0]][pos[1]] == "·":
                        return pos[1], pos[0]
            elif choice_bot == "h":
                while True:
                    pos = randint(0, 2)
                    if field[pos][coords_bot_attack[0]] == "·":
                        return coords_bot_attack[0], pos
            elif choice_bot == "v":
                while True:
                    pos = randint(0, 2)
                    if field[coords_bot_attack[1]][pos] == "·":
                        return pos, coords_bot_attack[1]
              
        elif num_b == 2 and num_pl == 0:
            end_attack = self.ThirdAttack(field, player_symbol)
            if end_attack != None:
                return end_attack
            end_attack = self.ThirdAttack(field, bot_symbol)
            if end_attack != None:
                return end_attack
        
        else:
            end_attack = self.ThirdAttack(field, bot_symbol)
            if end_attack != None:
                return end_attack
            end_attack = self.ThirdAttack(field, player_symbol)
            if end_attack != None:
                return end_attack
            
            while True:
                coords = randint(0, 2), randint(0, 2)
                if field[coords[0]][coords[1]] == "·":
                    return coords[1], coords[0]
            
    def SecondAttack(self, field, symbol): # используется в BotChoice
        coords_first_bot_attack = None
        for i in range(3):
            for j in range(3):
                if field[i][j] == symbol:
                    coords_first_bot_attack = (j, i)
                    break
            
        if (coords_first_bot_attack[0] == coords_first_bot_attack[1]) and (coords_first_bot_attack[0] == 3 - coords_first_bot_attack[1] + 1):
            choice_bot = randint(1, 4)
        elif coords_first_bot_attack[0] == coords_first_bot_attack[1]:
            choice_bot = randint(1, 3)
        else:
            choice_bot = randint(1, 2)
            
        if choice_bot == 1:
            x_coords = [0, 1, 2]
            del x_coords[coords_first_bot_attack[0]]
            return choice(x_coords), coords_first_bot_attack[1]
        elif choice_bot == 2:
            y_coords = [0, 1, 2]
            del y_coords[coords_first_bot_attack[1]]
            return coords_first_bot_attack[0], choice(y_coords)
        elif choice_bot == 3:
            main_coords = [0, 1, 2]
            del main_coords[coords_first_bot_attack[0]]
            pos = choice(main_coords)
            return pos, pos
        elif choice_bot == 4:
            side_diagonal = [(0, 2), (1, 1), (2, 0)]
            del side_diagonal[coords_first_bot_attack[0]]
            pos = choice(side_diagonal)
            return pos[0], pos[1]
    
    def ThirdAttack(self, field, symbol): # используется в BotChoice
        for i in range(3):
            if "".join(field[i]).count(symbol) == 2:
                for j in range(3):
                    if field[i][j] == "·":
                        return j, i
            elif "".join([field[0][i], field[1][i], field[2][i]]).count(symbol) == 2:
                for j in range(3):
                    if field[j][i] == "·":
                        return i, j
        if "".join([field[0][0], field[1][1], field[2][2]]).count(symbol) == 2:
            for i in range(3):
                if field[i][i] == "·":
                    return i, i
        elif "".join([field[0][2], field[1][1], field[2][0]]).count(symbol) == 2:
            for i in [(0, 2), (1, 1), (2, 0)]:
                if field[i[0]][i[1]] == "·":
                    return i[1], i[0]
    
            


# field = Field()

# field.PrintFieldConsole()
# while True:
#     coords = [int(i) for i in input().split()]
#     field.attack((0, 0), coords, "O")
#     a = field.BotChoice((0, 0), "O", "X")
#     field.attack((0, 0), a, "X")
#     field.TestMiniFields(testing_all=True)
#     print(field.TestEndGame())
#     field.PrintFieldConsole()
#     print(field.BigField)

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

