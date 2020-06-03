##multiple inheritance
from math import sqrt,factorial

class arith_calc:
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2

    def result(self):
        if (self.num1 < self.num2):
            self.num1,self.num2 = self.num2,self.num1
        print('{} + {}'.format(self.num1,self.num2),' = ',(self.num1+self.num2))
        print('{} - {}'.format(self.num1, self.num2), ' = ', (self.num1 - self.num2))
        print('{} * {}'.format(self.num1, self.num2), ' = ', (self.num1 * self.num2))
        print('{} / {}'.format(self.num1, self.num2), ' = ', (self.num1 / self.num2))
        print('{} % {}'.format(self.num1, self.num2), ' = ', (self.num1 % self.num2))

class sqrt_cal:
    def __init__(self, num):
        self.num = num

    def result(self):
        print('Square root of {}'.format(self.num), ' is ', (sqrt(self.num)))

class fact_calc(sqrt_cal,arith_calc):
    def __init__(self,f_num,num,num1,num2):
        super().__init__(num)
        arith_calc.__init__(self,num1,num2)  ## exclusively called constructor.
        self.f_num = f_num

    def result(self):
        ##super().result_su1()
        arith_calc.result(self)
        super().result()
        print('Factorial of {} is'.format(self.f_num), factorial(f_num))

print('Enter two number on which you want to perform arithmetic operation::')
num1 = int(input('Number 1: '))
num2 = int(input('Number 2: '))

num = int(input('Enter number to calculate square root: '))
f_num = int(input('Enter number to calculate factorial: '))

print ()
print('The result is below: ')
#fc = fact_calc(f_num,num)   ## example of method order resolution- same method name: result,_init_()
fc = fact_calc(f_num,num,num1,num2)
fc.result()


