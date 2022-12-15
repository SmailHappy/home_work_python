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
li = [i for i in numbers if numbers.count(i) == 1]
print (f"Список не повторяющихся элементов - {li}")



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
count = 0
result = [count + 1 for i in range(1, len(text)) if int(text[i]) > int(text[i - 1])]

print (count)
