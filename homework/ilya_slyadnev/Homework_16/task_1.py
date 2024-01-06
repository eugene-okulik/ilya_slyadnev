import os
import csv
from mysql.connector import connect
from dotenv import load_dotenv
from faker import Faker


'''
Блок для генирации тестовых данных
'''

fake = Faker()
name = fake.first_name()
second_name = fake.last_name()
title_groups = fake.company()
title_book_v1 = fake.catch_phrase()
title_book_v2 = fake.catch_phrase()


'''
Блок для подключения к БД
'''

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
if db.is_connected():
    print("Успешное подключение к БД.")
    print()

'''
Блок выполнения SQL запросов
'''

cursor = db.cursor()
cursor.execute(
    "INSERT INTO `groups` (title, start_date, end_date) "
    "VALUES (%s, %s, %s)", (title_groups, 'sep 2023', 'feb 2024')
)
group_id = cursor.lastrowid

cursor.execute(
    "INSERT INTO students (name, second_name, group_id) "
    "VALUES (%s, %s, %s)", (name, second_name, group_id)
)
student_id = cursor.lastrowid

sql_create_book = (
    "INSERT INTO books (title, taken_by_student_id) "
    "VALUES (%s, %s)"
)
book_data = [(title_book_v1, student_id), (title_book_v2, student_id)]
cursor.executemany(sql_create_book, book_data)

sql_create_subjects = (
    "INSERT INTO subjets (title) VALUES (%s)"
)
subjects_data = [('Python course Okulik',), ('SQL course Okulik',)]
cursor.executemany(sql_create_subjects, subjects_data)

cursor.execute("SELECT LAST_INSERT_ID() as last_id")
last_subjects_id = cursor.fetchone()[0]
cursor.execute(
    "SELECT id FROM subjets ORDER BY id DESC LIMIT 1, 1"
)
previous_subjects_id = cursor.fetchone()[0]

sql_create_lessons = (
    "INSERT INTO lessons (title, subject_id) VALUES (%s, %s)"
)
lesson_data = [
    ('Lesson Python', last_subjects_id,),
    ('Lesson SQL', previous_subjects_id,)
]
cursor.executemany(sql_create_lessons, lesson_data)

cursor.execute("SELECT LAST_INSERT_ID() as last_id")
last_lesson_id = cursor.fetchone()[0]
cursor.execute(
    "SELECT id FROM lessons ORDER BY id DESC LIMIT 1, 1"
)
previous_lesson_id = cursor.fetchone()[0]

sql_create_marks = (
    "INSERT INTO marks (value, lesson_id, student_id) "
    "VALUES (%s, %s, %s)"
)
marks_data = [
    ('Great', last_lesson_id, student_id),
    ('Unsatisfactory', previous_lesson_id, student_id)
]
cursor.executemany(sql_create_marks, marks_data)


'''
Блок вывода информации о студенте
'''

cursor.execute(
    "SELECT value FROM marks WHERE student_id=%s", (student_id,)
)
marks_student = cursor.fetchall()
print("Все оценки студента", marks_student)

cursor.execute(
    "SELECT title FROM books WHERE taken_by_student_id=%s",
    (student_id,)
)
books_student = cursor.fetchall()
print("Все книги студента", books_student)

sql_info_student = """
SELECT
    students.id AS student_id,
    students.name AS student_name,
    students.second_name AS student_second_name,
    `groups`.title AS group_title,
    books.title AS book_title,
    marks.value AS mark_value,
    `subjets`.title AS subject_title,
    lessons.title AS lesson_title
FROM
    students
JOIN
    `groups` ON students.group_id = `groups`.id
LEFT JOIN
    books ON students.id = books.taken_by_student_id
LEFT JOIN
    marks ON students.id = marks.student_id
LEFT JOIN
    lessons ON marks.lesson_id = lessons.id
LEFT JOIN
    `subjets` ON lessons.subject_id = `subjets`.id
WHERE
    students.id = %s;
"""

cursor.execute(sql_info_student, (student_id,))
info_student = cursor.fetchall()
print("Все о студенте", info_student)

'''
Блок чтения и проверки csv файла
'''

current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, '..', '..', 'eugene_okulik', 'Lesson_16', 'hw_data', 'data.csv')

with open(file_path, "r") as file:
    csv_reader = csv.reader(file)

    for row in csv_reader:
        name, second_name, group_title, book_title, subject_title, lesson_title, mark_value = row

    cursor.execute("SELECT * FROM students WHERE name=%s AND second_name=%s", (name, second_name))
    student = cursor.fetchone()
    if student:
        print()
        print(f"Студент {name} {second_name} найден в базе данных.")
        print()
    else:
        print()
        print(f"Студент {name} {second_name} не найден в базе данных.")

db.commit()
cursor.close()

db.close()
print()
print("Соединение с БД закрыто.")
