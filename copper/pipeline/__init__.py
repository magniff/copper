from ..frontend import RShiftMixin
from .pipeline import PathThroughNode, FSMNode, coroutine
from .base import BaseSource


class Apply(PathThroughNode, RShiftMixin):
    """Applyes function to stream.
    """
    pass


class Filter(PathThroughNode, RShiftMixin):
    """Filters stream by predicate filter_pred
    """
    def __init__(self, filter_pred):
        super().__init__(lambda x: x if filter_pred(x) else None)


class Printer(PathThroughNode, RShiftMixin):
    """Writes stream to console.
    Should be done as subclass of File?
    """
    def __init__(self):
        super().__init__(function=print)


class File(PathThroughNode, RShiftMixin):
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

        super().__init__(function=_dump_to_file)


class FSM(FSMNode, RShiftMixin):
    pass


class Source(BaseSource, RShiftMixin):
    """Wrap your data stream iterator with Source to be able to use pipes.
    """
    pass
