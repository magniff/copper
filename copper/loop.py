from collections import deque


class LoopMeta(type):

    def __new__(cls, name, bases, attrs):
        loop = super().__new__(cls, name, bases, attrs)

        loop._is_running = False
        if not attrs.get('BASE'):
            loop._queue = deque()

        return loop


class BaseMainloop(metaclass=LoopMeta):

    BASE = True

    @classmethod
    def add(cls, pipe_cell, message):
        cls._queue.append((pipe_cell, message))

    @classmethod
    def run(cls):
        cls._is_running = True



class Mainloop(BaseMainloop):

    @classmethod
    def run(cls, source):
        super().run()
        
        source.emit()
        while cls._is_running:

            while cls._queue:
                task, value = cls._queue.popleft()
                task.coroutine.send(value)

            source.emit()
