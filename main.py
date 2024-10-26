from controller import BookController

def main():
    controller = BookController()
    while True:
        print("1. Добавить книгу")
        print("2. Удалить книгу")
        print("3. Показать все книги")
        print("4. Выход")
        choice = input("Введите номер действия: ")
        if choice == "1":
            controller.add_book()
        elif choice == "2":
            controller.delete_book()
        elif choice == "3":
            controller.show_books()
        elif choice == "4":
            break
        else:
            print("Неправильный номер действия")

if __name__ == "__main__":
    main()