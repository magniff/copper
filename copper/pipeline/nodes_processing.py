from ..common import coroutine
from .nodes_base import BaseProcessingNode


class PathThroughNode(BaseProcessingNode):
    def _prepare_function(self, function):
        return function


class FSM(BaseProcessingNode):

    def fsm_callback(self, value):
        self._fsm_data = value

    def _prepare_function(self, fsm_coroutine):
        fsm_coroutine = coroutine(fsm_coroutine)(self.fsm_callback)

        def _handler(value):
            self._fsm_data = None
            fsm_coroutine.send(value)

            if self._fsm_data is not None:
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
