def start():
    print("                   ")
    print("  Крестики-нолики  ")
    print("___________________")
    print(" Формат ввода: X Y ")
    print(" X - номер строки  ")
    print(" Y - номер столбца ")


def table():
    print()
    print("   Y| 0 | 1 | 2 | ")
    print("  X ------------- ")
    for i, row in enumerate(field):
        row_str = f"  {i} | {' | '.join(row)} | "
        print(row_str)
        print("    ------------- ")
    print()


def to_ask():
    while True:
        print("______________")
        cords = input("  Ваш ход: ").split()

        if len(cords) != 2:
            print(" Введите 2 координаты! ")
            continue

        x, y = cords

        if not (x.isdigit()) or not (y.isdigit()):
            print(" Введите координаты! ")
            continue

        x, y = int(x), int(y)

        if 0 > x or x > 2 or 0 > y or y > 2:
            print(" Данной координаты не существует! ")
            continue

        if field[x][y] != " ":
            print(" Клетка занята! ")
            continue

        return x, y


def win():
    win_cord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for cord in win_cord:
        symbols = []
        for c in cord:
            symbols.append(field[c[0]][c[1]])
        if symbols == ["X", "X", "X"]:
            print("Победитель X!")
            return True
        if symbols == ["0", "0", "0"]:
            print("Победитель 0!")
            return True
    return False


start()
field = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]
count = 0
while True:
    count += 1
    table()
    if count % 2 == 1:
        print(" Ход крестика!")
    else:
        print(" Ход нолика!")

    x, y = to_ask()

    if count % 2 == 1:
        field[x][y] = "X"
    else:
        field[x][y] = "0"

    if check_win():
        break

    if count == 9:
        print(" Победила дружба!")
        break