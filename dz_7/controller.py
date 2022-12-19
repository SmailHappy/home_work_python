import view as v
import model as m

def menu():
    vibor = input('Выберите пункт Меню: ')
    if vibor == '1':
        m.export()
        v.select_menu()
    elif vibor == '2':
        m.import_cont()
        v.select_menu()
    elif vibor == '3':
        m.search_cont()
        v.select_menu()
    elif vibor == '4':
        exit
    else:
        print('\n Невверный ввод !!!\n')
        v.select_menu()