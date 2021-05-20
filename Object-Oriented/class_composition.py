"""Inheritance: why Bad"""
"""In the below example, conceptually, all books are bookshelf but vice-versa is not true sounds logically bad
Secondly, technically, we are not using any method of the parent class so inheritance is not required"""
class Bookshelf:
    def __init__(self, quantity):
        self.quantity = quantity

    def __str__(self):
        return f"bookshelf has {self.quantity} books"

class Book(Bookshelf):
    def __init__(self, name, quantity):
        super().__init__(quantity)
        self.name = name

    def __str__(self):
        return f"{self.name}"

print("Inheritance Example")
print("=========================")
book1 = Book("Harry Potter", 120)
book2 = Book("PYTHON 101",60)
print(book1)
print(book2)

print()

"""Class Composition: why Good"""
"""In the below example, conceptually, bookshelf contains many books which sounds logically good"""
class Bookshelf:
    def __init__(self, *books):
        self.books = books

    def __str__(self):
        return f"bookshelf has {len(self.books)} books"

class Book:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"{self.name}"

print("Class Composition Example")
print("=========================")
book1 = Book("Harry Potter")
book2 = Book("PYTHON 101")
shelf = Bookshelf(book1, book2)
print(shelf)
print(f"{book1}, {book2}")