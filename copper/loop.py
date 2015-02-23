from collections import deque
from .exceptions import SourceDepleted


class Mainloop:

    _queue = deque()
    _is_running = True

    @classmethod
    def register_source(cls, source):
        cls.source = source

    @classmethod
    def run(cls):
        cls.source.emit()

        while cls._is_running:
            while cls._queue:
                pipe, message = cls._queue.popleft()
                result = pipe.func(message)
                if pipe.cond(result):
                    for sink in pipe.sinks:
                        sink.send(result)

            try:
                cls.source.emit()
            except SourceDepleted as e:
                cls._is_running = False
                print(e.value)

    @classmethod
    def add(cls, pipe_cell, message):
        cls._queue.append((pipe_cell, message))
