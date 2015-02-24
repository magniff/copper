from .common import coroutine
from .exceptions import SourceDepleted
from .loop import Mainloop as mainloop


class BasePipelineNode:

    def add_sink(self, sink):
        if not isinstance(sink, ProcessingNode):
            raise TypeError(
                'Object %s must be an instance of ProcessingNode.' % sink
            )

        self.sinks.append(sink._make_coroutine())
        return sink

    def __init__(self):
        self.sinks = []
        self.mainloop = mainloop


class BaseSource(BasePipelineNode):

    def __init__(self, iterator):
        super().__init__()
        self.mainloop.register_source(self)
        self.iterator = iterator

    def emit(self):
        try:
            new_value = next(self.iterator)
        except StopIteration:
            raise SourceDepleted()
        else:
            for sink in self.sinks:
                sink.send(new_value)


class ProcessingNode(BasePipelineNode):

    def _make_coroutine(self):

        @coroutine
        def _coroutine():
            func = self.function
            re_emit = self.reemit_condition
            consumers = self.sinks

            while True:
                value = yield
                result = func(value)

                if not re_emit(result):
                    continue

                for consumer in consumers:
                    self.mainloop.add(consumer, result)

        return _coroutine()

    def __init__(self, func, cond):
        super().__init__()
        self.function = func
        self.reemit_condition = cond
        self.coroutine = self._make_coroutine()
