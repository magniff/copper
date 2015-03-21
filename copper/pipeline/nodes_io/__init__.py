import sys

from .base import BaseFileReader, BaseFileWriter


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
