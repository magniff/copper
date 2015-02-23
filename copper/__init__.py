from .pipeline import ProcessingNode, BaseSource
from .loop import Mainloop as mainloop
from .frontend import RShiftMixin


class Apply(ProcessingNode, RShiftMixin):
    def __init__(self, func):
        super().__init__(func=func, cond=lambda x: True)


class Filter(ProcessingNode, RShiftMixin):
    def __init__(self, cond):
        super().__init__(cond=cond, func=lambda x: x)


class Printer(ProcessingNode, RShiftMixin):
    def __init__(self, msg):
        super().__init__(func=lambda x: print(msg, x), cond=lambda x: True)


class Source(BaseSource, RShiftMixin):
    pass
