import time, logging
from datetime import datetime
import getpass


def my_timer(func):

    def wrapper(*args, **kwargs):
        print(f"my_time started with {func.__name__}")

        start_time = time.time()

        result = func(*args, **kwargs)

        print(f"my_time finished: {time.time()-start_time}")
        return result

    return wrapper


def my_logger(func):
    logging.basicConfig(filename=f"my_app.log", level=logging.INFO)

    def wrapper(*args, **kwargs):
        print(f"my_logger started")
        logging.info(f"{datetime.now()} User: {getpass.getuser()}. args: {args, kwargs}")

        result = func(*args, **kwargs)

        return result
    return wrapper