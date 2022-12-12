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

all_candy = 202
candy_1_player = 0
candy_2_player = 0
candy_com = 0
mode = int(input('Введите с кем играть. 0 - игрок, 1 - бот, 2 - интелектуальный бот\n'))
move = randint(0, 1) # Определяем ход
print(f'Всего конфет - {all_candy}')
while all_candy > 0 :
    if move == 1 :
        # 1 игрок
        if all_candy <= 28 :
            print ('Побеждает игрок номер 1')
            candy_1_player += all_candy
            print(f'1 игроку потребовалось - {candy_1_player} конфет')
            all_candy = 0
        else :
            print('Ходит 1 игрок.')
            get_candy = int(input('Сколько конфет вы возьмете? ')) # берет конфеты
            while get_candy > 28 :
                print('Максимум 28 конфет за ход')
                get_candy = int(input('Сколько конфет вы возьмете? '))
            candy_1_player += get_candy
            all_candy -= get_candy
            print(f'\nВсего осталось - {all_candy}')
            move = 0

    else :
        if mode == 0 :
            # 2 игрок
            if all_candy <= 28 :
                print ('Побеждает игрок номер 2')
                candy_2_player += all_candy
                print(f'2 игроку потребовалось - {candy_2_player} конфет')
                all_candy = 0
            else :
                print('Ходит 2 игрок.')
                get_candy = int(input('Сколько конфет вы возьмете? ')) # берет конфеты
                while get_candy > 28 :
                    print('Максимум 28 конфет за ход')
                    get_candy = int(input('Сколько конфет вы возьмете? '))
                candy_2_player += get_candy
                all_candy -= get_candy
                print(f'\nВсего осталось - {all_candy}')
                move = 1

        elif mode == 1 :
            # Bot
            if all_candy <= 28 :
                print ('Побеждает компьютер.')
                candy_com += all_candy
                print(f'Компьютеру потребовалось - {candy_com} конфет')
                all_candy = 0
            else :
                print('Ходит компьютер.')
                get_candy = randint(1, 28)
                print(f'Компьютер берёт - {get_candy} конфет')
                candy_com += get_candy
                all_candy -= get_candy
                print(f'\nВсего осталось - {all_candy}')
                move = 1

        elif mode == 2 :
            # Интелект
            if all_candy <= 28 :
                print ('Побеждает ИИ.')
                candy_com += all_candy
                print(f'ИИ потребовалось - {candy_com} конфет')
                all_candy = 0
            else :
                print('Ходит ИИ.')
                for k in range(29, all_candy, 29) :
                    for i in range(1, 29) :
                        if all_candy - i == k :
                            get_candy = i
                            break
                print(f'ИИ берёт - {get_candy} конфет')
                candy_com += get_candy
                all_candy -= get_candy
                print(f'\nВсего осталось - {all_candy}')
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
text_for_comp = list()
comp_text = ''

for i in text :
    if i in text_for_comp :
        continue
    else : 
        text_for_comp.append(i)
        comp_text += str(text.count(i)) + i

print (f'Сжатые данные - {comp_text}')

rep_text = ''

for j in range(0, len(comp_text) - 1, 2) :
    rep_text += comp_text[j + 1] * int(comp_text[j])

print(f'Восстановленые данные - {rep_text}')