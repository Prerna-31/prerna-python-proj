import threading as th
import os
import time

def print_cube(num):
    print("Calculating cube is assigned to :", th.current_thread().name)
    print("Id of process running print_cube: ",os.getpid())
    print("Cube : {}".format(num*num*num))

def print_square(num):
    print("Calculating square is assigned to :", th.current_thread().name)
    print("Id of process running print_square: ", os.getpid())
    print("Square : {}".format(num*num))

if __name__ == "__main__":
    print("Id of process running print_main program: ", os.getpid())
    print("This is the :",th.main_thread().name)
    # t1 = threading.Thread(target=print_cube, args=(10,))
    #t2 = threading.Thread(target=print_square, args=(10,))
    t1 = th.Thread(target=print_cube, args=(10,), name='T1')
    t2 = th.Thread(target=print_square, args=(10,), name = 'T2')
    t1.start()
    time.sleep(0.2)
    t2.start()
    t1.join()
    t2.join()
    print("Done!!!!!")