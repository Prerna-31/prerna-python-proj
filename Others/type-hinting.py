from typing import List #Tuple, Set etc.
class Book:
    types = ['Hardcopy', 'Paperback']
    def __init__(self, name:str, book_type:str,weight:int):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __str__(self):
        return f"{self.name},{self.types[0]} weighing {self.weight}g"

    @classmethod
    def hardcover(cls, name:str, weight:int) -> "Book": ##"Book" refers return type of hardcover method. We can't write Book without quotes
                                                       # because it is inside the same class(At this time, object has not been created). we can
                                                       # write object without quotes only if the returned object belong to other class.
        return cls(name, cls.types[0] , weight+100)

    @classmethod
    def paperback(cls, name:str, weight:int) -> "Book":
        return cls(name, cls.types[1], weight)

print(Book.hardcover("Harry Potter", 600))
print(Book.paperback("Python 101", 160))