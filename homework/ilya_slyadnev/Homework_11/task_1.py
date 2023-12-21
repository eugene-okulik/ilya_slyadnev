class Book:
    material = "бумага"
    has_text = True

    def __init__(self, title, author, num_pages, ISBN, reserved=False):
        self.title = title
        self.author = author
        self.num_pages = num_pages
        self.ISBN = ISBN
        self.reserved = reserved


book1 = Book("Преступление и наказание", "Федор Достоевский", 551, "978-5171011937", True)
book2 = Book("Война и мир", "Лев Толстой", 1274, "978-5389076671")
book3 = Book("Мастер и Маргарита", "Михаил Булгаков", 384, "978-5171032871")
book4 = Book("Анна Каренина", "Лев Толстой", 864, "978-5170742099")
book5 = Book("Братья Карамазовы", "Федор Достоевский", 1225, "978-5170819250")

books = [book1, book2, book3, book4, book5]
for book in books:
    if book.reserved:
        print(f"Название: {book.title}, Автор: {book.author}, страниц: {book.num_pages}, материал: {Book.material}, "
              f"зарезервирована")
    else:
        print(f"Название: {book.title}, Автор: {book.author}, страниц: {book.num_pages}, материал: {Book.material}")


class SchoolBook(Book):
    def __init__(self, title, author, num_pages, ISBN, subject, school_classroom,
                 availability_of_tasks, reserved=False):
        super().__init__(title, author, num_pages, ISBN, reserved)
        self.subject = subject
        self.school_classroom = school_classroom
        self.availability_of_tasks = availability_of_tasks


school_book1 = SchoolBook("Алгебра", "Иванов", 200, "111", 'Математика', '9', True, True)
school_book2 = SchoolBook("Алгебра", "Петров", 300, "222", 'Математика', '10', True, False)

school_books = [school_book1, school_book2]
for book in school_books:
    if book.reserved:
        print(f"Название: {book.title}, Автор: {book.author}, страниц: {book.num_pages}, предмет: {book.subject}, "
              f"класс: {book.school_classroom}, зарезервирована")
    else:
        print(f"Название: {book.title}, Автор: {book.author}, страниц: {book.num_pages}, предмет: {book.subject}, "
              f"класс: {book.school_classroom}")
