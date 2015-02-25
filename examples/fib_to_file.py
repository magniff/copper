"""
This code produces a stream of fibonacci numbers and dumps it into file.
Implements following stream:

source --------> fib ---> Delay ----> Apply0 ---> File
                  ^               |
                  |               |
                   ---------------
note: this works quite fast, so keep an eye on yours hd free space :)
"""

from copper import Source, FileWriter, Apply, mainloop


def inp():
    yield (1, 1)


source = Source(inp())
fib = Apply(lambda x: (x[1], x[0]+x[1]))
source >> fib

fib >> fib
fib_stream = fib >> Apply(lambda x: x[0]) >> FileWriter('fib.txt')


mainloop.run(source)
