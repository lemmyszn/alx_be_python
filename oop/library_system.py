# Define the base class Book
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"

# Define the derived class EBook
class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        return f"{self.title} by {self.author} [E-Book, File Size: {self.file_size} MB]"

# Define the derived class PrintBook
class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        return f"{self.title} by {self.author} [Print Book, Page Count: {self.page_count}]"

# Define the Library class demonstrating composition
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        for book in self.books:
            print(book)

# Example usage (uncomment to test)
# if __name__ == "__main__":
#     library = Library()
#     ebook = EBook("1984", "George Orwell", 2)
#     print_book = PrintBook("To Kill a Mockingbird", "Harper Lee", 336)
#     library.add_book(ebook)
#     library.add_book(print_book)
#     library.list_books()

from library_system import Book, EBook, PrintBook, Library

def main():
    # Create a library instance
    library = Library()

    # Create instances of EBook and PrintBook
    ebook1 = EBook("1984", "George Orwell", 2)
    print_book1 = PrintBook("To Kill a Mockingbird", "Harper Lee", 336)
    ebook2 = EBook("The Great Gatsby", "F. Scott Fitzgerald", 1)
    print_book2 = PrintBook("Moby Dick", "Herman Melville", 635)

    # Add books to the library
    library.add_book(ebook1)
    library.add_book(print_book1)
    library.add_book(ebook2)
    library.add_book(print_book2)

    # List all books in the library
    print("Books in the library:")
    library.list_books()

if __name__ == "__main__":
    main()
