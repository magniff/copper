from copper import IteratorBasedSource, Filter, Apply, StdOut, mainloop


source = IteratorBasedSource(iter(range(10)))
source >> Filter(lambda x: x % 2) >> Apply(lambda x: x**2) >> StdOut()

mainloop.run(source)
