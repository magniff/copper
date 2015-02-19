class Source:

    def __init__(self, iterator):
        self._iterator = iterator
        self._sink = list()

    def __rshift__(self, other):
        if isinstance(other, __class__):
            self._sink.append(other._get_coroutine())
            return other
        else:
            raise RuntimeError(
                'Object %s should be an instance of %s' % (
                    other, __class__.__name__
                )
            )

    def _close_sink(self):
        for treater in self._sink:
            treater.close()

    def emit(self):
        for item in self._iterator:
            for treater in self._sink:
                treater.send(item)

        self._close_sink()
