from ..common import coroutine
from .nodes_base import BaseReEmitter


class PathThroughNode(BaseReEmitter):
    _prepare_function = lambda self, func: func


class FSM(BaseReEmitter):

    def fsm_callback(self, value):
        self._fsm_data = value

    # coro is genobject
    def _prepare_function(self, coro):
        fsm_coroutine = coroutine(coro)(self.fsm_callback)

        def _handler(value):
            self._fsm_data = None
            # this code changes self._fsm_data
            fsm_coroutine.send(value)

            return self._fsm_data

        return _handler

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._fsm_data = None


class Apply(PathThroughNode):
    """Applyes function to stream.
    """
    pass


class Filter(PathThroughNode):
    """Filters stream by predicate filter_pred
    """
    def __init__(self, filter_pred):
        super().__init__(lambda x: x if filter_pred(x) else None)
