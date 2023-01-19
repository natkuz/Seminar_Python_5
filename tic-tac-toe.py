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
        cell = int(input(f'Игрок {player}, какую ячейку выбираете? '))
        if 1 > cell or cell > 10 or isinstance(playing_field[cell - 1], str):
            while 1 > cell or cell > 10 or isinstance(playing_field[cell - 1], str):
                print('Либо такой ячейки нет, либо она занята, попробуйте еще раз: ')
                cell = int(input(f'Игрок {player}, какую ячейку выбираете? '))
        playing_field[cell - 1] = '0'
        print_field(playing_field)
        num -= 1
        if (playing_field[0] == '0' and playing_field[1] == '0' and playing_field[2] == '0') \
                or (playing_field[3] == '0' and playing_field[4] == '0' and playing_field[5] == '0') \
                or (playing_field[6] == '0' and playing_field[7] == '0' and playing_field[8] == '0') \
                or (playing_field[0] == '0' and playing_field[3] == '0' and playing_field[6] == '0') \
                or (playing_field[1] == '0' and playing_field[4] == '0' and playing_field[7] == '0') \
                or (playing_field[2] == '0' and playing_field[5] == '0' and playing_field[8] == '0') \
                or (playing_field[0] == '0' and playing_field[4] == '0' and playing_field[8] == '0') \
                or (playing_field[2] == '0' and playing_field[4] == '0' and playing_field[6] == '0'):
            print(f'Выиграл игрок {player}')
            break
        else:
            player = 1

print('Игра окончена')
