from collections import deque


class Mainloop:

    _queue = deque()
    _is_running = True

    @classmethod
    def run(cls, source):
        source.emit()

        while cls._is_running:

            while cls._queue:
                task, value = cls._queue.popleft()
                task.coroutine.send(value)

            source.emit()

    @classmethod
    def add(cls, pipe_cell, message):
        cls._queue.append((pipe_cell, message))
