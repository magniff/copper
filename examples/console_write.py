from copper import Source, StdOut, mainloop


source = Source(iter(range(10)))
source >> StdOut()

mainloop.run(source)
