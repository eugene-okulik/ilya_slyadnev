class Book:
    def __init__(self, material, has_text, title, author, num_pages, ISBN, reserved=False):
        self.material = material
        self.has_text = has_text
        self.title = title
        self.author = author
        self.num_pages = num_pages
        self.ISBN = ISBN
        self.reserved = reserved


book1 = Book("бумага", True, "Преступление и наказание", "Федор Достоевский", 551, "978-5171011937")
book2 = Book("бумага", True, "Война и мир", "Лев Толстой", 1274, "978-5389076671")
book3 = Book("бумага", True, "Мастер и Маргарита", "Михаил Булгаков", 384, "978-5171032871")
book4 = Book("бумага", True, "Анна Каренина", "Лев Толстой", 864, "978-5170742099")
book5 = Book("бумага", True, "Братья Карамазовы", "Федор Достоевский", 1225, "978-5170819250", True)

books = [book1, book2, book3, book4, book5]
for book in books:
    if book.reserved:
        print(f"Название: {book.title}, Автор: {book.author}, страниц: {book.num_pages}, материал: {book.material}, "
              f"зарезервирована")
    else:
        print(f"Название: {book.title}, Автор: {book.author}, страниц: {book.num_pages}, материал: {book.material}")


class SchoolBooks(Book):
    def __init__(self, material, has_text, title, author, num_pages, ISBN, subject, school_classroom,
                 availability_of_tasks, reserved=False):
        Book.__init__(self, material, has_text, title, author, num_pages, ISBN, reserved)
        self.subject = subject
        self.school_classroom = school_classroom
        self.availability_of_tasks = availability_of_tasks


school_book1 = SchoolBooks("бумага", True, "Алгебра", "Иваанов", "200", 111, 'Математика', '9', True, True)
school_book2 = SchoolBooks("бумага", True, "Алгебра", "Петров", "300", 222, 'Математика', '10', True, False)

school_books = [school_book1, school_book2]
for book in school_books:
    if book.reserved:
        print("\n")  # это я для себя, так легче воспринимать
        print(f"Название: {book.title}, Автор: {book.author}, страниц: {book.num_pages}, предмет: {book.subject}, "
              f"класс: {book.school_classroom}, зарезервирована")
    else:
        print(f"Название: {book.title}, Автор: {book.author}, страниц: {book.num_pages}, предмет: {book.subject}, "
              f"класс: {book.school_classroom}")
