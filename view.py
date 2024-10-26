class BookView:
    def show_book(self, book):
        print(book)

    def add_book(self):
        title = input("Введите название книги: ")
        author = input("Введите автора книги: ")
        year = int(input("Введите год издания книги: "))
        return Book(title, author, year)

    def delete_book(self, book):
        print(f"Книга '{book.title}' удалена")