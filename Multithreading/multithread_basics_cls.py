from threading import *
from time import sleep

class hello(Thread):
    def run(self):
        for i in range(5):
            print("HELLO")
            sleep(1)

class hi(Thread):
    def run(self):
        for i in range(5):
            print("HI")
            sleep(1)

t1 = hello()
t2 = hi()

t1.start()
sleep(0.2)
t2.start()

t1.join()
t2.join()


#t1.run()
#t2.run()

print('Bye')