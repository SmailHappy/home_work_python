def show_all_workers() :
    with open('full_base.txt', 'r', encoding='utf-8') as database :
        print("\nИндекс " + " " * 8 + "Имя  "
                + " " * 10 + "Фамилия" + " " * 8
                + "Должноть" + " " * 7 + "Зарплата" + " " * 7
                + "Номер Телефона" + "\n" + "=" * 89)
        data = (database.read()).split(',')
        result = ''
        for i in range(len(data)) :
            count = 0
            if i % 5 == 0 :
                for j in data[i][-1:] :
                    if j == 'n' : break
                    else : count += 1
            else : count = len(data[i])
            space = 15 - count
            result += data[i] + " " * space 
        print (result)





def add_worker() :
    with open('full_base.txt', 'r', encoding='utf-8') as database :
        data = database.read()
        index = data.count('\n')

    with open('full_base.txt', 'a', encoding='utf-8') as database:
        id = str(index + 1)
        last_name = input('\nВведите фамилию: ')
        if last_name == '' : last_name = '---'
        first_name = input('Введите имя: ')
        if first_name == '' : first_name = '---'
        position = input('Введите должность: ')
        if position == '' : position = '---'
        salary = input('Введите зарплату сотрудника: ')
        if salary == '' : salary = '---'
        phone_number = input('Введите номер телефона: ')
        if phone_number == '' : phone_number = '---'
        data = id + ',' + first_name + ',' + last_name + ',' + position + ',' + salary + ',' + phone_number 
        database.write(data + '\n')
        print('Сотрудник успешно добавлен')





def del_worker(index: int) :
    index = int(index)
    with open('full_base.txt', 'r', encoding='utf-8') as database :
        data = database.read()
        if index > data.count('\n') : return print('Неверный индекс, такого сотрудника нет')
    
    with open('full_base.txt', 'r', encoding='utf-8') as database :
        result = ''
        flag = 0
        for line in database:
            data = line.split(',')
            if data[0] == str(index): 
                flag = 1
                print ('Сотрудник успешно удален')
            if flag > 0 :
                if flag == 1 : flag = 2 
                else : result += str(int(data[0]) - 1) + ',' + data[1] + ',' + data[2] + ',' + data[3] + ',' + data[4] + ',' + data[5]
            else : result += line
            
    with open('full_base.txt', 'w', encoding='utf-8') as database:
        database.write(result)





def find_worker(last_name: str) :
    count = 0
    result = ''
    with open('full_base.txt', 'r', encoding='utf-8') as database :
        for line in database:
            if last_name in line:
                data = line.split(',')
                for i in range(len(data)) :
                    if i == 5 :
                        result += data[i]
                    else :
                        space = 15 - len(data[i])
                        result += data[i] + " " * space 
                count += 1
    if count == 0: print('Сотрудников с такой фамилией нет') 
    else :
        print("\nИндекс " + " " * 8 + "Имя  "
                + " " * 10 + "Фамилия" + " " * 8
                + "Должноть" + " " * 7 + "Зарплата" + " " * 7
                + "Номер Телефона" + "\n" + "=" * 89)
        print(result)





def refresh_worker(index: int) :
    index = int(index)
    with open('full_base.txt', 'r', encoding='utf-8') as database :
        data = database.read()
        if index > data.count('\n') : return print('Неверный индекс, такого сотрудника нет')
    
    with open('full_base.txt', 'r', encoding='utf-8') as database :
        result = ''
        for line in database:
            data = line.split(',')
            if data[0] == str(index):
                refresh = int(input('1. Имя\n2. Фамилия\n3. Должность' +
                                '\n4. Зарплата\n5. Номер Телефона\n' +
                                'Какие данные хотите обновить?  '))
                if refresh == 1 :
                    first_name = input('Введите новое Имя: ')
                    data[1] = first_name
                elif refresh == 2 :
                    last_name = input('Введите фамилию: ')
                    data[2] = last_name
                elif refresh == 3 :
                    position = input('Введите новую должность: ')
                    data[3] = position
                elif refresh == 4 :
                    salary = input('Введите новую зарплоату: ')
                    data[4] = salary
                elif refresh == 5 :
                    phone_number = input('Введите новый номер телефона: ')
                    data[5] = phone_number + '\n'
                print ('Данные сотрудника обновлены')
            result += data[0] + ',' + data[1] + ',' + data[2] + ',' + data[3] + ',' + data[4] + ',' + data[5]
            
    with open('full_base.txt', 'w', encoding='utf-8') as database:
        database.write(result)





def position(position: str) :
    count = 0
    result = ''
    with open('full_base.txt', 'r', encoding='utf-8') as database :
        for line in database:
            data = line.split(',')
            if position.lower() == data[3].lower():
                for i in range(len(data)) :
                    if i == 5 :
                        result += data[i]
                    else :
                        space = 15 - len(data[i])
                        result += data[i] + " " * space 
                count += 1
    if count == 0: print('Сотрудников с такой должностью нет') 
    else :
        print("\nИндекс " + " " * 8 + "Имя  "
                + " " * 10 + "Фамилия" + " " * 8
                + "Должноть" + " " * 7 + "Зарплата" + " " * 7
                + "Номер Телефона" + "\n" + "=" * 89)
        print(result)





def salary(level: int) :
    level = int(level)
    if level < 0 or level > 15 : return print('Неверный код.')
    salary = level * 10000
    count = 0
    result = ''
    with open('full_base.txt', 'r', encoding='utf-8') as database :
        for line in database:
            data = line.split(',')
            if salary <= int(data[4]) <= (salary + 10000):
                for i in range(len(data)) :
                    if i == 5 :
                        result += data[i]
                    else :
                        space = 15 - len(data[i])
                        result += data[i] + " " * space 
                count += 1
    if count == 0: print('Сотрудников с такой зарплатой нету') 
    else :
        print("\nИндекс " + " " * 8 + "Имя  "
                + " " * 10 + "Фамилия" + " " * 8
                + "Должноть" + " " * 7 + "Зарплата" + " " * 7
                + "Номер Телефона" + "\n" + "=" * 89)
        print(result)





def export_json() :
    import json
    with open("workers.json", "w", encoding = 'utf-8') as w_file:
        with open('full_base.txt', 'r', encoding = 'utf-8') as database :
            for line in database:
                data = line.replace('\n', '').split(',')
                result = {"Индекс": data[0], "Имя": data[1], "Фамилия": data[2], "Должность": data[3], "Зарплата": data[4], "Номер телефона": data[5]}
                json.dump(result, w_file, indent = 4)
    print ('Успешный экспорт')
    




def export_csv() :
    import csv
    with open("workers.csv", "w", encoding = 'utf-8') as w_file:
        file_writer = csv.writer(w_file, delimiter = ",", lineterminator= "\r")
        file_writer.writerow(["Индекс", "Имя", "Фамилия", "Должность", "Зарплата", "Номер телефона"])
        with open('full_base.txt', 'r', encoding = 'utf-8') as database :
            for line in database:
                data = line.replace('\n', '').split(',')
                file_writer.writerow(data)
    print ('Успешный экспорт')