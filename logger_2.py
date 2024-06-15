
from logger import input_data, print_data
def delete_data():
    name = input("Введите имя или фамилию для удаления: ")
    with open("data_first_variant.csv", "r", encoding="utf-8") as f:
        lines = f.readlines()
    with open("data_first_variant.csv", "w", encoding="utf-8") as f:
        for line in lines:
            if name not in line:
                f.write(line)
    with open("data_second_variant.csv", "r", encoding="utf-8") as f:
        lines = f.readlines()
    with open("data_second_variant.csv", "w", encoding="utf-8") as f:
        for line in lines:
            if name not in line:
                f.write(line)

def change_data():
    name = input("Введите имя или фамилию для изменения: ")
    new_data = input("Введите новые данные: ")
    with open("data_first_variant.csv", "r", encoding="utf-8") as f:
        lines = f.readlines()
    with open("data_first_variant.csv", "w", encoding="utf-8") as f:
        for line in lines:
            if name in line:
                f.write(new_data + "\n")
            else:
                f.write(line)
    with open("data_second_variant.csv", "r", encoding="utf-8") as f:
        lines = f.readlines()
    with open("data_second_variant.csv", "w", encoding="utf-8") as f:
        for line in lines:
            if name in line:
                f.write(new_data.replace(";", ";") + "\n")
            else:
                f.write(line)