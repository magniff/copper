from select import select

from ..nodes_base import BaseReEmitter, BaseEmitter


class BaseIOMixin:

    READERS = set()
    WRITERS = set()
    ERROR = set()

    def _add_reader(self, file_object):
        __class__.READERS.add(file_object)

    def _add_writer(self, file_object):
        __class__.WRITERS.add(file_object)

    def _select(self):
        return select(__class__.READERS, __class__.WRITERS, __class__.ERROR)


class BaseFileWriter(BaseReEmitter, BaseIOMixin):

    def _prepare_function(self, function):
        def _writer(arg):
            _, writers, *_ = self._select()
            return function(arg) if self._file_object in writers else None

        return _writer

    def __init__(self, file_object):
        self._file_object = file_object
        self._add_writer(self._file_object)
        super().__init__(self._file_object.write)


class BaseFileReader(BaseEmitter, BaseIOMixin):

    def _build_emitter(self, file_object):
        def _generator():
            while True:
                readers, *_ = self._select()

                # todo: fix 100% processor consumption when waiting stdin
                if file_object not in readers:
                    yield

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
