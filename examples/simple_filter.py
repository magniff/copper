from copper import IteratorBasedSource, Filter, Apply, StdOut, mainloop


source = IteratorBasedSource(iter(range(10)))
source >> StdOut()

mainloop.run(source)
