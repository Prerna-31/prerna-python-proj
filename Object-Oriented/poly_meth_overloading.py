class Person:
    category = 'MALE'
    def __init__(self):
        self.name = 'Prerna'
        self.age = 26
        globals()['category'] = 'FEMALE'

    def show_detail(self):
        print('My name is ',self.name)
        print(self.category)

    def show_detail(self,cat):
        print('My name is ', self.name)
        print("My age is ", self.age)
        print("My gender is ",cat)

    def add(self,a=None, b=None, c=None):
        s=0
        if(a!=None and b!=None and c!=None):
            s=a+b+c
        elif(a!=None and b!=None):
            s=a+b
        else:
            s=a

        print(s)


p_obj1 = Person()

Person.category = 'Female'
p_obj1.show_detail(Person.category)  ##Method overloading cannot be done because it calls the last defined method and hence it throws typeerror in python.
p_obj1.add(5)