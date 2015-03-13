import select
import sys

from .nodes_base import BaseReEmitter, BaseEmitter


class BaseIONode:

    READERS = set()
    WRITERS = set()
    ERROR = set()

    def _add_reader(self, file_object):
        __class__.READERS.add(file_object)

    def _add_writer(self, file_object):
        __class__.WRITERS.add(file_object)

    def _select(self):
        return select.select(
            __class__.READERS, __class__.WRITERS, __class__.ERROR
        )


class BaseFileWriter(BaseReEmitter, BaseIONode):

    def _prepare_function(self, function):
        _, writers, *_ = self._select()
        if self._file_object in writers:
            return lambda arg: function(arg) and None
        else:
            return lambda arg: None

    def __init__(self, file_object):
        self._file_object = file_object
        self._add_writer(self._file_object)
        super().__init__(self._file_object.write)


class BaseFileReader(BaseEmitter, BaseIONode):

    def _build_emitter(self, file_object):
        def _generator():
            while True:
                readers, *_ = self._select()
                if file_object in readers:
                    line = file_object.readline()
                    if not line:
                        file_object.close()
                        self.mainloop.sources.remove(self)
                    yield line

        return _generator()

    def __init__(self, file_object):
        self._file_object = file_object
        self._add_reader(self._file_object)
        super().__init__(file_object)


class StdOut(BaseFileWriter):

    def __init__(self):
        super().__init__(sys.stdout)


class StdIn(BaseFileReader):

    def __init__(self):
        super().__init__(sys.stdin)


class FSFileWriter(BaseFileWriter):

    def __init__(self, path):
        super().__init__(open(path, 'w'))


class FSFileReader(BaseFileReader):

    def __init__(self, path):
        super().__init__(open(path, 'r'))
