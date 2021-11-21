import time


def my_timer(func):

    def wrapper(*args, **kwargs):
        print(f"my_time started with {func.__name__}")

        start_time = time.time()
        result = func(*args, **kwargs)

        print(f"my_time finished: {time.time()-start_time}")
        return result

    return wrapper