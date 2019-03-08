import time
from functools import wraps


def run_time(func):
    @wraps(func)
    def inner(*args, **kwargs):
        start_time = time.time()
        data = func(*args, **kwargs)
        print()
        stop_time = time.time()
        print('{0}:{1}'.format(func.__name__, round((stop_time - start_time), 2)))
        return data

    return inner


def type_limit(*typeLimit, **returnLimit):
    def warp(func):
        @wraps(func)
        def inner(*ar, **kw):
            length = len(typeLimit)
            for index in range(length):
                if not isinstance(type(ar[index]), typeLimit[index]):
                    raise TypeError('类型错误')
            run = func(*ar, **kw)
            if 'returnLimit' in returnLimit:
                limit = returnLimit["returnLimit"]
                if not isinstance(run, limit):
                    raise TypeError('这个函数必须返回一个{0}类型的返回值,但现在返回的是{1}类型'.format(limit, type(run)))
            return run

        return inner

    return warp


if __name__ == "__main__":
    type_limit(3, 4)
