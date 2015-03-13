"""
This code produces a stream of fibonacci numbers and dumps it into file.
Implements following stream:

source --------> fib ----> Unpack ---> FSFileWriter
                  ^    |           |
                  |    |           |
                   ----             ----> StdOut
note: this works quite fast, so keep an eye on yours hd free space :)
"""

from copper import IteratorBasedSource, FSFileWriter, Apply, mainloop


def inp():
    yield (1, 1)


source = IteratorBasedSource(inp())

fib = Apply(lambda x: (x[1], x[0]+x[1]))
source >> fib

fib >> fib
fib_stream = fib >> Apply(lambda x: x[0])

fib_stream >> FSFileWriter('fib.txt')


mainloop.run(source)
