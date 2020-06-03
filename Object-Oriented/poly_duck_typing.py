#class sparrow:
 #   def fly(self):
  #      print('Sparrows flies')

#class eagle:
 #   def fly(self):
  #      print('Eagle Flies')

#class dog:
 #   def bark(self):
  #      print('Dog can\'t fly. It barks')

#for obj in sparrow(),eagle(),dog():
 #   obj.fly()                         ## it gives attributeerror for dog()

class Pycharm:
    def execute(self):
        print('Compiling')
        print('Running')

class MyEditor:
    def execute(self):
        print('Spell Check')
        print('convention check')
        print('Compiling')
        print('Running')

class Laptop:
    def code(self,ide):
        ide.execute()

#ide = Pycharm();    ##we can create Pycharm object as well because it has execute() method in it.
ide = MyEditor()
lap1 = Laptop()
lap1.code(ide)


