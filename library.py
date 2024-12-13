from abc import ABC, abstractmethod
from typing import List
import logging

# Налаштування логування
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

# Клас для зберігання інформації про книгу
class Book:
    def __init__(self, title: str, author: str, year: int) -> None:
        self.title: str = title
        self.author: str = author
        self.year: int = year

    def display_info(self) -> None:
        logging.info(f"Назва: {self.title}")
        logging.info(f"Автор: {self.author}")
        logging.info(f"Рік видання: {self.year}")

    def __str__(self) -> str:
        return f"'{self.title}' by {self.author} ({self.year})"


# Абстрактний клас, визначає методи для роботи над бібліотекою
class LibraryInterface(ABC):
    @abstractmethod
    def add_book(self, book: Book) -> None:
        pass

    @abstractmethod
    def remove_book(self, title: str) -> None:
        pass

    @abstractmethod
    def show_books(self) -> None:
        pass


# Клас Library для управління колекцією книг
class Library(LibraryInterface):
    def __init__(self) -> None:
        self.books: List[Book] = []

    def add_book(self, book: Book) -> None:
        self.books.append(book)
        logging.info(f"Book '{book.title}' added to the library.")

    def remove_book(self, title: str) -> None:
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                logging.info(f"Book '{title}' removed from the library.")
                return
        logging.info(f"Book '{title}' not found in the library.")

    def show_books(self) -> None:
        if not self.books:
            logging.info("The library is empty.")
        else:
            for book in self.books:
                logging.info(book)


# Відповідає за управління бібліотекою
class LibraryManager:
    def __init__(self, library: LibraryInterface) -> None:
        self.library: LibraryInterface = library

    def add_book(self, title: str, author: str, year: int) -> None:
        book = Book(title, author, year)
        self.library.add_book(book)

    def remove_book(self, title: str) -> None:
        self.library.remove_book(title)

    def show_books(self) -> None:
        self.library.show_books()


# Функція для взаємодії з користувачем
def main() -> None:
    library = Library()
    manager = LibraryManager(library)

    while True:
        command: str = (
            input("Enter command (add, remove, show, exit): ").strip().lower()
        )

        match command:
            case "add":
                title: str = input("Enter book title: ").strip()
                author: str = input("Enter book author: ").strip()
                year_input: str = input("Enter book year: ").strip()

                try:
                    year: int = int(year_input)
                    manager.add_book(title, author, year)
                except ValueError:
                    logging.info("Invalid year. Please enter a valid integer for the year.")
            case "remove":
                title: str = input("Enter book title to remove: ").strip()
                manager.remove_book(title)
            case "show":
                manager.show_books()
            case "exit":
                confirm = input("Are you sure you want to exit? (yes/no): ").strip().lower()
                if confirm == "yes":
                    logging.info("Goodbye!")
                    break
                else:
                     logging.info("Exit cancelled. Continuing...")

            case _:
                logging.warning("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
