from utilities.file_utils import get_files
import time, random, threading, queue

job_list = queue.Queue()

file_list = get_files(r"C:\Work\_PythonSuli\pycore-211106\photos")

# [job_list.put(i) for i in file_list]

for file in file_list:
    job_list.put(file)