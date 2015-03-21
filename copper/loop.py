from collections import deque


class LoopMeta(type):

    def __new__(cls, name, bases, attrs):
        loop = super().__new__(cls, name, bases, attrs)

        loop._is_running = False
        if not attrs.get('BASE'):
            loop._queue = deque()

        return loop


class Mainloop(metaclass=LoopMeta):

    @classmethod
    def add(cls, pipe_cell, message):
        cls._queue.append((pipe_cell, message))

    @classmethod
    def wake_sources(cls):
        for source in cls.sources:
            source.emit()

        return bool(cls.sources)

    @classmethod
    def run(cls, *source_list):
        cls.sources = list(source_list)
        cls.wake_sources()

        cls._is_running = True
        while cls._is_running:

            while cls._queue:
                task, value = cls._queue.popleft()
                task.coroutine.send(value)

            cls._is_running = cls.wake_sources()
