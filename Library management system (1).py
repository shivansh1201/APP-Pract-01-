class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False

    def borrow(self):
        if self.is_borrowed:
            print(f'"{self.title}" is already borrowed.')
            return False
        self.is_borrowed = True
        return True

    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed = False
            return True
        return False


class Patron:
    def __init__(self, name, patron_id):
        self.name = name
        self.patron_id = patron_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.borrow():
            self.borrowed_books.append(book)
            print(f"{self.name} borrowed '{book.title}'.")

    def return_book(self, book):
        if book in self.borrowed_books:
            if book.return_book():
                self.borrowed_books.remove(book)
                print(f"{self.name} returned '{book.title}'.")
        else:
            print(f"{self.name} has not borrowed '{book.title}'.")


class Library:
    def __init__(self):
        self.books = []
        self.patrons = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added to library.")

    def register_patron(self, patron):
        self.patrons.append(patron)
        print(f"Patron '{patron.name}' registered.")

    def borrow_book(self, patron_id, isbn):
        patron = next((p for p in self.patrons if p.patron_id == patron_id), None)
        book = next((b for b in self.books if b.isbn == isbn), None)
        if patron and book:
            patron.borrow_book(book)
        else:
            print("Patron or Book not found.")

    def return_book(self, patron_id, isbn):
        patron = next((p for p in self.patrons if p.patron_id == patron_id), None)
        book = next((b for b in self.books if b.isbn == isbn), None)
        if patron and book:
            patron.return_book(book)
        else:
            print("Patron or Book not found.")

    def display_information(self):
        print("\n----- Library Books -----")
        for book in self.books:
            status = "Borrowed" if book.is_borrowed else "Available"
            print(f"{book.title} | {book.author} | {book.isbn} | {status}")

        print("\n----- Patrons -----")
        for patron in self.patrons:
            print(f"{patron.name} ({patron.patron_id})")
            if patron.borrowed_books:
                for book in patron.borrowed_books:
                    print("  -", book.title)
            else:
                print("  No borrowed books")


library = Library()

book1 = Book("Python Basics", "John", "101")
book2 = Book("Data Structures", "Alice", "102")

library.add_book(book1)
library.add_book(book2)

patron1 = Patron("Rahul", "P001")
patron2 = Patron("Priya", "P002")

library.register_patron(patron1)
library.register_patron(patron2)

library.borrow_book("P001", "101")
library.borrow_book("P002", "102")

library.return_book("P001", "101")

library.display_information()
