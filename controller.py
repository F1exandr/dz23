from view import BookView

class BookController:
    def __init__(self):
        self.books = []
        self.view = BookView()

    def add_book(self):
        book = self.view.add_book()
        self.books.append(book)
        self.view.show_book(book)

    def delete_book(self):
        title = input("Введите название книги для удаления: ")
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                self.view.delete_book(book)
                break
        else:
            print("Книга не найдена")

    def show_books(self):
        for book in self.books:
            self.view.show_book(book)