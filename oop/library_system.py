# Define the base class Book
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"Book: {self.title} by {self.author}"

# Define the derived class EBook
class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"

# Define the derived class PrintBook
class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"

# Define the Library class demonstrating composition
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        for book in self.books:
            print(book)

from library_system import Book, EBook, PrintBook, Library

def main():
    # Create a library instance
    library = Library()

    # Create instances of Book, EBook, and PrintBook
    book1 = Book("Pride and Prejudice", "Jane Austen")
    ebook1 = EBook("Snow Crash", "Neal Stephenson", 500)
    print_book1 = PrintBook("The Catcher in the Rye", "J.D. Salinger", 234)

    # Add books to the library
    library.add_book(book1)
    library.add_book(ebook1)
    library.add_book(print_book1)

    # List all books in the library
    print("Books in the library:")
    library.list_books()

if __name__ == "__main__":
    main()

