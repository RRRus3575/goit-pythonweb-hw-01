from abc import ABC, abstractmethod

# Клас для зберігання інформації про книгу
class Book:
    def __init__(self, title, author, year, ):
        self.title = title
        self.author = author
        self.year = year
    
    def display_info(self):
        print(f"Назва: {self.title}")
        print(f"Автор: {self.author}")
        print(f"Рік видання: {self.year}")


    def __str__(self):
        return f"'{self.title}' by {self.author} ({self.year})"
    
# Абстрактний клас, визначає методи для роботи над бібліотекою
class LibraryInterface(ABC):
    @abstractmethod
    def add_book(self, book: Book):
        pass

    def remove_book(self, title):
        pass

    def show_book(self):
        pass

# Клас Library для управління колекцією книг
class Library(LibraryInterface):
    def __init__(self):
        self.books = []


    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added to the library.")

    def remove_book(self, title: str):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                print(f"Book '{title}' removed from the library.")
                return
        print(f"Book '{title}' not found in the library.")

    def show_books(self):
        if not self.books:
            print("The library is empty.")
        else:
            for book in self.books:
                print(book)

# Відповідає за управління бібліотекою
class LibraryManager:
    def __init__(self, library: LibraryInterface):
        self.library = library

    def add_book(self, title, author, year):
        book = Book(title, author, year)
        self.library.add_book(book)

    def remove_book(self, title):
        self.library.remove_book(title)

    def show_books(self):
        self.library.show_books()

# Функція для взаємодії з користувачем
def main():
    library = Library()
    manager = LibraryManager(library)

    while True:
        command = input("Enter command (add, remove, show, exit): ").strip().lower()

        match command:
            case "add":
                title = input("Enter book title: ").strip()
                author = input("Enter book author: ").strip()
                year = input("Enter book year: ").strip()
                manager.add_book(title, author, year)
            case "remove":
                title = input("Enter book title to remove: ").strip()
                manager.remove_book(title)
            case "show":
                manager.show_books()
            case "exit":
                print("Goodbye!")
                break
            case _:
                print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()