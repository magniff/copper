"""
This code produces a stream of fibonacci numbers.
Implements following stream:

source --------> fib ---> Delay ----> Apply0 ---> Print
                  ^               |
                  |               |
                  ----------------

Note, that extra delay applied.
"""

from copper import Source, StdOut, mainloop


source = Source(iter(range(10)))
source >> StdOut()

mainloop.run(source)
