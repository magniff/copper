"""
This code produces a stream of fibonacci numbers.
Implements following stream:

source --------> fib ---> Delay ----> Apply0 ---> Print
                  ^               |
                  |               |
                  ----------------

Note, that extra delay applied.
"""

import time
from copper import Source, Printer, Apply, mainloop


def delay(t):
    def _delay(x):
        time.sleep(t)
        return x
    return _delay


def inp():
    yield (1, 1)


source = Source(inp())
fib = Apply(lambda x: (x[1], x[0]+x[1]))
source >> fib
fib >> Apply(delay(0.2)) >> fib
fib_ready = fib >> Apply(lambda x: x[1])
fib_ready >> Printer()

mainloop.run(source)
