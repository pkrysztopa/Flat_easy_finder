import time

def timethis(func):
    def inner(*args, **kwargs):
        t1 = time.time()
        result = func(*args, **kwargs)
        t2 = time.time()
        print(f'Czas wykonywania funkcji {func.__name__} to {t2 - t1}')
        return result
    return inner