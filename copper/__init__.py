from .pipe import PipelineCell
from .source import Source


class Apply(PipelineCell):
    def __init__(self, func):
        super().__init__(func=func, cond=lambda x: True)


class Filter(PipelineCell):
    def __init__(self, cond):
        super().__init__(cond=cond, func=lambda x: x)


class Printer(PipelineCell):
    def __init__(self, msg):
        super().__init__(func=lambda x: print(msg, x), cond=lambda x: True)
