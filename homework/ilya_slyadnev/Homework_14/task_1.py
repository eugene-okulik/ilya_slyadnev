import mysql.connector
from dotenv import load_dotenv
import os
from faker import Faker

fake = Faker()


def insert_and_get_id(cursor, query, fetch_last_id=True):
    cursor.execute(query)
    if fetch_last_id:
        cursor.execute("SELECT LAST_INSERT_ID()")
        return cursor.fetchone()[0]


# Функция для вывода содержимого таблицы
def print_table(cursor, table_name):
    cursor.execute(f"SELECT * FROM {table_name};")
    records = cursor.fetchall()
    print(f"Список {table_name}:")
    for record in records:
        print(record)
    print("")


load_dotenv()

# Подключение к БД
conn = mysql.connector.connect(
    host=os.getenv('DB_HOST'),
    port=os.getenv('DB_PORT'),
    user=os.getenv('DB_USER'),
    password=os.getenv('DB_PASSWORD'),
    database=os.getenv('DB_NAME')
)
cursor = conn.cursor()

# Создание группы и студента
title_groups = fake.company()
group_id = insert_and_get_id(cursor,
                             f"INSERT INTO `groups` (title, start_date, end_date) VALUES ('{title_groups}', 'sep 2023', 'feb 2024')")

name = fake.first_name()
second_name = fake.last_name()
student_id = insert_and_get_id(cursor,
                               f"INSERT INTO students (name, second_name, group_id) VALUES ('{name}', '{second_name}', {group_id})")

# Создание книг
titles_books = [fake.catch_phrase() for _ in range(2)]
for title in titles_books:
    insert_and_get_id(cursor, f"INSERT INTO books (title, taken_by_student_id) VALUES ('{title}', {student_id})")

# Создание предметов и занятий
titles_subjects = ['Python course Okulik', 'SQL course Okulik']
subject_ids = [insert_and_get_id(cursor, f"INSERT INTO `subjets` (title) VALUES ('{title}')") for title in
               titles_subjects]

for subject_id in subject_ids:
    for _ in range(2):  # По два занятия для каждого предмета
        lesson_title = f"Lesson on subject {subject_id}"
        insert_and_get_id(cursor, f"INSERT INTO lessons (title, subject_id) VALUES ('{lesson_title}', {subject_id})")

# Ставим оценки для занятий каждого предмета
marks_values = ['Great', 'Unsatisfactory']
for subject_id in subject_ids:
    cursor.execute(f"SELECT id FROM lessons WHERE subject_id = {subject_id}")
    lesson_ids = [lesson[0] for lesson in cursor.fetchall()]
    for lesson_id in lesson_ids:
        for mark_value in marks_values:
            insert_and_get_id(cursor,
                              f"INSERT INTO marks (value, lesson_id, student_id) VALUES ('{mark_value}', {lesson_id}, {student_id})")

sql_select_marks = f"SELECT value FROM marks WHERE student_id={student_id}"
cursor.execute(sql_select_marks)
marks_student = cursor.fetchall()
print(f"Все оценки студента", marks_student)

sql_select_marks = f"SELECT title FROM books WHERE taken_by_student_id={student_id}"
cursor.execute(sql_select_marks)
book_student = cursor.fetchall()
print(f"Все книги студента", book_student)

sql_info_student = (f"SELECT students.id AS student_id, students.name AS student_name, students.second_name AS "
                    f"student_second_name, `groups`.title AS group_title, books.title AS book_title, marks.value AS "
                    f"mark_value, `subjets`.title AS subject_title, lessons.title AS lesson_title FROM students JOIN "
                    f"`groups` ON students.group_id = `groups`.id LEFT JOIN books ON students.id = "
                    f"books.taken_by_student_id LEFT JOIN marks ON students.id = marks.student_id LEFT JOIN lessons "
                    f"ON marks.lesson_id = lessons.id LEFT JOIN `subjets` ON lessons.subject_id = `subjets`.id WHERE "
                    f"students.id = {student_id};")
cursor.execute(sql_info_student)
info_student = cursor.fetchall()
print(f"Все о студенте", info_student)

conn.close()
