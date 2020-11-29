# -*- coding: utf-8 -*-
from Book import Book


# First Book is file & second is Class

class Catalog:
    def __init__(self):
        self.different_book_count = 0
        self.books = []

    # Only available to admin
    def addBook(self, name, author, publish_date, pages):
        b = Book(name, author, publish_date, pages)
        self.different_book_count += 1
        self.books.append(b)
        return b

    def removeBook(self,name):
        book = self.searchByName(name)
        if book:
            self.books.remove(book)

    # Only available to admin
    def addBookItem(self, book, isbn, rack):
        book.addBookItem(isbn, rack)

    def searchByName(self, name):
        for book in self.books:
            if name.strip() == book.name:
                return book

    def searchByAuthor(self, author):
        author_not_found = True
        for book in self.books:
            if book.author.lower() == author.lower():
                book.printBook()
                author_not_found = False
        if author_not_found :
            print("author not found")

    def displayAllBooks(self):
        print('Different Book Count', self.different_book_count)
        c = 0
        for book in self.books:
            c += book.total_count
            book.printBook()

        print('Total Book Count', c)

    def removeBookItem(self, name, isbn):
        book = self.searchByName(name)
        book_item = book.searchBookItem(isbn)
        book.removeBookItem(book_item)
