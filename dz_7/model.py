def export():
    format_knigi = input('С каким форматом хотите работать?\n\
        1. формат CSV\n\
        2. формат TXT\n\
        ===1 or 2 ?===> ')
    if format_knigi == '1':
        with open('phone_book.csv', 'a', encoding='utf-8') as file:
            family = input('Введите фамилию: ')
            name = input('Введите имя: ')
            tel = input('Введите номер телефона: ')
            data = family+ ',' + name + ',' + tel
            file.write('\n' + data)
    else:
        with open('phone_book.txt', 'a', encoding='utf-8') as file:
            family = input('Введите фамилию: ')
            name = input('Введите имя: ')
            tel = input('Введите номер телефона: ')
            data = family+ ',' + name + ',' + tel
            file.write('\n' + data)
            
def import_cont():
    format_knigi = input('С каким форматом хотите работать?\n\
        1. формат CSV\n\
        2. формат TXT\n\
        ===1 or 2 ?===>')
    if format_knigi == '1':
        print("---"*22)
        print('Фамилия \t\t Имя       \t\t Номер_Телефона')
        print("---"*22)
        with open('phone_book.csv', 'r', encoding='utf-8') as file:
            for line in file:
                import_cont = line.split(',')
                print('\t\t\t'.join(import_cont),end='')
        print('\n')
    else:
        print("---"*22)
        print('Фамилия \t\t Имя       \t\t Номер_Телефона')
        print("---"*22)
        with open('phone_book.txt', 'r', encoding='utf-8') as file:
            for line in file:
                import_cont = line.split(',')
                print('\t\t\t'.join(import_cont),end='')
        print('\n')


def search_cont():
    format_knigi = input('С каким форматом хотите работать?\n\
        1. формат CSV\n\
        2. формат TXT\n\
        ===1 or 2 ?===>')
    if format_knigi == '1':
        count = 0
        family = input('\nВведите фамилию или имя абонента: ')
        with open('phone_book.csv', 'r', encoding='utf-8') as file:
            for line in file:
                if family in line:
                    print("---"*22)
                    print('Фамилия \t\t Имя       \t\t Номер Телефона')
                    print("---"*22)
                    print('\t\t\t'.join(line.split(',')))
                    count = count + 1
        if count == 0:
            print('У вас в книги нет абонента с данной фамилией!')
    else:
        count = 0
        family = input('\nВведите фамилию или имя абонента: ')
        with open('phone_book.txt', 'r', encoding='utf-8') as file:
            for line in file:
                if family in line:
                    print("---"*22)
                    print('Фамилия \t\t Имя       \t\t Номер_Телефона')
                    print("---"*22)
                    print('\t\t\t'.join(line.split(',')))
                    count = count + 1
        if count == 0:
            print('У вас в книги нет абонента с данной фамилией!') 