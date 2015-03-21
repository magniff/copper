from .pipeline import Apply


def OutLines(writer_object):
    def _line_maker(line):
        if isinstance(line, str) and line.endswith('\n'):
            return line
        else:
            return '%s\n' % line

    line_maker = Apply(_line_maker)
    line_maker >> writer_object
    return line_maker


def Bundle(*nodes, sink):
    for node in nodes:
        node >> sink

    return sink
