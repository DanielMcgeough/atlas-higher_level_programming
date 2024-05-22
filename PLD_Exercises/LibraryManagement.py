#!/usr/bin/python3
"""This is a library Module"""


class Book:
    def __init__(self, title, author, isbn, is_checked_out):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_checked_out = is_checked_out

    def checkout(self):
        if self.is_checked_out:
            return("book is not available")
        self.is_checked_out = True
        return("book is checked out")
    
    def return_book(self):
        if self.is_checked_out:
            self.is_checked_out = False
            return("book is checked out")
        else:
             return("book is not checked out")


class Library:
    def __init__(self):
        self.books = []
    def add_book(self, book):
        self.books.append(book)
    def remove_book(self, book):
        self.books.remove(book)
    def find_book_by_title(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None
    def list_books(self):
        for book in self.books:
            print(f"{book.title} by {book.author}")
class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []
    def borrow_book(self, book):
        if not (book.is_checked_out):
            Book.checkout(book)
            self.borrowed_books.append(book)
    def return_book(self, book):
        if book.is_checked_out:
            book.return_book()
            self.borrowed_books.remove(book)
    def list_books(self):
        print(self.name, ":", sep="")
        for book in self.borrowed_books:
            print(book.title)

Jeremy = Member("Jeremy", 1)
Jaylen = Member("Jaylen", 4)
David = Member("David", 34)
Danny = Member("Danny", 17)

book1 = Book("Croma Venture", "Joel Shepard", 1234, False )
book2 = Book("Kite Runner", "Khaled Hosseini", 5678, False)
book3 = Book("Brutal Prince", "Sophie Lark", 91011, False)
book4 = Book("Aftershocks", "Marko Kloos", 1231, False)
L = Library()
L.add_book(book1)
L.add_book(book2)
L.add_book(book3)
L.add_book(book4)
L.list_books()
Kite = L.find_book_by_title("KIte RUnNer")
print(Kite.author)
Jeremy.borrow_book(book1)
Danny.borrow_book(book3)
Jaylen.borrow_book(L.find_book_by_title("Aftershocks"))
Jaylen.borrow_book(L.find_book_by_title("Kite Runner"))
Danny.list_books()
Jaylen.list_books()