# Создайте программу для игры в 'Крестики-нолики'
import random

playing_field = [
    1, 2, 3,
    4, 5, 6,
    7, 8, 9
]


def print_field(field: list):
    print(f'{field[0]}\t|\t{field[1]}\t|\t{field[2]}')
    print('------------------')
    print(f'{field[3]}\t|\t{field[4]}\t|\t{field[5]}')
    print('------------------')
    print(f'{field[6]}\t|\t{field[7]}\t|\t{field[8]}')


print_field(playing_field)

operation = {
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y,
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
}

first_move = random.randint(1, 2)
print(f'Первый ход достается игроку {first_move}')
player = first_move
num = 9

while num > 0:
    if player == 1:
        cell = int(input(f'Игрок {player}, какую ячейку выбираете? '))
        if 1 > cell or cell > 10 or isinstance(playing_field[cell - 1], str):
            while 1 > cell or cell > 10 or isinstance(playing_field[cell - 1], str):
                print('Либо такой ячейки нет, либо она занята, попробуйте еще раз: ')
                cell = int(input(f'Игрок {player}, какую ячейку выбираете? '))
        playing_field[cell - 1] = 'X'
        print_field(playing_field)
        num -= 1
        if (playing_field[0] == 'X' and playing_field[1] == 'X' and playing_field[2] == 'X') \
                or (playing_field[3] == 'X' and playing_field[4] == 'X' and playing_field[5] == 'X') \
                or (playing_field[6] == 'X' and playing_field[7] == 'X' and playing_field[8] == 'X') \
                or (playing_field[0] == 'X' and playing_field[3] == 'X' and playing_field[6] == 'X') \
                or (playing_field[1] == 'X' and playing_field[4] == 'X' and playing_field[7] == 'X') \
                or (playing_field[2] == 'X' and playing_field[5] == 'X' and playing_field[8] == 'X') \
                or (playing_field[0] == 'X' and playing_field[4] == 'X' and playing_field[8] == 'X') \
                or (playing_field[2] == 'X' and playing_field[4] == 'X' and playing_field[6] == 'X'):
            print(f'Выиграл игрок {player}')
            break

        else:
            player = 2
    else:
        cell = 5
        if playing_field[0] == 'O' and playing_field[3] == 'O' and isinstance(playing_field[6], int) \
                or playing_field[7] == 'O' and playing_field[8] == 'O' and isinstance(playing_field[6], int) \
                or playing_field[2] == 'O' and playing_field[4] == 'O' and isinstance(playing_field[6], int):
            cell = 7
        elif playing_field[3] == 'O' and playing_field[6] == 'O' and isinstance(playing_field[0], int) \
                or playing_field[1] == 'O' and playing_field[2] == 'O' and isinstance(playing_field[0], int) \
                or playing_field[4] == 'O' and playing_field[8] == 'O' and isinstance(playing_field[0], int):
            cell = 1
        elif playing_field[0] == 'O' and playing_field[1] == 'O' and isinstance(playing_field[2], int) \
                or playing_field[6] == 'O' and playing_field[4] == 'O' and isinstance(playing_field[2], int) \
                or playing_field[5] == 'O' and playing_field[8] == 'O' and isinstance(playing_field[2], int):
            cell = 3
        elif playing_field[6] == 'O' and playing_field[7] == 'O' and isinstance(playing_field[8], int) \
                or playing_field[2] == 'O' and playing_field[5] == 'O' and isinstance(playing_field[8], int) \
                or playing_field[0] == 'O' and playing_field[4] == 'O' and isinstance(playing_field[8], int):
            cell = 9
        elif playing_field[0] == 'O' and playing_field[2] == 'O' and isinstance(playing_field[1], int) \
                or playing_field[4] == 'O' and playing_field[7] == 'O' and isinstance(playing_field[1], int):
            cell = 2
        elif playing_field[0] == 'O' and playing_field[6] == 'O' and isinstance(playing_field[3], int) \
                or playing_field[4] == 'O' and playing_field[5] == 'O' and isinstance(playing_field[3], int):
            cell = 4
        elif playing_field[6] == 'O' and playing_field[8] == 'O' and isinstance(playing_field[7], int) \
                or playing_field[1] == 'O' and playing_field[4] == 'O' and isinstance(playing_field[7], int):
            cell = 8
        elif playing_field[2] == 'O' and playing_field[8] == 'O' and isinstance(playing_field[5], int) \
                or playing_field[3] == 'O' and playing_field[4] == 'O' and isinstance(playing_field[5], int):
            cell = 6
        elif playing_field[3] == 'X' and playing_field[6] == 'X' and isinstance(playing_field[0], int) \
                or playing_field[1] == 'X' and playing_field[2] == 'X' and isinstance(playing_field[0], int) \
                or playing_field[4] == 'X' and playing_field[8] == 'X' and isinstance(playing_field[0], int):
            cell = 1
        elif playing_field[0] == 'X' and playing_field[3] == 'X' and isinstance(playing_field[6], int) \
                or playing_field[7] == 'X' and playing_field[8] == 'X' and isinstance(playing_field[6], int) \
                or playing_field[2] == 'X' and playing_field[4] == 'X' and isinstance(playing_field[6], int):
            cell = 7
        elif playing_field[0] == 'X' and playing_field[1] == 'X' and isinstance(playing_field[2], int) \
                or playing_field[6] == 'X' and playing_field[4] == 'X' and isinstance(playing_field[2], int) \
                or playing_field[5] == 'X' and playing_field[8] == 'X' and isinstance(playing_field[2], int):
            cell = 3
        elif playing_field[6] == 'X' and playing_field[7] == 'X' and isinstance(playing_field[8], int) \
                or playing_field[2] == 'X' and playing_field[5] == 'X' and isinstance(playing_field[8], int) \
                or playing_field[0] == 'X' and playing_field[4] == 'X' and isinstance(playing_field[8], int):
            cell = 9
        elif playing_field[0] == 'X' and playing_field[2] == 'X' and isinstance(playing_field[1], int) \
                or playing_field[4] == 'X' and playing_field[7] == 'X' and isinstance(playing_field[1], int):
            cell = 2
        elif playing_field[0] == 'X' and playing_field[6] == 'X' and isinstance(playing_field[3], int) \
                or playing_field[4] == 'X' and playing_field[5] == 'X' and isinstance(playing_field[3], int):
            cell = 4
        elif playing_field[6] == 'X' and playing_field[8] == 'X' and isinstance(playing_field[7], int) \
                or playing_field[1] == 'X' and playing_field[4] == 'X' and isinstance(playing_field[7], int):
            cell = 8
        elif playing_field[2] == 'X' and playing_field[8] == 'X' and isinstance(playing_field[5], int) \
                or playing_field[3] == 'X' and playing_field[4] == 'X' and isinstance(playing_field[5], int):
            cell = 6
        else:
            cell_list = [1, 2, 3, 4, 6, 7, 8, 9]
            if isinstance(playing_field[cell - 1], str):
                while isinstance(playing_field[cell - 1], str):
                    cell = random.choice(cell_list)

        print(f'Игрок {player} выбирает ячейку {cell}')
        playing_field[cell - 1] = 'O'
        print_field(playing_field)
        num -= 1
        if (playing_field[0] == 'O' and playing_field[1] == 'O' and playing_field[2] == 'O') \
                or (playing_field[3] == 'O' and playing_field[4] == 'O' and playing_field[5] == 'O') \
                or (playing_field[6] == 'O' and playing_field[7] == 'O' and playing_field[8] == 'O') \
                or (playing_field[0] == 'O' and playing_field[3] == 'O' and playing_field[6] == 'O') \
                or (playing_field[1] == 'O' and playing_field[4] == 'O' and playing_field[7] == 'O') \
                or (playing_field[2] == 'O' and playing_field[5] == 'O' and playing_field[8] == 'O') \
                or (playing_field[0] == 'O' and playing_field[4] == 'O' and playing_field[8] == 'O') \
                or (playing_field[2] == 'O' and playing_field[4] == 'O' and playing_field[6] == 'O'):
            print(f'Выиграл игрок {player}')
            break
        else:
            player = 1

print('Игра окончена')
