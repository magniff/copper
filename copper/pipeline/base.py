from ..loop import Mainloop as mainloop
from ..common import coroutine


class BasePipelineNode:

    def add_sink(self, sink):
        if not isinstance(sink, __class__):
            raise TypeError(
                'Object %s must be an instance of ProcessingNode.' % sink
            )

        self.sinks.append(sink)
        return sink

    def __init__(self):
        self.sinks = []
        self.mainloop = mainloop


class BaseSource(BasePipelineNode):

    def emit(self):
        try:
            data_from_source = next(self.emitter)
        except StopIteration:
            mainloop._is_running = False
        else:
            for sink in self.sinks:
                sink.send(data_from_source)

    def __init__(self, iterator):
        super().__init__()
        self.emitter = iterator


class BaseProcessingNode(BasePipelineNode):

    def _prepare_function(self, function):
        return NotImplementedError('Implement method _prepare_function().')

    def _build_coroutine(self, function):
        function = self._prepare_function(function)

        @coroutine
        def _coroutine():
            while True:
                value = yield
                result = function(value)
                if result is not None:
                    for consumer in self.sinks:
                        consumer.send(result)

        return _coroutine()

    def send(self, value):
        self.mainloop.add(self, value)

    def __init__(self, function):
        super().__init__()
        self.coroutine = self._build_coroutine(function)