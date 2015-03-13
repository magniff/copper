import select
import sys

from copper.pipeline.nodes_base import BaseProcessingNode


class BaseIONode(BaseProcessingNode):

    READERS = set()
    WRITERS = set()
    ERROR = set()

    def _add_reader(self, file_object):
        __class__.READERS.add(file_object)

    def _add_writer(self, file_object):
        __class__.WRITERS.add(file_object)

    def _select(self):
        return select.select(__class__.READERS, __class__.WRITERS, __class__.ERROR)


class BaseFileWriter(BaseIONode):

    def _prepare_function(self, function):
        _, writers, *_ = self._select()
        if self._file_object in writers:
            return lambda arg: function('%s\n' % arg) and None
        else:
            return lambda arg: None

    def __init__(self, file_object):
        self._file_object = file_object
        self._add_writer(self._file_object)
        super().__init__(self._file_object.write)


class BaseFileReader(BaseIONode):

    def _prepare_function(self, function):
        readers, *_ = self._select()
        if self._file_object in readers:
            return function
        else:
            return lambda arg: None

    def __init__(self):
        self._file_object = sys.stdin
        self._add_reader(self._file_object)
        super().__init__(self._file_object.read)


class StdOut(BaseFileWriter):

    def __init__(self):
        super().__init__(sys.stdout)


class StdIn(BaseFileReader):

    def __init__(self):
        super().__init__(sys.stdin)


class FSFileWriter(BaseFileWriter):

    def __init__(self, path):
        super().__init__(open(path, 'w'))
