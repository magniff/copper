from copper import IteratorBasedSource, StdOut, Apply, mainloop


def OutLines(klass):
    line_maker = Apply(lambda line: str(line)+'\n')
    line_maker >> klass()
    return line_maker


source = IteratorBasedSource(iter(range(10)))
source >> OutLines(StdOut)


mainloop.run(source)
