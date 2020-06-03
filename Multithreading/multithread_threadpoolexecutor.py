#import threading
import logging
import time
import concurrent.futures as cf

def thread_task(name):
    logging.info("Thread %s: starting",name)
    time.sleep(2)
    logging.info("Thread %s: finishing",name)

if __name__ == "__main__":
    format = "%(asctime)s --> %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,datefmt="%H:%M:%S")

### Using threadpoolexecutor to create a pool of threads
    with cf.ThreadPoolExecutor(max_workers=3) as executor:
        for index in range(3):
            executor.submit(thread_task,index)   ## can't directly pass range into the function
           # executor.map(thread_task,range(3))  ## can directly pass range into the function


### Using list to create a pool of threads
   # threads = list()
   # for index in range(3):
    #    logging.info("Main : create and start thread %d",index)
     #   t = threading.Thread(target=thread_task,args=(index,))
      #  threads.append(t)
       # t.start()
    #t1 = threading.Thread(target=thread_task,args=(1,), daemon=True)

   # for index,thread in enumerate(threads):
    #    logging.info("Main : before joining thread %d ",index)
     #   thread.join()
      #  logging.info("Main : thread %d  done", index)
