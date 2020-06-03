lst = [4,8,12,98,50]

it = iter(lst)
print('Iterator Values: without for loop - ')
print(it.__next__())
print(it.__next__())
print(next(it))
print('Iterator Values: with for loop - ')
for i in it:
    print(i)

## User-defined iterator
class iterSeq:
    def __init__(self):
        self.x = 1

    def __iter__(self):
        #self.x = 1       ## u can initialise it when u are not using init method.
        return self

    def __next__(self):
        if self.x <= 10:
            num = self.x
            self.x+=1
            return num
        else:
            raise StopIteration


it = iterSeq()
#it.__iter__()
print('User-defined Iterator Values: without for loop - ')
print(it.__next__())
print(next(it))

print('User-defined Iterator Values: with for loop - ')
for i in it:
    print(i)