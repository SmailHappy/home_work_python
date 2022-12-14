import controller

def show_menu() -> int:
    print("\n\t\t  Меню" + "\n" + "=" * 40 + "\n\
1. Показать всех сотрудников\n\
2. Добавить сотрудника\n\
3. Удалить сотрудника\n\
4. Найти сотрудника\n\
5. Обновить данные сотрудника\n\
6. Сделать выборку сотрудников по должности\n\
7. Сделать выборку сотрудников по зарплате\n\
8. Экспортировать данные в формате json\n\
9. Экспортировать данные в формате csv\n\
0. Закончить работу" + "\n" + "=" * 40 + "\n")
    controller.menu()

def show_menu_7() -> int:
    print("\nВыберите уровень зарплаты\n\
1. 10.000 - 20.000\t6. 60.000 - 70.000\t  11. 110.000 - 120.000\n\
2. 20.000 - 30.000\t7. 70.000 - 80.000\t  12. 120.000 - 130.000\n\
3. 30.000 - 40.000\t8. 80.000 - 90.000\t  13. 130.000 - 140.000\n\
4. 40.000 - 50.000\t9. 90.000 - 100.000\t  14. 140.000 - 150.000\n\
5. 50.000 - 60.000\t10. 100.000 - 110.000\t  15. 150.000 - 160.000\n")
    controller.salary_menu()