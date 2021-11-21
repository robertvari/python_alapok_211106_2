import time, random, threading


def worker1():
    print("worker1 started.")
    time.sleep(random.randint(10, 30))
    print("worker1 finished.")


def worker2():
    print("worker2 started.")
    time.sleep(random.randint(10, 30))
    print("worker2 finished.")


t1 = threading.Thread(target=worker1)
t2 = threading.Thread(target=worker2)

t1.start()
t2.start()

print("Program finished")