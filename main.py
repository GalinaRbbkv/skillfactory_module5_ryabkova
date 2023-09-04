board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(board, "-поле до начала игры")
all_steps_x = []
all_steps_zero = []
vin = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 2, 1], [3, 1, 2],
       [4, 5, 6], [4, 6, 5], [5, 4, 6], [5, 6, 4], [6, 4, 5], [6, 5, 4],
       [7, 8, 9], [7, 9, 8], [8, 7, 9], [8, 9, 7], [9, 7, 8], [9, 8, 7],
       [1, 4, 7], [1, 7, 4], [4, 1, 7], [4, 7, 1], [7, 1, 4], [7, 4, 1],
       [2, 5, 8], [2, 8, 5], [5, 2, 8], [5, 8, 2], [8, 5, 2], [8, 2, 5],
       [3, 6, 9], [3, 9, 6], [6, 3, 9], [6, 9, 3], [9, 6, 3], [9, 3, 6]]
def step_x():
    x = int(input("игрок- Х, сделай ход "))
    all_steps_x.append(x)
    if x not in list(board):
        print("неверный ход- выбери от 1 до 9")
        step_x()
        if x in list(all_steps_x) or x in list(all_steps_zero):
            print("ячейка занята - выбери другую")
            step_x()
    index_to_replace = x - 1
    new_value = "X"
    board[index_to_replace] = new_value
    print(board)

def step_z():
    zero = int(input("игрок- O, сделай ход "))
    all_steps_zero.append(zero)
    if zero not in list(board):
        print("неверный ход- выбери от 1 до 9")
        step_z()
        if zero not in list(all_steps_x) or zero not in list(all_steps_zero):
            print("ячейка занята - выбери другую")
            step_z()
    index_to_replace = zero - 1
    new_value = "O"
    board[index_to_replace] = new_value
    print(board)
print("все ходы игрока Х - ", all_steps_x, "и все ходы игрока О - ", all_steps_zero)

step_x()
while True:
    if all_steps_x in vin:
        print("победил игрок Х")
        break
    else:
        step_z()
        if all_steps_zero in vin:
            print("победил игрок O")
            break
        else:
            step_x()
    print(all_steps_x, all_steps_zero)
    print(*board)
#  не могу остановить игру при ничьей
#  работает только пока правильно вставлять цифры и не повторяться

#215386 - победа Х
#123568 - победа O
#314256879 - ничья
