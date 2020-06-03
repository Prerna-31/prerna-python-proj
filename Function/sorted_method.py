## using of sorted method with different sequence:
print("Sorting in ascending order:")
print("-------------------------------")
lst = [23,45,12,10,98,50]
print(sorted(lst))
tup = ('a','u','o','i','e')
print(sorted(tup))
st = {'a','u','o','i','e'}
print(sorted(st))
dic = {'a':97,'u':117,'o':112,'i':105,'e':101}
print(sorted(dic))
print()

## sort the sequence in descending order:
print("Sorting in descending order:")
print("-------------------------------")
st = {'a','u','o','i','e'}
print(sorted(st,reverse=True))
#print(sorted(st,reverse=False))
print()

## sort the sequence using key:
print("Sorting using key:")
print("---------------------")
lst1 = ['abc','ab','abcd','aa','ab']
print("Sorted list based on length:",sorted(lst1,key=len))

print('Sorted list basd on lowercase: ',sorted("This is my string to sort".split(),key=str.lower))

## key can take external data resource as well for sorting:
student = ['Dave','John','Jane']
st_dic = {'Dave':'C','John':'F','Jane':'A'}
print("Sorted using external data::",sorted(student, key=st_dic.__getitem__,reverse=True))

##using lambda function:
st_det = (('David',25,'C'),
          ('Alex',24,'A'),
          ('Karen',27,'B'),
         )
print("Sorted students based on grade:",sorted(st_det,key=lambda x: x[2]))

##using class object:
class Student:
    def __init__(self,name,age,grade):
        self.name=name
        self.age=age
        self.grade=grade

    def __repr__(self):
        return repr((self.name,self.age,self.grade))

list_st_obj = (
                Student('David',25,'B'),
                Student('Alex',24,'B'),
                Student('Karen',27,'A')
              )

print("Sorted students based on name:",sorted(list_st_obj,key=lambda st:st.name))

print()
## sorted using operator module:
import operator as opr
print("Sorted using operator module:")
print("----------------------------------")
print("Sorted students based on grade- sequence:::", sorted(st_det, key=opr.itemgetter(2))) ## for sequence:
print("Sorted students based on grade- class_obj::::",sorted(list_st_obj,key=opr.attrgetter('grade')))

##multi-level sorting = complex sorting
print()
print("Multi-level sorting::::::: sorted by age, and grade::")
print("-------------------------------------------------------")
print("The original student list::",list_st_obj)
s = sorted(list_st_obj, key=opr.attrgetter('age'))
print("Sorted students by age(asc) and grade (desc)::::",sorted(s, key=opr.attrgetter('grade'), reverse=True))

print()
## Alternative way of complex sorting:::
print("Alternative method::")
def multisort(xs,specs):
    for key,reverse in reversed(specs):
        xs.sort(key=opr.attrgetter(key), reverse=reverse)
    return xs

print("Multilevel - sorting using function:::",multisort(list(list_st_obj),(('grade',True),('age',False))))



