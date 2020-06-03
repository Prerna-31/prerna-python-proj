# Use multiple decorators on the same function

def dec_split_name(func):
    def wrapper(name):
        nm_sp = func(name).split()
        print('Name after split :',nm_sp)
    return wrapper

def dec_uppercase(func):
    def inner(name):
       ## nm = func(name)
        ##upp_nm = nm.upper()
        upp_nm = func(name).upper()
        print('Name in upper case: ',upp_nm)
        return upp_nm
    return inner

@dec_split_name
@dec_uppercase
def display_string(name):
    print('User\'s name :', name)
    return name

name=input('Enter your name: ')
display_string(name)

## another way to use multiple decorators
#res = dec_split_name(dec_uppercase(display_string))
#res(name)