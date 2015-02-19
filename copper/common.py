from concurrent.futures import ThreadPoolExecutor


pool = ThreadPoolExecutor(8)


def coroutine(func):
    def _coroutine(*args, **kwargs):
        f = func(*args, **kwargs)
        next(f)
        return f

    return _coroutine


@coroutine
def task_handler(func, cond, sink):

    def _callback(future):
        result = future.result()

        if cond(result):
            for treater in sink:
                treater.send(result)

    while True:
        item = yield
        future = pool.submit(func, item)
        future.add_done_callback(_callback)
