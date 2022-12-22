# Задача: предложить улучшения кода для уже решённых задач:
# С помощью использования **лямбд, filter, map, zip, enumerate, list comprehension(4 задачи из прошлых семинаров переделать с использованием этих функций)

# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример: - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

"""number = int(input("Введите число N: "))
num = 1
numb = 1

while num < number :
    numb *= num
    print (numb, end = ", ")
    num += 1

print (numb * number)"""

from math import factorial
number = int(input("Введите число N: "))
numb = [factorial(i) for i in range(1, number + 1)]
print (numb)



# # Задайте последовательность чисел. Напишите программу, 
# # которая выведет список неповторяющихся элементов исходной последовательности.

"""numbers = input('Задайте последовательность чисел:\n').split()
li = []

for i in numbers :
    if not i in li : li.append(i)

print (f"Список не повторяющихся элементов - {li}")"""

numbers = input('Задайте последовательность чисел:\n').split()
print (f"Список не повторяющихся элементов - ", [i for i in numbers if numbers.count(i) == 1])



# Стоимость строки
# Дана строка текста. Напишите программу для подсчета стоимости строки, исходя из того,
# что один любой символ (в том числе пробел) стоит 
# 60 копеек. Ответ дайте в рублях и копейках в соответствии с примерами.

"""text = input("Sample Input 1:\n")
lenght = len(text)
result = lenght * 60
print (f"Стоимость {result // 100} рублей {(result % 100)} копеек")"""

result = len(input("Sample Input 1:\n")) * 60
print (f"Стоимость {result // 100} рублей {(result % 100)} копеек")



# Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.
# Пример: - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

"""number = int(input("Введите число N: "))
ar = {}
for i in range(1, number + 1):
    ar[i] = 3 * i + 1
print (ar)"""

number = int(input("Введите число N: "))
result = {i: 3 * i + 1 for i in range(1, number + 1)}



# Больше предыдущего
# На вход программе подается строка текста из натуральных чисел. Из неё формируется список чисел. 
# Напишите программу подсчета количества чисел, которые больше предшествующего им в этом списке числа, то есть, стоят вслед за меньшим числом. 

"""text = input()
list = text.split(" ")

count = 0

for i in range(1, len(list)) :
    if int(list[i]) > int(list[i - 1]) :
        count += 1

print (list)
print(count)"""

text = input().split()

print (len([i for i in range(1, len(text)) if int(text[i]) > int(text[i - 1])]))



# # Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# # Пример: - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# n = int(input("Введите N: "))

# fill_numbers = [round(random() + randint(0, 10), 2) for i in range(n)]
# print (f"Список - {fill_numbers}")

# max = fill_numbers[0] - fill_numbers[0] // 1
# min = fill_numbers[0] - fill_numbers[0] // 1

# for i in fill_numbers :
#     j = i - i // 1
#     if j > max :
#         max = j
#     elif j < min :
#         min = j 

# diff = max - min
# print(f"Разница = {round(diff, 2)}")

# n = input("Введите список из вещественных чисел: ").split()
# print(sum(map(int, (filter(str.isdigit, input("Введите N: ").split())))))



# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

"""number = input("Введите число: ").replace("," , '').replace("." , '')
sum = 0

for i in number :
    sum += int(i)

print (sum)"""

print(sum(map(int, (filter(str.isdigit, input("Введите вещественное число: "))))))



# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

"""n = int(input("Введите N: "))

fill_numbers = [randint(0, 10) for i in range(n)]
print (f"Список - {fill_numbers}")

# if n % 2 == 1 :
#     index = n // 2 + 1
# else :
#     index = n // 2

multi_pairs = [fill_numbers[i] * fill_numbers[n - 1- i] for i in range(ceil(n / 2))] # ceil(n / 2) == index
print (f"Список умноженных пар - {multi_pairs}")"""

numbers = [2, 3, 4, 5, 6, 7, 5]
diff = list([a*b for a, b in zip(numbers, numbers[:(len(numbers)//2) - 1: -1])])
print(diff)



# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

"""n = int(input("Введите N: "))

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

print(list)"""

import random
a = random.randint(5, 11)
b = [1, 1]
[b.append(b[i-2] + b[i-1]) for i in range(2, a)]
[b.insert(0, b[1] - b[0]) for i in range(a + 1)]
print(b)