from collections import deque
from .common import task_handler
from .source import Source


class Coroutine:

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


class PipelineCell(Source):

    def _get_coroutine(self):
        return Coroutine(self._func, self._cond, self._sink)

    def __init__(self, func, cond):
        self._sink = list()
        self._cond = cond
        self._func = func
