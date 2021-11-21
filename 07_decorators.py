import time, random
from utilities.decorators import my_timer, my_logger


@my_logger
@my_timer
def worker1():
    time.sleep(random.randint(1, 10))


@my_logger
@my_timer
def worker2():
    time.sleep(random.randint(1, 10))


@my_logger
def say_hello(name):
    print(f"Hello {name}")

# worker1()
# worker2()

say_hello("Robert")