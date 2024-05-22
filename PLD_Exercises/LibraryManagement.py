#!/usr/bin/python3
"""This is a library Module"""


class Book(self):
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
    
    book1 = ("Croma Venture", "Joel Shepard", 1234, False )
    book2 = ("Kite Runner", "Khaled Hosseini", 5678, False)
    book3 = ("Brutal Prince", "Sophie Lark", 91011, False)
    book4 = ("Aftershokcs", "Marko Kloos", 1231, True)

class Library(self):
    books = list[Book] []
    def add_book(self, book):
        books.append(book)
    def remove_book(self, book):
        books.remove(book)
    def find_book_by_title(self, title)
        if book.title isinstance (title)
    if books is []:
        return ValueError("There needs to be at least one book in library")
    
    