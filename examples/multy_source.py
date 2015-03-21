from copper import (
    Apply, Bundle, IteratorBasedSource, OutLines, StdOut, mainloop
)


sources = [
    IteratorBasedSource(gen) for gen in
    (
        ('item %s from iter0' % n for n in range(5)),
        ('item %s from iter1' % n for n in range(5)),
        ('item %s from iter2' % n for n in range(5)),
    )
]

Bundle(sink=Apply(lambda line: 'data: '+line), *sources) >> OutLines()

mainloop.run(*sources)
