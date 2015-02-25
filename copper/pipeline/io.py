import select
import sys
from .base import BaseProcessingNode


class _WriterMixin:

    def _prepare_function(self, function):
        _, writers, *_ = self._select()
        if self._file_object in writers:
            return lambda arg: function('%s\n' % arg) and None
        else:
            return lambda arg: None


class _ReaderMixin:

    def _prepare_function(self, function):
        readers, *_ = self._select()
        if self._file_object in readers:
            return function
        else:
            return lambda arg: None


class BaseIONode(BaseProcessingNode):

    read = set()
    write = set()
    err = set()

    def _add_reader(self, file_object):
        __class__.read.add(file_object)

    def _add_writer(self, file_object):
        __class__.write.add(file_object)

    def _select(self):
        return select.select(__class__.read, __class__.write, __class__.err)


class StdOut(BaseIONode, _WriterMixin):

    def __init__(self):
        self._file_object = sys.stdout
        self._add_writer(self._file_object)
        super().__init__(self._file_object.write)


class StdIn(BaseIONode, _ReaderMixin):

    def __init__(self):
        self._file_object = sys.stdin
        self._add_reader(self._file_object)
        super().__init__(self._file_object.read)


class FileWriter(BaseIONode, _WriterMixin):

    def __init__(self, path):
        self._file_object = open(path, 'w')
        self._add_writer(self._file_object)
        super().__init__(self._file_object.write)
