import threading
import logging
import time

def thread_task(name):
    logging.info("Thread %s: starting",name)
    time.sleep(2)
    logging.info("Thread %s: finishing",name)

if __name__ == "__main__":
    format = "%(asctime)s --> %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,datefmt="%H:%M:%S")
    logging.info("Main : before creating thread")
    t1 = threading.Thread(target=thread_task,args=(1,), daemon=True)
    logging.info("Main : before running thread %s",threading.get_ident())
    t1.start()
    logging.info("Main : wait for the thread to finish")
    t1.join()
    logging.info("Main : all done")