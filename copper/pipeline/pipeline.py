from ..common import coroutine
from .base import BaseProcessingNode


class PathThroughNode(BaseProcessingNode):
    def _prepare_function(self, function):
        return function


class FSMNode(BaseProcessingNode):

    @staticmethod
    def fsm_callback(value):
        print(value)

    def _prepare_function(self, fsm_coroutine):
        fsm_coroutine = coroutine(fsm_coroutine)(__class__.fsm_callback)

        def _handler(value):
            return fsm_coroutine.send(value)

        return _handler
