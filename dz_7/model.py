def export():
    format_knigi = input('\t1. CSV\n\t2. TXT\nС каким форматом хотите работать? ')
    if format_knigi == '1':
        with open('phone_book.csv', 'a', encoding='utf-8') as file:
            name = input('\nВведите имя: ')
            name_2 = input('Введите фамилию: ')
            telefon_number = input('Введите номер телефона: ')
            data = name_2 + ',' + name + ',' + telefon_number
            file.write('\n' + data)
    else:
        with open('phone_book.txt', 'a', encoding='utf-8') as file:
            name = input('Введите имя: ')
            name_2 = input('Введите фамилию: ')
            telefon_number = input('Введите номер телефона: ')
            data = name_2 + ',' + name + ',' + telefon_number
            file.write('\n' + data)

def import_cont():
    format_knigi = input('\t1. CSV\n\t2. TXT\nС каким форматом хотите работать? ')
    if format_knigi == '1':
        print("\nФамилия\t\tИмя\t\tНомер Телефона\n")
        with open('phone_book.csv', 'r', encoding='utf-8') as file:
            for line in file:
                import_cont = line.split(',')
                print('\t\t'.join(import_cont),end='')
        print('\n')
    else:
        print("\nФамилия\t\tИмя\t\tНомер Телефона\n")
        with open('phone_book.txt', 'r', encoding='utf-8') as file:
            for line in file:
                import_cont = line.split(',')
                print('\t\t'.join(import_cont),end='')
        print('\n')


def search_cont():
    format_knigi = input('\t1. CSV\n\t2. TXT\nС каким форматом хотите работать? ')
    if format_knigi == '1':
        count = 0
        name_2 = input('\nВведите фамилию или имя абонента: ')
        with open('phone_book.csv', 'r', encoding='utf-8') as file:
            for line in file:
                if name_2 in line:
                    print("\nФамилия\t\tИмя\t\tНомер Телефона\n")
                    print('\t\t'.join(line.split(',')))
                    count += 1
        if count == 0: print('Такого абонента нет')
    else:
        count = 0
        name_2 = input('\nВведите фамилию или имя абонента: ')
        with open('phone_book.txt', 'r', encoding='utf-8') as file:
            for line in file:
                if name_2 in line:
                    print("\nФамилия\t\tИмя\t\tНомер Телефона\n")
                    print('\t\t'.join(line.split(',')))
                    count += 1
        if count == 0: print('Такого абонента нет') 