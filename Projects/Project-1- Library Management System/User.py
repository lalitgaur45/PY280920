# -*- coding: utf-8 -*-

class User:
    def __init__(self, name, location, age, aadhar_id):
        self.name = name
        self.location = location
        self.age = age
        self.aadhar_id = aadhar_id
        self.issuedbook = {}
        

class Member(User):
    def __init__(self,name, location, age, aadhar_id,student_id):
        super().__init__(name, location, age, aadhar_id)
        self.student_id = student_id
        
    def __repr__(self):
        return self.name + ' ' + self.location + ' ' + self.student_id
    
    #assume name is unique
    def issueBook(self,bookname,catalog,days=10):
        book = catalog.searchByName(bookname.lower().strip())
        if book:
            if book.total_count > 0:
                book_item = book.book_item[0]
                self.issuedbook[bookname] = book_item
                book.removeBookItem(book_item)
                print("book issued")
            else:
                print("book not available")
        else:
            print("book not found")
    
    #assume name is unique
    def returnBook(self,bookname,catalog):
        if bookname in self.issuedbook:
            book_item = self.issuedbook[bookname]
            book = catalog.searchByName(bookname.lower().strip())
            if book:
                catalog.addBookItem(book,book_item.isbn,book_item.rack)
                print("book has been returned")
            else:
                print("This book is not exist")
        else:
            print("Not have this book")




        
        
class Librarian(User):
    def __init__(self,name, location, age, aadhar_id,emp_id):
        super().__init__(name, location, age, aadhar_id)
        self.emp_id = emp_id
        
    def __repr__(self):
        return self.name + self.location + self.emp_id
    
    def addBook(self,name,author,publish_date,pages,catalog):
        return catalog.addBook(name,author,publish_date,pages)


    def addBookItem(self, book, isbn, rack):
        book.addBookItem(isbn, rack)

    def removeBook(self,name,catalog):
        catalog.removeBook(name)
    
    def removeBookItemFromCatalog(self,bookname,isbn,catalog):
        catalog.removeBookItem(bookname,isbn)
    
    
        