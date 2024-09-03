class Field:
    
    def __init__(self, space_symbol="·") -> None:
        self.field = [[[[space_symbol for _ in range(3)] for _ in range(3)] for _ in range(3)] for _ in range(3)]
    
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

field = Field()
field.PrintFieldConsole() 

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

