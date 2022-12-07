from random import randint

# Вычислить число c заданной точностью d
# Пример : - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

number = str(input('Введите число: '))
# degree = int(input('Введите степень d (без " - "): '))
degree = float(input('Введите точность d: '))

count = 1
for i in number :
    if i == '.' or i == ',':
        # number = number[:count + degree]
        number = number[:count + len(str(degree)) - 2]
    count += 1

print (number)



# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

number = int(input('Введите число N: '))

def simple_multipliers(input_number) :
    list_simple_multipliers = [2, 3, 5, 7, 11, 13, 17, 19] #, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]

    for i in list_simple_multipliers :
        if input_number % i == 0 :
            return i

    return input_number

list_multipliers_number = []

while number > 1 :
    num = simple_multipliers(number)
    list_multipliers_number.append(num)
    number /= num
    
print(list_multipliers_number)



# Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной последовательности.

numbers = input('Задайте последовательность чисел:\n').split()
li = []
for i in numbers :
    if i in li :
        continue
    else :
        li.append(i)

print (f"Список не повторяющихся элементов - {li}")



# Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена 
# и записать в файл многочлен степени k.

# Пример: - k=2 => 
# 1x² + 2x + 3 = 0 или 
# 1x² + 2x = 0 или
# 1x² + 3 = 0 или 
# 1x² = 0

# Пример: - k=3 => 
# 1x³ + 2x² + 3x + 4 = 0 или 
# 1x³ + 2x² + 3х = 0 или 
# 1x³ + 2x² + 4 = 0 или
# 1x³ + 3x + 4 = 0 или 
# 1x³ + 2x² = 0 или 
# 1x³ + 3x = 0 или 
# 1x³ + 4 = 0" или 
# 1x³ = 0

degree_k = int(input("Введите натуральную степень k: "))
list_coef = [randint(0, 100) for i in range(101)]

result = str(list_coef[randint(0, 100)]) + 'x^' + str(degree_k)

degree_k = degree_k - 1

while degree_k >= 0 :
    coef = randint(0, 1)
    if coef == 1 :
        if degree_k == 0 :
            result += ' + ' + str(list_coef[randint(0, 100)])
        else :
            result += ' + ' + str(list_coef[randint(0, 100)]) + 'x^' + str(degree_k)
    degree_k -= 1

result = result + ' = 0'

poly_degree_k = open('home_work/4dz_polynomials_degree_k.txt', 'w')
poly_degree_k.write(result)
poly_degree_k.close()



# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.

def polynomials() :
    degree_k = randint(1, 9)
    list_coef = [randint(0, 100) for i in range(101)]
    result = str(list_coef[randint(0, 100)]) + 'x^' + str(degree_k)
    degree_k = degree_k - 1

    while degree_k >= 0 :
        coef = randint(0, 1)
        if coef == 1 :
            if degree_k == 0 : result += ' + ' + str(list_coef[randint(0, 100)])
            else : result += ' + ' + str(list_coef[randint(0, 100)]) + 'x^' + str(degree_k)
        degree_k -= 1

    result = result + ' = 0'
    return result

def file_poly(file) :
    with open(file, 'w') as poly_sum_file :
        poly_sum_file.write(polynomials())
    with open(file, 'r') as poly_sum_file :
        poly = poly_sum_file.read()
    return poly

def find_index(text) :
    count = 0
    for i in text : 
        if not i == 'x' : count += 1
        else : return count
    return count

poly_1 = file_poly('home_work/4dz_poly_for_sum_1.txt')
poly_2 = file_poly('home_work/4dz_poly_for_sum_2.txt')

poly_1 = poly_1.replace('+', '').replace('=', '').split()[:-1]
poly_2 = poly_2.replace('+', '').replace('=', '').split()[:-1]

result = []

if len(poly_1) > len(poly_2) : g = len(poly_1)
else : g = len(poly_2)

while g >= 0 :
    if len(poly_1) == 0 :       # Проверка на пустой список 1
        if not len(poly_2) == 0 :       # При условие что 2 не пустой
            result.append(poly_2[0])
            del poly_2[0]
            g = len(poly_2)
    elif len(poly_2) == 0 :     # Проверка на пустой список 2
        if not len(poly_1) == 0 :       # При условие что 1 не пустой 
            result.append(poly_1[0])
            del poly_1[0]
            g = len(poly_1)

    else :
        if find_index(poly_1[0]) == len(poly_1[0]) :        # Проверка на 'x' в 1 списке
            for i in range(len(poly_2)) :
                if find_index(poly_2[i]) == len(poly_2[i]) :        # Поиск числа без 'x' во 2 списке
                    sum = int(poly_1[0]) + int(poly_2[i])
                    result.append(str(sum))
                    del poly_1[0]
                    del poly_2[i]
                    break
            if not len(poly_1) == 0 : 
                result.append(poly_1[0])
                del poly_1[0]
        elif find_index(poly_2[0]) == len(poly_2[0]) :      # Проверка на 'x' во 2 списке
            for i in range(len(poly_1)) :
                if find_index(poly_1[i]) == len(poly_1[i]) :        # Поиск числа без 'x' в 1 списке
                    sum = int(poly_2[0]) + int(poly_1[i])
                    result.append(str(sum))
                    del poly_2[0]
                    del poly_1[i]
                    break
            if not len(poly_2) == 0 : 
                result.append(poly_2[0])
                del poly_2[0]   

        elif int(poly_1[0][-1:]) > int(poly_2[0][-1:]) :        # Сравнение степеней 'x' в 1 и 2 списке
            result.append(poly_1[0])
            del poly_1[0]
        elif int(poly_1[0][-1:]) == int(poly_2[0][-1:]) : 
            sum_coef = int(poly_1[0][:find_index(poly_1[0])]) + int(poly_2[0][:find_index(poly_2[0])])
            result.append(str(sum_coef) + poly_1[0][-3:])
            sum_coef = 0
            del poly_1[0]
            del poly_2[0]
        else :
            result.append(poly_2[0])
            del poly_2[0]
    g -= 1

with open('home_work/4dz_sum_poly.txt', 'w') as sum_poly :
    temp = ''
    res = result[0]
    for i in result[1:] :
        if find_index(i) == len(i) : temp = ' + ' + i
        else : res += ' + ' + i
    res += temp + ' = 0'
    sum_poly.write(res)