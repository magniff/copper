def coroutine(func):
    def _coroutine(*args, **kwargs):
        f = func(*args, **kwargs)
        next(f)
        return f

    return _coroutine


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


class PipelineCell(Source):
    def _get_coroutine(self):

        func = self._func
        cond = self._cond

        @coroutine
        def _handler():
            while True:
                item = yield

                for treater in self._sink:
                    cond(item) and treater.send(func(item))
                else:
                    func(item)

        return _handler()

    def __init__(self, func, cond):
        self._sink = list()
        self._cond = cond
        self._func = func


class Apply(PipelineCell):
    def __init__(self, func):
        super().__init__(func=func, cond=lambda x: True)


class Filter(PipelineCell):
    def __init__(self, cond):
        super().__init__(cond=cond, func=lambda x: x)


class Printer(PipelineCell):
    def __init__(self, msg):
        super().__init__(func=lambda x: print(msg, x), cond=lambda x: True)
