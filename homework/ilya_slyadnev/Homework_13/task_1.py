import re
from datetime import datetime, timedelta
import locale
import os

# Данные из файла
# 1. 2023-11-27 20:34:13.212967 - распечатать эту дату, но на неделю позже. Должно получиться 2023-12-04 20:34:13.212967
# 2. 2023-07-15 18:25:10.121473 - распечатать какой это будет день недели
# 3. 2023-06-12 15:23:45.312167 - распечатать сколько дней назад была эта дата


current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, '..', '..', 'eugene_okulik', 'hw_13', 'data.txt')

# Настройка для русского языка
locale.setlocale(locale.LC_TIME, 'ru_RU.UTF-8')


def process_date_action(date_str, number):
    date_object = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S.%f")
    current_date = datetime.now()

    if number.startswith('1'):
        new_date = date_object + timedelta(weeks=1)
        print(new_date.strftime("%Y-%m-%d %H:%M:%S.%f"))
    elif number.startswith('2'):
        print(date_object.strftime("%A"))
    elif number.startswith('3'):
        days_ago = (current_date - date_object).days
        print(f"{days_ago} дней назад")


with open(file_path, "r") as file:
    file_content = file.readlines()

for line_number, line in enumerate(file_content, start=1):
    parts = line.strip().split(" - ")

    if len(parts) == 2:
        number, date_str = parts[0].split(". ")
        action = parts[1]
        process_date_action(date_str, number)
