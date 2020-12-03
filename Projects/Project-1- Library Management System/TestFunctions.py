# -*- coding: utf-8 -*-
from Book import Book
from Catalog import Catalog
from User import Member, Librarian

# b1 = Book('Shoe Dog','Phil Knight', '2015',312)
# b1.addBookItem('123hg','H1B2')
# b1.addBookItem('124hg','H1B3')

# b1.printBook()

# catalog = Catalog()

# b = catalog.addBook('Shoe Dog', 'Phil Knight', '2015', 312)
# catalog.addBookItem(b, '123hg', 'H1B2')
# catalog.addBookItem(b, '124hg', 'H1B4')
# catalog.addBookItem(b, '125hg', 'H1B5')
#
# b = catalog.addBook('Moonwalking with Einstien', 'J Foer', '2017', 318)
# catalog.addBookItem(b, '463hg', 'K1B2')
#
# catalog.displayAllBooks()
#
# m = Member("Vish", "Bangalore", 23, 'asljlkj22', 'std1233')
# m.issueBook('Shoe Dog')
# print(m1.issuedbook)
#
# librarian = Librarian("Awantik", "Bangalore", 34, 'asljlkj22', 'zeke101')
# print(m)
# print(librarian)
#
# b = catalog.searchByName('Shoe Dog')
# print("here")
# print(b)
#
# catalog.removeBookItem('Shoe Dog', '124hg')
# catalog.displayAllBooks()


# m1.issueBook
catalog = Catalog()
b1 = catalog.addBook("manish autobiography", "manish saini", '2020', 300)
b2 = catalog.addBook("sahil autobiography", "sahil khatri", '2019', 350)

# one way of doing of adding bookitem
b1.addBookItem('jhg876', 'B2')
b1.addBookItem('jhg876', 'B1')
b1.addBookItem('jhg876', 'B8')
# another way of doing of adding bookitem
catalog.addBookItem(b2, 'JKL123', 'A1')
catalog.addBookItem(b2, 'JKL123', 'A2')

catalog.displayAllBooks()

m1 = Member('Lalit','delhi','30','456789','12345')
print(m1)

m1.issueBook('manish autobiography',catalog)
m1.issueBook('sahil autobiography',catalog)
print(m1.issuedbook)

catalog.displayAllBooks()

m1.returnBook('manish autobiography',catalog)

catalog.displayAllBooks()

l = Librarian('deepak','haryana','26','654123','98732')
b3 = l.addBook('jack n jill','poppet','28/11/2020',180,catalog)
l.addBookItem(b3,'mnp876','C3')
l.addBookItem(b3,'mnp876','C6')
l.addBookItem(b3,'mnp876','C4')

catalog.displayAllBooks()

l.removeBookItemFromCatalog('sahil autobiography','JKL123',catalog)
l.removeBookItemFromCatalog('manish autobiography','jhg786',catalog)

catalog.displayAllBooks()

l.removeBook('jack n jill',catalog)

catalog.displayAllBooks()