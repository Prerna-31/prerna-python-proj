"""
Unpacked Positional Arguments:
"""

def mul(*args): ## Packing of positional arguments i.e it collects all the positional arguments in the form of tuple
    product = 1;
    for arg in args:
        product = product * arg
    return(product)

def sum_(args):  ## Collecting it as tuple
    return(sum(args))

def apply(*args, operator):   ## Packing of positional arguments i.e it collects all the positional arguments in the form of tuple
    if(operator == '*'):
        return mul(*args)  ## Unpacking the arsg(tuple) into individual elements.
    elif(operator == '+'):
        return sum_(args)  ## passing tuple as it is
    else:
        print("No valid operator has been passed to apply")

lst= [1,2,3,4,5]
print("Working of Unpacking positional arguments: ")
print("============================================")
print(f"Sum of list elements: {apply(*lst, operator='+')}")    ## Unpacking arguments : splitting collection(tuple,list etc) into individual elements.

print(f"Product of individual elements: {apply(1,2,3,4,5, operator='*')}")

"""
Unpacked Keyword/named Arguments:
"""
print()
print("Working of Unpacking keyword arguments: ")
print("============================================")
def named(**kwargs): ##Collecting multiple named parameters into single argument/dictionary
    print(kwargs)

def print_nicely(**kwargs): ## Collecting individual named arguments into dictionary.
    named(**kwargs)   ##splitting  dictionary into individual keyword arguments.
    for key, value in kwargs.items():
        print(f"{key} : {value}")

print("Example of packing named arguments: ")
named(name="Bob", age=48) ## Passing multiple named parameters

detail = {"NAME": "Arjun" , "AGE" : 30}

print("Example of unpacking named arguments: ")
print_nicely(**detail)   ##unpacking named parameters i.e. splitting  dictionary into individual keyword arguments.