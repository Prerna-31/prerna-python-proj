class TooManyPagesToReadError(ValueError):
    pass

class book:
    def __init__(self,name, page_cnt:int):
        self.name = name
        self.page_cnt = page_cnt
        self.readPages = 0

    def __repr__(self):
        return (f"The {self.name} has {self.page_cnt} pages")

    def readBook(self, Pages:int):
        self.readPages += Pages
        if(self.readPages > self.page_cnt):
            raise TooManyPagesToReadError(f"You have tried to read {self.readPages} pages but {self.name} has {self.page_cnt} pages. ")
        return (f"you have read {self.readPages} out of {self.page_cnt} in {self.name} book")

book1 = book("Harry Potter", 600)
book2 = book("Python 101", 120)
print(book1)
try:
    print(book1.readBook(300))
    print(book1.readBook(350))
    print(book2.readBook(20))
except TooManyPagesToReadError as e:
    print(e)

