import time


def run_time(func):
    def inner(*args, **kwargs):
        start_time = time.time()
        data = func(*args, **kwargs)
        print()
        stop_time = time.time()
        print('{0}>>>running_time:{1}'.format(func.__name__, stop_time - start_time))
        return data

    return inner
