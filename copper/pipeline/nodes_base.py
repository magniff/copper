# this garanties that we are using correct mainloop
from copper import mainloop

from ..common import coroutine
from ..frontend import RShiftMixin


class BasePipelineNode(RShiftMixin):

    mainloop = mainloop

    def add_sink(self, sink):
        if not isinstance(sink, __class__):
            raise TypeError(
                'Object %s must be an instance of %s.' % (
                    sink, __class__.__name__
                )
            )

        self.sinks.append(sink)
        return sink

    def __init__(self):
        self.sinks = list()


class BaseEmitter(BasePipelineNode):

    def __init__(self, *args, **kwargs):
        super().__init__()
        self.emitter = self._build_emitter(*args, **kwargs)

    def emit(self):
        try:
            data_from_source = next(self.emitter)
        except StopIteration:
            self.mainloop.sources.remove(self)
        else:
            for sink in self.sinks:
                sink.send(data_from_source)


class BaseReEmitter(BasePipelineNode):

    def __init__(self, function):
        super().__init__()
        self.coroutine = self._build_coroutine(function)

    def _build_coroutine(self, function):
        function = self._prepare_function(function)

        @coroutine
        def _coroutine():
            while 1:
                result = function((yield))
                if result is None:
                    continue

                for consumer in self.sinks:
                    consumer.send(result)

        return _coroutine()

    def send(self, value):
        self.mainloop.add(self, value)
