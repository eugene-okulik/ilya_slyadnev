import os
import csv
from mysql.connector import connect
from dotenv import load_dotenv


load_dotenv()
db_host = os.getenv('DB_HOST')
db_port = os.getenv('DB_PORT')
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSW')
db_name = os.getenv('DB_NAME')

db = connect(
    host=db_host,
    port=db_port,
    user=db_user,
    password=db_password,
    database=db_name
)

cursor = db.cursor()
current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, '..', '..', 'eugene_okulik', 'Lesson_16', 'hw_data', 'data.csv')

with open(file_path, "r") as file:
    csv_reader = csv.reader(file)

    for row in csv_reader:
        name, second_name, group_title, book_title, subject_title, lesson_title, mark_value = row

    cursor.execute("SELECT * FROM students WHERE name=%s AND second_name=%s", (name, second_name))
    student = cursor.fetchone()
    if student:
        print(f"Студент {name} {second_name} найден в базе данных.")
    else:
        print(f"Студент {name} {second_name} не найден в базе данных.")

db.commit()
cursor.close()
db.close()
