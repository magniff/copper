from .loop import Mainloop as mainloop
from .exceptions import SourceDepleted


class BasePipelineNode:

    def add_sink(self, sink):
        if not isinstance(sink, ProcessingNode):
            raise RuntimeError(
                'Object %s must be an instance of ProcessingNode.'
            )

        self.sinks.append(sink)
        return sink

    def close_sinks(self):
        for sink in self.sinks:
            sink.close()

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

    def send(self, message):
        self.mainloop.add(self, message)

    def __init__(self, func, cond):
        super().__init__()
        self.func = func
        self.cond = cond
