import time, random, threading


def worker(job_list: list):
    print(f"{threading.current_thread().name} started.")

    for i in job_list:
        print(f"{threading.current_thread().name} working on: {i}")
        time.sleep(random.randint(1, 10))

    print(f"{threading.current_thread().name} finished.")


name_list = ["robert", "csaba", "tamás", "csilla"]
t1 = threading.Thread(target=worker, args=[name_list])

photo_list = ["photo1.jpg", "photo2.jpg", "photo3.jpg", "photo4.jpg"]
t2 = threading.Thread(target=worker, args=[photo_list])

t1.start()
t2.start()

print("Program finished")