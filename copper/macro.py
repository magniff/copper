from .pipeline import Apply, StdOut, FSM


def SplitBy(delimeter):

    def split_coro(callback):
        sequence = []
        while 1:
            value = yield
            if value != delimeter:
                sequence.append(value)
            elif value == delimeter:
                if sequence:
                    callback(tuple(sequence))
                    sequence = []
                else:
                    continue

    return FSM(split_coro)


def OutLines(klass=StdOut):
    def _line_maker(line):
        if isinstance(line, str) and line.endswith('\n'):
            return line
        else:
            return str(line) + '\n'

    line_maker = Apply(_line_maker)
    line_maker >> klass()
    return line_maker
