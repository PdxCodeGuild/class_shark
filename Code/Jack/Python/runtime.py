from time import clock


def get_runtime(fn):
    def timer(*args, **kwargs):
        start = clock()
        result = fn(*args, **kwargs)
        print(f'Completed {fn.__name__} in {clock() - start} s')
        return result

    return timer
