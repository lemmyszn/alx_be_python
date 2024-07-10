class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        return not self._is_checked_out

from library_management import Book

class Library:
    def __init__(self):
        self._books = []

    def add_book(self, title, author):
        new_book = Book(title, author)
        self._books.append(new_book)

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                return True
        return False

    def return_book(self, title):
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                return True
        return False

    def list_available_books(self):
        available_books = [book for book in self._books if book.is_available()]
        if available_books:
            for book in available_books:
                print(f"Title: {book.title}, Author: {book.author}")
        else:
            print("No available books.")

from library_management import Library

def main():
    # Create a library
    library = Library()

    # Add books to the library
    library.add_book("The Great Gatsby", "F. Scott Fitzgerald")
    library.add_book("1984", "George Orwell")
    library.add_book("To Kill a Mockingbird", "Harper Lee")

    # List available books
    print("Available books:")
    library.list_available_books()
    print()

    # Check out a book
    if library.check_out_book("1984"):
        print("Checked out '1984'.")
    else:
        print("'1984' is not available.")
    print()

    # List available books after checking out '1984'
    print("Available books after checkout:")
    library.list_available_books()
    print()

    # Return the book
    if library.return_book("1984"):
        print("Returned '1984'.")
    else:
        print("'1984' was not checked out.")
    print()

    # List available books after returning '1984'
    print("Available books after return:")
    library.list_available_books()

if __name__ == "__main__":
    main()
