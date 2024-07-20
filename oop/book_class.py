class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        print(f"deleting {self.title}")

    def __str__(self):
        return f"Book('{self.title}', '{self.author}', published in {self.year})"
    
    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.year})"
    
# Example usage (uncomment to test)
# book1 = Book("The Great Gatsby", "F. Scott Fitzgerland", 1925)
# print(book1)
# print(repr(book1))
# del book1

from book_class import Book

def main():
    # Creating an instance of Book
    my_book = Book("1984", "George Orwell", 1949)

    # Demonstrating the __str__ method
    print(my_book)  # Expected to use __str__

    # Demonstrating the __repr__ method
    print(repr(my_book))  # Expected to use __repr__

    # Deleting a book instance to trigger __del__
    del my_book

if __name__ == "__main__":
    main()