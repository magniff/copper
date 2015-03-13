from copper import Source, Filter, Apply, StdOut, mainloop


source = Source(iter(range(10)))
source >> Filter(lambda x: x % 2) >> Apply(lambda x: x**2) >> StdOut()

mainloop.run(source)
