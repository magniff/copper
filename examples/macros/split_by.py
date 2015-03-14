from copper import StdIn, OutLines, SplitBy, mainloop


source = StdIn()
source >> SplitBy(' ') >> OutLines()

mainloop.run(source)
