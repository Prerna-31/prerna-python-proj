import logging
import queue
import threading as th
import random
import concurrent.futures as cf
import time

## Created a class Pipeline which is subclass of queue. so pipeline = queue
#class Pipeline(queue.Queue):
    #def __init__(self):
     #   super().__init__(maxsize=10)

    #def get_message(self,name):
     #   logging.debug("%s: about to get message from queue ", name)
      #  value = self.get()
       # logging.debug("%s: got %d from queue ",name,value)
        #return value

    #def set_message(self, value, name):
     #   logging.debug("%s: about to add message to queue ", name)
      #  self.put(value)
       # logging.debug("%s: added %d to queue ", name,value)


def producer(pipeline,event):
    ## Pretending that we are getting message from network
    while not event.is_set():
        message = random.randint(1,101)
        logging.info("Producer got message: %s", message)
       ## pipeline.set_message(message, "Producer")  ##pipeline class method; user defined
        pipeline.put(message)   ##queue inbuilt method

    logging.info("Producer received EXIT event. Exiting")

def consumer(pipeline,event):
    while not event.is_set() or not pipeline.empty():
       # message = pipeline.get_message("Consumer")   ##pipeline class method
        message=pipeline.get()    ##queue inbuilt method  :user defined
        logging.info("Consumer storing message: %s (queue size=%s)", message, pipeline.qsize())
    logging.info("Consumer received EXIT event. Exiting")

if __name__ == "__main__":
    format = "%(asctime)s : %(message)s"
    logging.basicConfig(format = format, level=logging.INFO,datefmt="%H:%M:%S")
   # logging.getLogger().setLevel(logging.DEBUG)

    #pipeline = Pipeline()

    ## Another way: Used directly queue rather than using inheritance concept(subclass of queue).
    pipeline = queue.Queue(maxsize=10)
    event = th.Event()
    with cf.ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(producer,pipeline,event)
        executor.submit(consumer,pipeline,event)

        time.sleep(0.1)
        logging.info("Main : about to set event")
        event.set()