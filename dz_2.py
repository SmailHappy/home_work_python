from random import randint

# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

number = input("Введите число: ")
number = number.replace("," , '')
number = number.replace("." , '')
sum = 0

for i in number :
    sum += int(i)

print (sum)



# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

number = int(input("Введите число N: "))
num = 1
numb = 1

while num < number :
    numb *= num
    print (numb, end = ", ")
    num += 1

print (numb * number)



# Задайте список из n чисел последовательности $(1 + 1/n)^n$ и выведите на экран их сумму.
# Пример:
# - Для n = 4: {1: 2, 2: 2,25, 3: 2,37, 4: 2,44}

number = int(input("Введите число N: "))

result = [round((1 + 1/i)**i, 2) for i in range(1, number + 1)]
print (result)

sum = 0
for i in result :
    sum += i

print (f"Сумма = {sum}")



# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.

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



# Реализуйте алгоритм перемешивания списка.

number = int(input("Введите число N: "))

result = [i for i in range(number)]

print(f"Изначальный список: {result}")

for i in result :
    index = randint(1, number)
    result[index], result[i] = result[i], result[index]

print(f"Перемешанный список: {result}")