"""Wwhen class method is not acting as factory"""
class Book:
    types = ['Hardcover', 'Paperback']
    def __init__(self, name, type, weight):
        self.name = name
        self.type=type
        self.weight = weight

    def __str__(self):
        return f"{self.name},{self.type} weighing {self.weight}g"

print("Class without factory - Example")
print("=========================")
book1 = Book("Harry Potter", "hardcover", 600);  ## I dont want to provide "hardcover" or "paperback" to book class as there are only two possible values.
book2 = Book("Python 101","paperback", 120)
print(book1)
print(book2)

print()
"""When class method is acting as factory"""
class Book:
    types = ['Hardcopy', 'Paperback']
    def __init__(self, name, book_type,weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __str__(self):
        return f"{self.name},{self.types[0]} weighing {self.weight}g"

    @classmethod
    def hardcover(cls, name, weight):
        return cls(name, cls.types[0] , weight+100)  # it retuns book object so no need to create its instance.

    @classmethod
    def paperback(cls, name, weight):
        return cls(name, cls.types[1], weight)

print("Class with factory - Example")
print("=========================")
print(Book.hardcover("Harry Potter", 600))
print(Book.paperback("Python 101", 160))