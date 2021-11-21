import time


def my_timer(func):

    def wrapper(*args, **kwargs):
        print(f"my_time started with {func.__name__}")

    return wrapper