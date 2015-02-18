from collections import deque
from concurrent.futures import ThreadPoolExecutor


pool = ThreadPoolExecutor(2)


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


class Corutine:

    MAX_QUEUE = 10

    def send(self, item):
        if len(self.queue) < __class__.MAX_QUEUE:
            self.queue.append(item)

        if not self.handler.gi_running:
            self.handler.send(self.queue.popleft())

    def close(self):
        self.handler.close()

    def __init__(self, func, cond, sink):
        self.queue = deque()
        self.handler = task_handler(func, cond, sink)


class Source:

    def __init__(self, iterator):
        self._iterator = iterator
        self._sink = list()

    def __rshift__(self, other):
        if isinstance(other, __class__):
            self._sink.append(other._get_coroutine())
            return other
        else:
            raise RuntimeError(
                'Object %s should be an instance of %s' % (
                    other, __class__.__name__
                )
            )

    def _close_sink(self):
        for treater in self._sink:
            treater.close()

    def emit(self):
        for item in self._iterator:
            for treater in self._sink:
                treater.send(item)

        self._close_sink()


class PipelineCell(Source):

    def _get_coroutine(self):
        return Corutine(self._func, self._cond, self._sink)

    def __init__(self, func, cond):
        self._sink = list()
        self._cond = cond
        self._func = func
