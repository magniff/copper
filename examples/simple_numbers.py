from copper import IteratorBasedSource, Apply, OutLines, StdOut, mainloop


source = IteratorBasedSource(range(1, 4))
source >> Apply(lambda x: x**2) >> OutLines(StdOut())

mainloop.run(source)
