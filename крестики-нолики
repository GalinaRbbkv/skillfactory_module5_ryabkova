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
    x = int(input("игрок- Х, сделай ход - "))
    if x not in list(board):
        print(x,"-это не подходит- выбери число из", board)
        step_x()
    index_to_replace_x = x - 1
    new_value_x = "X"
    board[index_to_replace_x] = new_value_x
    all_steps_x.append(x)
    print(board)
    print("все ходы игрока Х - ", all_steps_x, "и все ходы игрока О - ", all_steps_zero)

def step_z():
    zero = int(input("игрок- O, сделай ход - "))
    if zero not in list(board):
        print(zero,"-это не подходит- выбери число из", board)
        step_z()
    index_to_replace_z = zero - 1
    new_value_z = "O"
    board[index_to_replace_z] = new_value_z
    all_steps_zero.append(zero)
    print(board)
    print("все ходы игрока Х - ", all_steps_x, "и все ходы игрока О - ", all_steps_zero)

step_x()
while True:
    if all_steps_x in vin:
        print("КОНЕЦ ИГРЫ:  победил игрок Х")
        break
    else:
        step_z()
        if all_steps_zero in vin:
            print("КОНЕЦ ИГРЫ: победил игрок O")
            break
        else:
            step_x()
    if len(all_steps_x) + (len(all_steps_x)) >= 9:
        print("Игра окончена - НИЧЬЯ!!!")
        break


#  работает только пока правильно вставлять цифры и не повторяться
# не срабатвает если выигрышная комбиная не точна, напрмер не 789 а 1789
# список всех ходов сохрянает ошибочные ходы

#215386 - победа Х
#123568 - победа O
#314256879 - ничья
