"""
    threadingScript.py
    Threading in Python 3, utilising multiple Producers and Consumers feature.
    In object oriented design.
"""


# import the necessary modules
import threading
import time
import random
import queue


# create the producer class
class Producer:
    def __init__(self):
        self.products = ["magic wang", "hat", "overcoat", "trinkets"]  # sample products
        self.next = 0  # counter initialisation

    def run(self):
        """
        function that will run the producer.
        :param queue_: queue generated with queue module
        :return: None
        """
        global queue_
        while time.process_time() < 10:
            if self.next < time.process_time():
                item = self.products[random.randrange(len(self.products))]
                queue_.put(item)
                print(f"item added {item}")
                self.next += random.random()


class Consumer:
    def __init__(self):
        self.next = 0

    def run(self):
        global queue_
        while time.process_time() < 10:
            print(f"Queue size: {queue_.qsize()}")
            if self.next < time.process_time() and not queue_.empty():
                item = queue_.get()
                print(f"Processed: {item}")
                self.next += random.random()
            elif queue_.empty():
                print("waiting for the item to process...")


# initialise producer and consumer objects
def main():
    # queue_ = queue.Queue(10)
    producer1 = Producer()
    consumer1 = Consumer()

    produc_thread = threading.Thread(target=producer1.run, args=())
    consum_thread = threading.Thread(target=consumer1.run, args=())

    produc_thread.start()
    consum_thread.start()


# execute the script
if __name__ == "__main__":
    queue_ = queue.Queue(10)
    main()

# TODO : refactor the code for multiple producers and consumers.
