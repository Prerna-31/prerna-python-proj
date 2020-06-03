import threading as th
import logging as log
import concurrent.futures as cf
import time


class FakeDatabase:
    def __init__(self):
        self.value = 0
        self.lck = th.Lock()

    def update(self,th_name):
        log.info("Thread %s , starting update ", th_name)
        log.info("Thread %s about to lock ", th_name)
        with self.lck:
            log.info("Thread %s has lock ", th_name)
            local_copy = self.value   ##simulating reading from DB
            local_copy +=1            ##simulating processing rows fetched from DB
            time.sleep(0.1)
            self.value = local_copy   ##simulating updating DB
            log.info("Thread %s about to release lock ", th_name)
        log.info("Thread %s after release ", th_name)
        log.info("Thread %s , finishing update ", th_name)

if __name__ == "__main__":
    format = "%(asctime)s --> %(message)s"
    log.basicConfig(format = format,level=log.INFO, datefmt="%H:%M:%S")
    db = FakeDatabase()
    log.info("testing update. starting value is %d. ", db.value)
    with cf.ThreadPoolExecutor(max_workers=2) as exe:
        for index in range(2):
            exe.submit(db.update,index)
    log.info("testing update. Ending value is %d. ", db.value)