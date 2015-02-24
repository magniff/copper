"""
This code produces a stream of fibonacci numbers and dumps it into file.
Implements following stream:

source --------> fib ---> Delay ----> Apply0 ---> File
                  ^               |
                  |               |
                   ---------------
note: this works quite fast, so keep an eye on yours hd free space :)
"""

from copper import Source, File, Apply, mainloop


def inp():
    yield (1, 1)


source = Source(inp())
fib = Apply(lambda x: (x[1], x[0]+x[1]))
source >> fib

fib >> fib
fib >> Apply(lambda x: x[1]) >> File('fib.txt', buff_len=1000)

mainloop.run()
