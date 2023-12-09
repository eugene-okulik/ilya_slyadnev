from datetime import datetime

first_date = "Jan 15, 2023 - 12:05:33"

date_obj = datetime.strptime(first_date, "%b %d, %Y - %H:%M:%S")

print(f"Полное название месяца: {date_obj.strftime('%B')}")
print(f"Новый формат: {date_obj.strftime('%d.%m.%Y, %H:%M')}")
