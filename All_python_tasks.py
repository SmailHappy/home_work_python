import os
from random import randint
from random import random
from math import ceil

def Run() :
    print ("Домашнее задание 1. Задача 1 - 1. Задача 2 - 2. Задача 3 - 3. Задача 4 - 4. Задача 5 - 5.")
    print ("Домашнее задание 2. Задача 6 - 6. Задача 7 - 7. Задача 8 - 8. Задача 9 - 9. Задача 10 - 10.")
    print ("Домашнее задание 3. Задача 11 - 11. Задача 12 - 12. Задача 13 - 13. Задача 14 - 14. Задача 15 - 15.")
    code = int(input ("Введите код задачи: "))
    if code == 1 :
        zadacha_1()
    elif code == 2 :
        zadacha_2()
    elif code == 3 :
        zadacha_3()
    elif code == 4 :
        zadacha_4()
    elif code == 5 :
        zadacha_5()
    elif code == 6 :
        zadacha_6()
    elif code == 7 :
        zadacha_7()
    elif code == 8 :
        zadacha_8()
    elif code == 9 :
        zadacha_9()
    elif code == 10 :
        zadacha_10()
    elif code == 11 :
        zadacha_11()
    elif code == 12 :
        zadacha_12()
    elif code == 13 :
        zadacha_13()
    elif code == 14 :
        zadacha_14()
    elif code == 15 :
        zadacha_15()
    else :
        print ("Такой задачи тут нет.")



def zadacha_1() :
    # Задача 1: Напишите программу, которая принимает на вход цифру, 
    # обозначающую день недели, и проверяет, является ли этот день выходным.
    # Пример:
    # - 6 -> да
    # - 7 -> да
    # - 1 -> нет

    os.system('CLS')

    print ("Задача 1. Принимает на вход число и проверяет является ли этот день выходным\n")
    day = int(input("Введите число: "))

    if day >= 1 and day <= 7 :
        if day == 6 or day == 7 :
            print ("Да, этот день выходной")
        else : 
            print ("Нет")
    else :
        print ("Вы ввели не день недели")

    Break()



def zadacha_2() :
    # Задача 2:
    # Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z 
    # (расшифровка этого выражения not (x[0] or x[1] or x[2] = not x[0] and not x[1] and not x[2]) для всех значений предикат.

    os.system('CLS')

    print ("Задача 2. Проверка истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z\n")
    logik = [True, False]

    for x in logik :
        for y in logik :
            for z in logik :
                result = not (x or y or z) == (not x) and (not y) and (not z)
                print(f"Если x = {x}, y = {y}, z = {z}\nУтверждение = {result}", )

    Break()



def zadacha_3() :
    # Задача 3:
    # Напишите программу, которая принимает на вход координаты точки (X и Y), 
    # причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка .
    # Пример:
    # - x=34; y=-30 -> 4
    # - x=2; y=4-> 1
    # - x=-34; y=-30 -> 3

    os.system('CLS')

    print ("Задача 3. Принимает на вход координаты точки (X и Y) и выдаёт номер четверти плоскости, в которой находится эта точка\n")
    x = int(input("Введите координаты точки по оси X: "))
    y = int(input("Введите координаты точки по оси Y: "))

    if x == 0 or y == 0 :
        print ("Попробуйте ввести другие координаты")
    else :
        if x > 0 and y > 0 :
            print ("Ваша точка находится в 1 четверти")
        if x < 0 and y > 0 :
            print ("Ваша точка находится в 2 четверти")
        if x < 0 and y < 0 :
            print ("Ваша точка находится в 3 четверти")
        if x > 0 and y < 0 :
            print ("Ваша точка находится в 4 четверти")

    Break()



def zadacha_4() :
    # Задача 4:
    # Напишите программу, которая по заданному номеру четверти, 
    # показывает диапазон возможных координат точек в этой четверти (x и y).

    os.system('CLS')

    print ("Задача 4. Принимает на вход номер четверти плоскости и показывает диапазон возможных координат точек\n")
    number = int(input("Введите номер четверти плоскости: "))

    if number == 1 :
        print ("Возможные координаты\nПо оси 'x' от 1 до +∞\nПо оси 'y' от 1 до +∞")
    elif number == 2 :
        print ("Возможные координаты\nПо оси 'x' от -1 до -∞\nПо оси 'y' от 1 до +∞")
    elif number == 3 :
        print ("Возможные координаты\nПо оси 'x' от -1 до -∞\nПо оси 'y' от -1 до -∞")
    elif number == 4 :
        print ("Возможные координаты\nПо оси 'x' от 1 до +∞\nПо оси 'y' от -1 до -∞")
    else :
        print ("Вы ввели не номер четверти")

    Break()



def zadacha_5() :
    # Задача 5:
    # Напишите программу, которая принимает на вход координаты двух точек
    #  и находит расстояние между ними в 2D пространстве.
    # Пример:
    # - A (3,6); B (2,1) -> 5,09
    # - A (7,-5); B (1,-1) -> 7,21

    os.system('CLS')

    print ("Задача 5. Принимает на координаты двух точек A и B, и находит расстояние между ними\n")
    point_a_x = int(input("Введите координаты точки A по оси X: "))
    point_a_y = int(input("Введите координаты точки A по оси Y: "))

    point_b_x = int(input("\nВведите координаты точки B по оси X: "))
    point_b_y = int(input("Введите координаты точки B по оси Y: "))

    result = (((point_b_x - point_a_x)**2) + ((point_b_y - point_a_y)**2))**(1/2)
    result = int(result * 100) / 100
    print ('Расстояние между точками = ' + str(result))

    Break()



def zadacha_6() :
    # Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
    # Пример:
    # - 6782 -> 23
    # - 0,56 -> 11

    os.system('CLS')

    print ("Задача 6. Принимает на вход вещественное число и показывает сумму его цифр\n")
    number = input("Введите число: ")
    number = number.replace("," , '')
    number = number.replace("." , '')
    sum = 0

    for i in number :
        sum += int(i)

    print (sum)

    Break()



def zadacha_7() :
    # Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
    # Пример:
    # - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

    os.system('CLS')

    print ("Задача 7. Принимает на вход число N и выдает набор произведений чисел от 1 до N\n")
    number = int(input("Введите число N: "))
    num = 1
    numb = 1

    while num < number :
        numb *= num
        print (numb, end = ", ")
        num += 1
    
    print (numb * number)

    Break()



def zadacha_8() :
    # Задайте список из n чисел последовательности $(1 + 1/n)^n$ и выведите на экран их сумму.
    # Пример:
    # - Для n = 4: {1: 2, 2: 2,25, 3: 2,37, 4: 2,44}

    os.system('CLS')

    print ("Задача 8. Задаёт список из N чисел последовательности (1 + 1/n)^n и выводит на экран их сумму\n")
    number = int(input("Введите число N: "))

    result = [round((1 + 1/i)**i, 2) for i in range(1, number + 1)]
    print (result)

    sum = 0
    for i in result :
        sum += i

    print (f"Сумма = {sum}")

    Break()



def zadacha_9() :
    # Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
    # Найдите произведение элементов на указанных позициях. 
    # Позиции хранятся в файле file.txt в одной строке одно число.

    os.system('CLS')

    print ("Задача 9. Задаёт список из N элементов и находит произведение элементов на указанных позициях в файле\n")
    number = int(input("Введите число N: "))

    list = [randint(-number, number) for i in range(number)]
    print(list)
    
    with open("home_work/file.txt", "w") as file :
        count_numbers = randint(0, number)
        print (f"\nКол-во позиций в файле = {count_numbers}")
        while count_numbers > 0 :
            file.write(str(randint(1, number)) + "\n")
            count_numbers -= 1

    with open("home_work/file.txt", "r") as file :
        result = 1
        for line in file :
            result *= list[int(line) - 1]
        print (f"Произведение на указанных позициях = {result}")

    Break()



def zadacha_10() :
    # Реализуйте алгоритм перемешивания списка.

    os.system('CLS')

    print ("Задача 10. Перемешиванние списка из N элементов\n")
    number = int(input("Введите число N: "))

    result = [i for i in range(number)]

    print(f"Изначальный список: {result}")

    for i in result :
        index = randint(1, number)
        result[index], result[i] = result[i], result[index]

    print(f"Перемешанный список: {result}")

    Break()



def zadacha_11() :
    # Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
    # Пример: - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

    os.system('CLS')

    print("Задача 11. Создаёт список из N элементов и выводит сумму нечётных элементов\n")
    n = int(input("Введите N: "))

    fill_numbers = [randint(0, 10) for i in range(n)]
    sum = 0
    print (f"Список - {fill_numbers}") 

    for i in range(1, n, 2) :
        sum += fill_numbers[i]

    # i = 1
    # while i < n :
    #     sum += fill_numbers[i]
    #     i += 2

    print (f"Сумма цифр на нечётных позициях = {sum}") 

    Break()



def zadacha_12() :
    # Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
    # Пример:
    # - [2, 3, 4, 5, 6] => [12, 15, 16];
    # - [2, 3, 5, 6] => [12, 15]

    os.system('CLS')

    print("Задача 12. Создаёт список из N элементов и найдёт произведение пар чисел списка ( пара - первый и последний элемент )\n")
    n = int(input("Введите N: "))

    fill_numbers = [randint(0, 10) for i in range(n)]
    print (f"Список - {fill_numbers}")

    # if n % 2 == 1 :
    #     index = n // 2 + 1
    # else :
    #     index = n // 2

    multi_pairs = [fill_numbers[i] * fill_numbers[n - 1- i] for i in range(ceil(n / 2))] # ceil(n / 2) == index
    print (f"Список умноженных пар - {multi_pairs}")

    Break()



def zadacha_13() :
    # Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
    # Пример: - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

    os.system('CLS')

    print("Задача 13. Создаёт список из N элементов вещественных чисел и находит разницу между макс. и мин. дробной части элементов\n")
    n = int(input("Введите N: "))

    fill_numbers = [round(random() + randint(0, 10), 2) for i in range(n)]
    print (f"Список - {fill_numbers}")

    max = fill_numbers[0] - fill_numbers[0] // 1
    min = fill_numbers[0] - fill_numbers[0] // 1

    for i in fill_numbers :
        j = i - i // 1
        if j > max :
            max = j
        elif j < min :
            min = j 

    diff = max - min
    print(f"Разница = {round(diff, 2)}")

    Break()



def zadacha_14() :
    # Напишите программу, которая будет преобразовывать десятичное число в двоичное.
    # Пример:
    # - 45 -> 101101
    # - 3 -> 11
    # - 2 -> 10

    os.system('CLS')

    print("Задача 14. Преобразовывать десятичное число N в двоичное\n")
    n = int(input("Введите N: "))

    result = ''

    while n != 1:
        if n % 2 == 1:
            result = '1' + result
            n = (n - 1) / 2
        elif n % 2 == 0:
            result = '0' + result
            n = n / 2
            
    if n == 0:
        result = '0' + result
    elif n == 1:
        result = '1' + result

    print(f"В двоичной системе: {result}")

    Break()



def zadacha_15() :
    # Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
    # Пример:
    # - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

    os.system('CLS')

    print("Задача 15. Составляет список чисел Фибоначчи, в том числе для отрицательных индексов\n")
    n = int(input("Введите N: "))

    def fib(number, mode = 0) :
        if number == 1 or number == 0 :
            return 1
        else :
            if mode == 1:
                return fib (number - 2, 1) - fib (number - 1, 1)
            else :
                return fib (number - 1) + fib (number - 2)

    list = [0]
    for i in range(n) :
        list.insert(0, fib(i + 3, 1))
        list.append(fib(i))

    print(list)

    Break()



def Break() :
    code = int(input("\nДля выбора другой задачи - 5. Для завершения - 0\n"))
    if code == 5 :
        Run()



Run()