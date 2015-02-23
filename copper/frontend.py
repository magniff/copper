class RShiftMixin:
    def __rshift__(self, other):
        return self.add_sink(other)
