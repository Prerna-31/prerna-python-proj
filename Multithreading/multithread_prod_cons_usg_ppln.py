import logging
import threading as th
import random
import concurrent.futures as cf

class Pipeline:
    def __init__(self):
        self.message = 0
        self.producer_lock = th.Lock()  ## restricts producer to access message
        self.consumer_lock = th.Lock()  ## restricts consumer to access message
        self.consumer_lock.acquire()

    def get_message(self,name):
        logging.debug("%s: about to acquire getlock ", name)
        self.consumer_lock.acquire()
        logging.debug("%s: have getlock ", name)
        message = self.message
        logging.debug("%s: about to release setlock ", name)
        self.producer_lock.release()
        logging.debug("%s: setlock released ", name)
        return message

    def set_message(self, message, name):
        logging.debug("%s: about to acquire setlock ", name)
        self.producer_lock.acquire()
        logging.debug("%s: have setlock ", name)
        self.message = message
        logging.debug("%s: about to release getlock ", name)
        self.consumer_lock.release()
        logging.debug("%s: getlock released", name)



SENTINEL = object()
#flag = False  # we can use flag as well to just consumer let know that producer finished reading data from the network

def producer(pipeline):
    ## Pretending that we are getting message from network
    for index in range(10):
        message = random.randint(1,101)
        logging.info("Producer got message: %s", message)
        pipeline.set_message(message, "Producer")

    pipeline.set_message(SENTINEL, "Producer") ##Send a sentinel message to consumer stating we are done.
    #flag = True
    #pipeline.set_message(flag, "Producer")


def consumer(pipeline):
    ##Pretending the we are saving a no. of messages in db
    message = 0
    while message is not SENTINEL:
    #while message is not flag:
        message = pipeline.get_message("Consumer")
        if message is not SENTINEL:
        #if message is not flag:
            logging.info("Consumer storing message: %s", message)
    logging.info("Consumer got message: %s", message)

if __name__ == "__main__":
    format = "%(asctime)s : %(message)s"
    logging.basicConfig(format = format, level=logging.INFO,datefmt="%H:%M:%S")
    #logging.getLogger().setLevel(logging.DEBUG)   ## it is responsible to print all the debug statements

    pipeline = Pipeline()
    with cf.ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(producer,pipeline)
        executor.submit(consumer,pipeline)