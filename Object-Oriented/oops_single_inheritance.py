##Single inheritance
from math import sqrt
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

class sqrt_cal(arith_calc):
    def __init__(self, num, num1, num2):
        super().__init__(num1,num2)
        self.num = num

    def result(self):
        super().result()
        print('Square root of {}'.format(self.num), ' is ', (sqrt(self.num)))


print('Enter two number on which you want to perform operation::')
num1 = int(input('Number 1: '))
num2 = int(input('Number 2: '))
ac = arith_calc(num1,num2)
#ac.result()

num = int(input('Enter number to calculate square root: '))

sc = sqrt_cal(num,num1,num2)
#sc = sqrt_cal(num)
sc.result()

