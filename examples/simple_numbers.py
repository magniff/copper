from copper import IteratorBasedSource, Apply, OutLines, mainloop


source = IteratorBasedSource(range(1, 4))
source >> Apply(lambda x: x**2) >> OutLines()

mainloop.run(source)
