"""
This code recursively calculates factorial for each nubmer from inp stream.
Implements following stream:

source ----> _factorial ---> filter0 ---> filter1 ---> Unpack ---> Print
                  ^                   |
                  |                   |
                  --------------------

"""

import os
import sys
sys.path.insert(0, os.path.abspath('.'))

from copper import Source, Filter, Printer, Apply, mainloop


def inp():
    for i in range(10):
        yield (i+1, 1, 1)


source = Source(inp())
_factorial = Apply(lambda value: (value[0], value[1]+1, value[2]*value[1]))
source >> _factorial
factorial = _factorial >> Filter(lambda x: x[1] <= x[0]) >> _factorial
factorial >> Filter(lambda x: x[1] > x[0]) >> Apply(lambda x: x[2]) >> Printer('factorial')

mainloop.run()
