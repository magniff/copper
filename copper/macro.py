from .pipeline import Apply, StdOut


def OutLines(writer_object=None, prefix=''):
    writer_object = writer_object or StdOut()

    def _line_maker(line):
        if isinstance(line, str) and line.endswith('\n'):
            return prefix + line
        else:
            return prefix + '%s\n' % line

    line_maker = Apply(_line_maker)
    line_maker >> writer_object
    return line_maker


def Bundle(*nodes, sink):
    for node in nodes:
        node >> sink

    return sink
