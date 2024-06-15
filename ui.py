from logger import input_data, print_data
from logger_2 import delete_data, change_data

def interface():
    print("Добрый день! Вы попали на бот справочник от GeekBrains! \n 1 - запись данных \n 2 - вывод данных \n 3 - удаление данных \n 4 - изменение данных ")
    command = int(input('Введите число: '))

    while command != 1 and command != 2 and command != 3 and command != 4:
        print("Не правильный ввод")
        command = int(input("Ввведите число: "))

    if command == 1:
        input_data()
    elif command == 2:
        print_data()
    elif command == 3:
        delete_data()
    elif command == 4:
        change_data()