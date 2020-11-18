import string

desk_array = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

print("---------")
for j in range(0, 3):
    print(f"| {' '.join(' ' * 3)} |")
print("---------")


def next_move(gameboard, player):
    check = True
    while check:
        user_x, user_y = input("Enter the coordinates:").split()

        if user_x not in string.digits or user_y not in string.digits:
            print("You should enter numbers!")
            continue

        x = 3 - int(user_y)
        y = int(user_x) - 1

        if int(user_x) not in range(1, 4) or int(user_y) not in range(1, 4):
            print("Coordinates should be from 1 to 3!")
            continue
        elif gameboard[x][y] != " ":
            print("This cell is occupied! Coose another one!")
            continue
        else:
            if player:
                gameboard[x][y] = "X"
            else:
                gameboard[x][y] = "O"
            print("---------")
            for i in range(3):
                print(f"| {' '.join(gameboard[i][0:3])} |")
            print("---------")
            check = False

    return gameboard


def result(gameboard):
    x_win = False
    o_win = False
    x_num = gameboard.count("X")
    o_num = gameboard.count("O")
    empty_num = gameboard.count(" ")
    for i in range(0, 3):
        cur_X = gameboard[i].count("X")
        x_num += cur_X
        cur_O = gameboard[i].count("O")
        o_num += cur_O
        cur_empty = gameboard[i].count(" ")
        empty_num += cur_empty
        if gameboard[0][i] == gameboard[1][i] and gameboard[0][i] == gameboard[2][i] and gameboard[0][i] != " ":
            if gameboard[0][i] == "X":
                x_win = True
            else:
                o_win = True
        elif gameboard[i][0] == gameboard[i][1] and gameboard[i][0] == gameboard[i][2] and gameboard[i][0] != " ":
            if gameboard[i][0] == "X":
                x_win = True
            else:
                o_win = True
        elif gameboard[0][2] == gameboard[1][1] and gameboard[0][2] == gameboard[2][0] and gameboard[1][1] != " " or gameboard[0][0] == gameboard[1][1] and gameboard[0][0] == gameboard[2][2] and gameboard[1][1] != " ":
            if gameboard[1][1] == "X":
                x_win = True
            else:
                o_win = True

    if empty_num == 0 and not x_win and not o_win:
        status = "Draw"
    elif x_win is True and o_win is not True:
        status = "X wins"
    elif o_win is True and x_win is not True:
        status = "O wins"
    else:
        status = "continue"
    return status


def game():
    game_continue = True
    cur_player = True
    while game_continue:
        next_move(desk_array, cur_player)
        cur_status = result(desk_array)
        if cur_status != "continue":
            print(cur_status)
            game_continue = False
        else:
            cur_player = not cur_player


game()

