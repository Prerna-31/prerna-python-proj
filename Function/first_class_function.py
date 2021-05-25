"""first example: Perform division"""
print("first example of first class function : Perform division")
print("=========================================================")
def divide(dividend, divisor):
    if(divisor == 0):
        raise ZeroDivisionError('Divisor cannot be 0.')
    return (dividend/divisor)

def calculator(*values, operator):
    if(len(values) > 2):
        raise ValueError('Too many values to pass to divide function')
    return operator(*values)

try:
    print(calculator(20,5, operator = divide))
    print(calculator(20, 0, operator=divide))
    print(calculator(20, 5, 30, operator=divide))
except ZeroDivisionError as z:
    print(z)
except ValueError as v:
    print(v)

print()

"""Second example: Search string in the database"""
from operator import itemgetter
print("Second example of first class function : Search person in the database")
print("======================================================================")
def search(sequence, expected, finder):
    for elem in sequence:
        if(finder(elem) == expected):
            return (f"The person ,{expected} , is present in the database")
    return (f"The Person, {expected}, is not present in the database")

friends = [{"name" : "Rolf smith" , "age": 23 , "gender'" : "Male"},
           {"name" : "Jossette Coven" , "age": 35 , "gender'" : "Female"},
           {"name" : "Steven Salvatore" , "age": 30 , "gender'" : "Male"}]

def find_string(friend):
    return(friend["name"])

print(search(friends,"Bob Smith", find_string))
print(search(friends,"Steven Salvatore", find_string))
print(search(friends,"Damon Salvatore", lambda friend:friend["name"]))  ## lambda function also can be used
print(search(friends,"Elena Gilbert", itemgetter("name")))