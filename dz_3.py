from random import randint
from random import random
from math import ceil

# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример: - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

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



# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

n = int(input("Введите N: "))

fill_numbers = [randint(0, 10) for i in range(n)]
print (f"Список - {fill_numbers}")

# if n % 2 == 1 :
#     index = n // 2 + 1
# else :
#     index = n // 2

multi_pairs = [fill_numbers[i] * fill_numbers[n - 1- i] for i in range(ceil(n / 2))] # ceil(n / 2) == index
print (f"Список умноженных пар - {multi_pairs}")



# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример: - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

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



# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

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



# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

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