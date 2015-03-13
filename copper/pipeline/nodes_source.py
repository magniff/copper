from .nodes_base import BaseEmitter


class IteratorBasedSource(BaseEmitter):
    def _build_emitter(self, iterator):
        return iter(iterator)
