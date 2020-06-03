class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print('{0}\'s age is {1}'.format(self.name,self.age))


p_obj1 = Person('User1',26)
#Person.display(p_obj1)   ## this also works fine.
p_obj1.display()
p_obj2 = Person('User2',25)
#Person.display(p_obj2)
p_obj2.display()
