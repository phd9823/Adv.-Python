# Book Class
class Book:
    def __init__(self, id, title, author):
        self.id = id
        self.title = title
        self.author = author
        self.available = True

# Patron Class
class Patron:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.borrowed = []

# Library Class
class Library:
    def __init__(self):
        self.books = {}
        self.patrons = {}

    def add_book(self, book):
        self.books[book.id] = book
        print("Book Added")

    def register_patron(self, patron):
        self.patrons[patron.id] = patron
        print("Patron Registered")

    def borrow_book(self, patron_id, book_id):
        if patron_id in self.patrons and book_id in self.books:
            book = self.books[book_id]
            patron = self.patrons[patron_id]

        if book.available:
            book.available = False
            patron.borrowed.append(book.title)
            print(patron.name, "borrowed", book.title)
        else:
            print("Book not available")

            print("Invalid ID")

    def return_book(self, patron_id, book_id):
        if patron_id in self.patrons and book_id in self.books:
            book = self.books[book_id]
            patron = self.patrons[patron_id]

        if book.available:
            book.available = False
            patron.borrowed.append(book.title)
            print(patron.name, "borrowed", book.title)
        else:
            print("Book not available")

            print("Invalid ID")
    def display_books(self):
        print("\nBooks in Library")
        for book in self.books.values():
            status = "Available" if book.available else "Borrowed"
            print(book.id, "-", book.title, "-", book.author, "-", status)

    def display_patrons(self):
        print("\nPatrons")
        for patron in self.patrons.values():
            print(patron.id, "-", patron.name, "- Borrowed Books:", patron.borrowed)


# Main Program
library = Library()

# Add Books
library.add_book(Book(101, "Python Programming", "Guido"))
library.add_book(Book(102, "Data Structures", "Mark"))
library.add_book(Book(103, "Machine Learning", "Andrew"))

# Register Patrons
library.register_patron(Patron(1, "Alice"))
library.register_patron(Patron(2, "Bob"))

# Display Books
library.display_books()

# Borrow Book
library.borrow_book(1, 101)

# Display Books
library.display_books()

# Return Book
library.return_book(1, 101)

# Display Books Again
library.display_books()

# Display Patrons
library.display_patrons()