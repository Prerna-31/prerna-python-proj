## modify the function display to print positional and keword arguments.
def gen_prps_decorator(func):
    def inner_fun(*args,**kwargs):
        if (args):
            print ('Positional arguments are : ',args)
        elif(kwargs):
            print ('Keyword arguments are : ',kwargs)
        else:
            print('No arguments has been passed: ')
        func(*args,**kwargs)
    return inner_fun

@gen_prps_decorator
def display(a,b):
    print('Totals: ',a+b)

##res = gen_prps_decorator(display)
##res(23,67)
display(23,67)

@gen_prps_decorator
def display():
    print('Nothing to display')

display()

@gen_prps_decorator
def display(**kwargs):
    print('Personal details : ')
    for i,j in kwargs.items():
        print(i,j)

display(name='User1', age=28)