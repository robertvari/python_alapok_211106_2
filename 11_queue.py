from utilities.file_utils import get_files
import time, random, threading, queue

job_list = queue.Queue()

file_list = get_files(r"C:\Work\_PythonSuli\pycore-211106\photos")

# [job_list.put(i) for i in file_list]

for file in file_list:
    job_list.put(file)


def worker():
    print(f"{threading.current_thread().name} started.")

    while not job_list.empty():
        next_job = job_list.get()
        print(f"{threading.current_thread().name} working on {next_job}")
        time.sleep(random.randint(1, 10))

    print(f"{threading.current_thread().name} finished.")