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

class Library(Book):
    def __init__(self, books, title):
        self.books = books
        self.title = title

    
    if books is []:
        return ValueError("There needs to be at least one book in library")
    