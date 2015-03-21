from copper import IteratorBasedSource, Apply, Filter, OutLines, mainloop


source = IteratorBasedSource(range(100))
source >> Apply(lambda x: x**2+1) >> Filter(lambda x: x % 7) >> OutLines()

mainloop.run(source)
