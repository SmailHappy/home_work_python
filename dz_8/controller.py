import view
import model

def menu():
    choice = input('Выберите необходимый пункт: ')
    if choice == '1':
        model.show_all_workers()
        view.show_menu()
    elif choice == '2':
        model.add_worker()
        view.show_menu()
    elif choice == '3':
        index = input('\nВведите индекс сотрудника, которого необходимо удалить: ')
        model.del_worker(index)
        view.show_menu()
    elif choice == '4':
        last_name = input('\nВведите фамилию сотрудника: ')
        model.find_worker(last_name)
        view.show_menu()
    elif choice == '5':
        index = input('\nВведите индекс сотрудника, чьи данные хотите обновить: ')
        model.refresh_worker(index)
        view.show_menu()
    elif choice == '6':
        position = input('\nВведите должность: ')
        model.position(position)
        view.show_menu()
    elif choice == '7':
        view.show_menu_7()
    elif choice == '8':
        model.export_json()
        view.show_menu()
    elif choice == '9':
        model.export_csv()
        view.show_menu()
    elif choice == '0':
        exit
    else:
        print('\nНевверный код.\n')
        view.show_menu()

def salary_menu() :
    level = input('Выберите необходимый уровень: ')
    model.salary(level)
    view.show_menu()
    