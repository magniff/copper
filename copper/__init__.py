from .pipeline import ProcessingNode, Source
from .loop import Mainloop as mainloop


class Apply(ProcessingNode):
    def __init__(self, func):
        super().__init__(func=func, cond=lambda x: True)


class Filter(ProcessingNode):
    def __init__(self, cond):
        super().__init__(cond=cond, func=lambda x: x)


class Printer(ProcessingNode):
    def __init__(self, msg):
        super().__init__(func=lambda x: print(msg, x), cond=lambda x: True)
