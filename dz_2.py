import os
from random import randint

def Run() :
    code = int(input ("Задача 6 - 6. Задача 7 - 7. Задача 8 - 8. Задача 9 - 9. Задача 10 - 10.\nВведите код задачи: "))
    if code == 6 :
        zadacha_6()
    elif code == 7 :
        zadacha_7()
    elif code == 8 :
        zadacha_8()
    elif code == 9 :
        zadacha_9()
    elif code == 10 :
        zadacha_10()
    else :
        print ("Такой задачи тут нет.")

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

    print ("Задача 8. Задаёт список из N чисел последовательности (1 + 1/n)^n\n")
    number = int(input("Введите число N: "))

    result = {i: round((1 + 1/i)**i, 2) for i in range(1, number + 1)}

    print (result)

    Break()

def zadacha_9() :
    # Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
    # Найдите произведение элементов на указанных позициях. 
    # Позиции хранятся в файле file.txt в одной строке одно число.

    os.system('CLS')

    print ("Задача 9. Задаёт список из N элементов и находит произведение элементов на указанных позициях\n")
    number = int(input("Введите число N: "))

    list = {i: randint(-number, number) for i in range(1, number + 1)}
    print(list)
    
    with open("home_work/file.txt", "w") as file :
        count_numbers = randint(2, number)
        print (f"\nКол-во позиций в файле = {count_numbers}")
        while count_numbers > 0 :
            file.write(str(randint(1, number)) + "\n")
            count_numbers -= 1

    with open("home_work/file.txt", "r") as file :
        result = 1
        for line in file :
            result *= list[int(line)]
        print (f"Произведение на указанных позициях = {result}")

    Break()

def zadacha_10() :
    # Реализуйте алгоритм перемешивания списка.

    os.system('CLS')

    print ("Задача 10. Перемешиванние списка из N эдементов\n")
    number = int(input("Введите число N: "))

    result = {i: i for i in range(1, number + 1)}

    print(f"Изначальный список: {result}")

    for i in result :
        index = randint(1, number)
        result[index], result[i] = result[i], result[index]

    print(f"Перемешанный список: {result}")

    Break()

def Break() :
    code = int(input("\nДля выбора другой задачи - 5. Для завершения - 0\n"))
    if code == 5 :
        Run()

Run()