#!/usr/bin/python3
"""This is a library Module"""


class Book:
    def __init__(self, title, author, isbn, is_checked_out):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_checked_out = is_checked_out

    def checkout(self, is_checked_out):
        if is_checked_out:
            return("book is not available")
        is_checked_out = true
        return("book is checked out")
    
    def return_book(self):
        if is_checked_out:
            is_checked_out = false
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
            print(f"{book.title}, by {book.author}")

    book1 = Book("Croma Venture", "Joel Shepard", 1234, False )
    book2 = Book("Kite Runner", "Khaled Hosseini", 5678, False)
    book3 = Book("Brutal Prince", "Sophie Lark", 91011, False)
    book4 = Book("Aftershocks", "Marko Kloos", 1231, True)
    L = Library()
    L.add_book(book1)
    L.add_book(book2)
    L.add_book(book3)
    L.add_book(book4)