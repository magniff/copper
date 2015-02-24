"""
This code reads numbers from console and calculates their factorials.
Implements following stream:

console ----> _factorial ---> filter0 ---> filter1 ---> Unpack ---> Print
                  ^                   |
                  |                   |
                   -------------------
"""

import sys
from copper import Source, Printer, Filter, Apply, mainloop


def console():
    while 1:
        try:
            yield input('>> enter number: ')
        except EOFError:
            sys.exit()


source = Source(console())
factorial_input = source >> Apply(lambda x: (int(x), 1, 1))

_factorial = Apply(lambda value: (value[0], value[1]+1, value[2]*value[1]))
factorial_input >> _factorial
factorial = _factorial >> Filter(lambda x: x[1] <= x[0]) >> _factorial
factorial >> Filter(lambda x: x[1] > x[0]) >> Apply(lambda x: x[2]) >> Printer('factorial is:')

mainloop.run()
