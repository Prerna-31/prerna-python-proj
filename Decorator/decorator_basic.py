## The first way to use decorator::
def div(a,b):
    print (a/b)

def decorator_div(fun):
    def inner_fun(a,b):
        if a < b:
            a,b=b,a
        return fun(a,b)
    return inner_fun

res=decorator_div(div)
print('Enter numerator and denominator to perform division::')
num1 = int(input('Numerator ::'))
num2 = int(input('Denominator::'))
res(num1,num2)

## other way to use decorator::
#def decorator_div(func):
  #  def inner_fun(a,b):
    #    if a<b:
      #      a,b = b,a
        #func(a,b)
    #return inner_fun

#@decorator_div
#def div(a,b):
 #   print(a/b)

#print('Enter numerator and denominator to perform division::')
#num1 = int(input('Numerator ::'))
#num2 = int(input('Denominator::'))
#div(num1,num2)