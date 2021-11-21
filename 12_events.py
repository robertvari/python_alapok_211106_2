import time, threading


downloading = threading.Event()


def downloader_worker():
    print("Downloading started...")
    time.sleep(3)
    print("Download finished")

    downloading.set()


def file_worker():
    downloading.wait()

    print("file_worker started")
    time.sleep(3)
    print("file_worker finished")


t1 = threading.Thread(target=downloader_worker)
t2 = threading.Thread(target=file_worker)

t1.start()
t2.start()