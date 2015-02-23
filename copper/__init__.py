from .pipeline import ProcessingNode, BaseSource
from .loop import Mainloop as mainloop
from .frontend import RShiftMixin


class ShiftableProcessingNode(ProcessingNode, RShiftMixin):
    """Add support for '>>' (as known as right shift) operator as pipe.
    """
    pass


class Apply(ShiftableProcessingNode):
    """Applyes function func to stream.
    """
    def __init__(self, func):
        super().__init__(func=func, cond=lambda x: True)


class Filter(ShiftableProcessingNode):
    """Filters stream by predicate cond
    """
    def __init__(self, cond):
        super().__init__(cond=cond, func=lambda x: x)


class Printer(ShiftableProcessingNode):
    """Writes stream to console.
    Should be done as subclass of File?
    """
    def __init__(self, msg):
        super().__init__(func=lambda x: print(msg, x), cond=lambda x: True)


class File(ShiftableProcessingNode):
    """Writes stream to file.
    """
    def __init__(self, filename, buff_len=1):
        self._buffer = []

        def _dump_to_file(value):
            if len(self._buffer) <= buff_len:
                self._buffer.append(value)
            else:
                with open(filename, 'a') as f:
                    f.write('\n'.join(map(str, self._buffer)))

                self._buffer = []

        super().__init__(func=_dump_to_file, cond=lambda x: True)


class Source(ShiftableProcessingNode):
    """Wrap your data stream iterator with Source to be able to use pipes.
    """
    pass
