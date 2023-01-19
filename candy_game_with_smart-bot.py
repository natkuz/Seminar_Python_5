# Создайте программу для игры с конфетами человек против бота, наделенного "интеллектом".
# Условие задачи: На столе лежит заданное количество конфет.
# Играют два игрока, человек и бот, делая ход по очереди.
# Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
import math
import random

candies = int(input('Укажите количество конфет на столе: '))
first_move = random.randint(1, 2)
print(f'Первый ход достается игроку {first_move}')
player = first_move
candies_number = 0
while candies > 0:
    if player == 1:
        candies_number = int(input(f'Игрок {player}, сколько возьмете конфет? '))
        if candies_number > 28 or candies_number < 1:
            while candies_number > 28 or candies_number < 1:
                print('Не меньше 1 и не больше 28, попробуйте еще раз: ')
                candies_number = int(input(f'Игрок {player}, сколько возьмете конфет? '))
        candies = candies - candies_number
        if candies < 0:
            while candies < 0:
                candies = candies + candies_number
                print(f'На столе уже нет столько конфет. Осталось {candies}. Попробуйте еще раз: ')
                candies_number = int(input(f'Игрок {player}, сколько возьмете конфет? '))
                if candies_number < 1:
                    while candies_number < 1:
                        print('Не меньше 1, попробуйте еще раз: ')
                        candies_number = int(input(f'Игрок {player}, сколько возьмете конфет? '))
                candies = candies - candies_number
                if candies > 0:
                    player = 2
        elif candies > 0:
            player = 2
        print(f'Осталось {candies} конфет')
    else:
        candies_number = candies - (math.trunc(candies / 29) * 29)
        if candies_number == 0:
            candies_number = random.randint(1, 29)
        print(f'Игрок {player} берет {candies_number} конфет')
        candies = candies - candies_number
        print(f'Осталось {candies} конфет')
        if candies > 0:
            player = 1
print(f'Игрок {player} выиграл и забирает все конфеты!')


