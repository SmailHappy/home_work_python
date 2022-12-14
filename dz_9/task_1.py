# Создайте программу (можно взять любой прошлый проект) при помощи виртуального окружения и PIP(в семинаре все обсудили по этому поводу.

# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка.

from random import randint
from isOdd import isOdd
fill_numbers = [randint(0, 100) for i in range(4)]
print (f"Список - {fill_numbers}") 
print (f"Сумма  четных цифр = {sum(i for i in fill_numbers if not isOdd(i))}") 

# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример: - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

print (f"Сумма цифр на нечётных позициях = {sum(fill_numbers[i] for i in range(len(fill_numbers)) if isOdd(i))}") 
