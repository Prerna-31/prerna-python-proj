##Iterator containing power of 2 upto 10.
class iter_sqr:
    def __init__(self):
        self.x = 0
        self.limit = 10

    def __iter__(self):
        return self

    def __next__(self):#next(self):
        if self.x <= self.limit:
            num = self.x
            sq = 2**(self.x)
            self.x += 1
            return sq
        else:
           raise StopIteration

it = iter_sqr()
for i in it:
    print(i)