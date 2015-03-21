from copper import IteratorBasedSource, Apply, Filter, OutLines, StdOut, mainloop


source = IteratorBasedSource(range(100))
source >> Apply(lambda x: x**2+1) >> Filter(lambda x: x % 7) >> OutLines(StdOut())

mainloop.run(source)
