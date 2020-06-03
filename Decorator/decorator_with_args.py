def decorator_maker(d_args1,d_args2,d_args3):
    def decorator1(func):
        def inner_fun(f_args1,f_args2,f_args3):
            print('Decorator arguments: ',d_args1,d_args2,d_args3)
            print('Inner function arguments: ',f_args1,f_args2,f_args3)
            func(f_args1,f_args2,f_args3)
        return inner_fun
    return decorator1

#@decorator_maker('Prerna','Aziz','Chirag')
def funct(args1,args2,args3):
    print('Functions arguments : ', args1,args2,args3)

#funct('Papa','Mummy','bachhe')

res = decorator_maker('User1','User2','User3')
res1 = res(funct)
res1(12,13,14)