import time, random
from utilities.decorators import my_timer


@my_timer
def worker1():
    print("Worker1 started...")
    time.sleep(random.randint(1, 10))
    print("Worker1 finished!")


@my_timer
def worker2():
    print("Worker2 started...")
    time.sleep(random.randint(1, 10))
    print("Worker2 finished!")


@my_timer
def my_function():
    time.sleep(random.randint(1, 10))


# worker1()
# worker2()
my_function()