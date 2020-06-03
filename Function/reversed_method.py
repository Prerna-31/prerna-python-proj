## reversing all the sequences:
lst = [23,45,12,10,98,50]
print(lst)
print("Reversing the above sequences:::")

print("List: ",list(reversed(lst)))
print("Tuple: ",tuple(reversed(lst)))

def print_reverse(obj):
    for item in obj:
        print(item, end=" ")

tup = (23,45,12,10,98,50)
print("Tuple: ",end=" ")
print_reverse(reversed(tup))

print()
st = "Are you Mad"
print("String: ",end=" ")
print_reverse(reversed(st))

print()
print("Range: ",end=" ")
print_reverse(reversed(range(6)))

print()
set1 = {23,12,98,50,35}
print("The original set:", set1)
print("The reversed set: ", end="")
print(list(reversed(sorted(set1))))  ##always we have to sort it.

dic = {'Name':'Prerna','Age': 26 ,'Area':'Raebareli'}
print("The original dictionary: ",list(dic.items()))
print("The reversed dictionary: ", end="")
print_reverse(reversed(sorted(dic.items()))) ## always we have to sort it.
#print(list(reversed(sorted(dic.items()))))

print()
## Reversing sequence: for custom object having _reversed_()
print("Reversing using _reversed_")

class Data:
    def __init__(self,item):
        self.lst_item=item
    def __reversed__(self):
        return reversed(self.lst_item)

lst1 = ['aa','bb','ab','bc','cd']
print('The original list: ', lst1)
dt_obj = Data(lst1)
print('The reversed list: ', end="")
#print(list(reversed(dt_obj)))
print_reverse(reversed(dt_obj))

print()
##Reversing using object having sequence protocol::
print("Reversing using _len_ and _getitem_")
class MytuppleWrapper:
    t=()
    def __init__(self, tup):
        self.t = tup
    def __len__(self):
        return len(self.t)
    def __getitem__(self, index):
        return self.t[index]

mt = MytuppleWrapper(('aa','ab','cdef','abdf'))
print_reverse(reversed(mt))



