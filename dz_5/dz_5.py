from os import system
system('CLS')
from random import randint
from random import choice

# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

text = input('Введите текст\n').split()

result = ''
for i in text :
    if 'а' in i or 'б' in i or 'в' in i : result += ''
    else : result += i + ' '

print (result)

# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

all_candy = int(input('Введите количество конфет: '))
max_candies_per_turn = int(input('Введите Максимальное количество конфет за ход - '))
mode = int(input('\nВыберите с кем играть.\nИгрок --- 0\tБот --- 1\tИнтелектуальный бот --- 2\n'))

candy_1_player = 0
candy_2_player = 0

move = randint(0, 1) # Определяем ход

while all_candy > 0 :
    if all_candy <= max_candies_per_turn :
        if move == 1 :
            print(f'Побеждает игрок номер 1.\nИгроку номер 1 для победы потребовалось - {candy_1_player + all_candy} конфет')
        else :
            if mode == 0 :
                print(f'Побеждает игрок номер 2.\nИгроку номер 2 для победы потребовалось - {candy_2_player + all_candy} конфет')
            elif mode == 1 :
                print(f'Побеждает компьютер.\nКомпьютеру потребовалось - {candy_2_player + all_candy} конфет')
            else :
                print(f'Побеждает Интелект.\nИнтелекту потребовалось всего - {candy_2_player + all_candy} конфет')
        all_candy = 0    

    elif move == 1 : # 1 игрок
        get_candy = int(input('\nХодит 1 игрок. Сколько конфет вы возьмете? ')) # берет конфеты
        while get_candy > max_candies_per_turn :
            get_candy = int(input(f'\nМаксимум {max_candies_per_turn} за ход!\nСколько конфет вы возьмете на этот раз? '))
        candy_1_player += get_candy
        all_candy -= get_candy
        print(f'Всего осталось - {all_candy}')
        move = 0

    else :
        if mode == 0 : # 2 игрок
            get_candy = int(input('\nХодит 2 игрок. Сколько конфет вы возьмете? ')) # берет конфеты
            while get_candy > max_candies_per_turn :
                get_candy = int(input(f'\nМаксимум {max_candies_per_turn} за ход!\nСколько конфет вы возьмете на этот раз? '))
            candy_2_player += get_candy
            all_candy -= get_candy
            print(f'Всего осталось - {all_candy}')
            move = 1

        elif mode == 1 : # Bot
            get_candy = randint(1, max_candies_per_turn)
            candy_2_player += get_candy
            all_candy -= get_candy
            print(f'\nХодит компьютер. Компьютер берёт - {get_candy}\nВсего осталось - {all_candy}')
            move = 1

        else : # Интелект
            for k in range(max_candies_per_turn + 1, all_candy, max_candies_per_turn + 1) :
                for i in range(1, max_candies_per_turn + 1) :
                    if all_candy - i == k :
                        get_candy = i
                        break
            candy_2_player += get_candy
            all_candy -= get_candy
            print(f'\nХодит Интелект. Интелект берёт - {get_candy}\nВсего осталось - {all_candy}')
            move = 1
                    

    
# Создайте программу для игры в ""Крестики-нолики"".

def check_win (field, letter = 0) :
    win = 0
    x_o = ''
    if letter == 1 : x_o = 'O'
    else : x_o = 'X'
    if ((field[0] == x_o and field[5] == x_o and field[10] == x_o) or 
        (field[12] == x_o and field[17] == x_o and field[22] == x_o) or 
        (field[24] == x_o and field[29] == x_o and field[34] == x_o) or 
        (field[0] == x_o and field[12] == x_o and field[24] == x_o) or 
        (field[5] == x_o and field[17] == x_o and field[29] == x_o) or 
        (field[10] == x_o and field[22] == x_o and field[34] == x_o) or 
        (field[0] == x_o and field[17] == x_o and field[34] == x_o) or 
        (field[10] == x_o and field[17] == x_o and field[24] == x_o)) :
        win = 1
    return win

def step_on_field(field, move) :
    re_field = ''
    if move == 1 : char = 'X'
    else : char = 'O'
    step = input(f'\nВаши {char}. Выберете место куда поставить - ')
    for i in range(len(field)) :
        if field[i] == step : 
            re_field += char
        else : re_field += field[i]
    field = re_field
    return field

field = '1    2    3\n4    5    6\n7    8    9'
print (field)
move = choice([-1, 1]) # Определяем ход
g = 9

while g >= 0 :
    if check_win(field) == 1 : 
        print ('Игрок 1 победил!')
        break
    elif check_win(field, 1) == 1 : 
        print ('Игрок 2 победил!')
        break
    elif g == 0 : print ('Ничья')
    else :
        field = step_on_field(field, move)
        print(field)
        move = -move
    g -= 1


# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

text = input('Введите последовательность: ')
comp_text = ''
count = 1

for i in range(len(text) - 1) : # не захватывает последний элемент если он другой
    if text[i + 1] == text[i] :
        count += 1
    else : 
        if not count == 1 : comp_text += str(count) + text[i]
        else : comp_text += text[i]
        count = 1
    

print (f'Сжатые данные - {comp_text}')

# rep_text = ''

# for j in range(0, len(comp_text) - 1, 2) :
#     rep_text += comp_text[j + 1] * int(comp_text[j])

# print(f'Восстановленые данные - {rep_text}')