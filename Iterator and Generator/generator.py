##topten is a generator which generates square on demand
def topten():
    n = 1
    while n <= 10:
        sq = n*n
        yield sq
        n+=1

values = topten()
print(values.__next__())
print(values.__next__())
print('Before for loop: ')
for i in values:
    print(i)
