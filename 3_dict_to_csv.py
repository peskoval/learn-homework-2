"""

Домашнее задание №2

Работа csv

1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору. 
   В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv

"""
from csv import DictWriter, QUOTE_NONNUMERIC


PERSONALITIES = [
    {'name': 'Albert', 'age': 34, 'job': 'Scientist'},
    {'name': 'Charles', 'age': 47, 'job': 'Pediatrician'},
    {'name': 'Genry', 'age': 23, 'job': 'Mechanic'},
    {'name': 'Martha', 'age': 56, 'job': 'Dog expert'},
    {'name': 'Mary', 'age': 29, 'job': 'Accountant'},
]
COLUMNS = ['name', 'age', 'job']

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    with open('personalities.csv', 'w', encoding='utf-8', newline='') as file:
        writer = DictWriter(file, fieldnames=COLUMNS, delimiter=';', quoting=QUOTE_NONNUMERIC)
        writer.writeheader()
        writer.writerows(PERSONALITIES)

if __name__ == "__main__":
    main()
