def coroutine(func):
    def _coroutine(*args, **kwargs):
        _c = func(*args, **kwargs)
        next(_c)
        return _c

    return _coroutine
