"""
This code recursively calculates factorial for each nubmer from inp stream.
Implements following stream:

source ----> _factorial ---> filter0 ---> filter1 ---> Unpack ---> StdOut
                  ^                   |
                  |                   |
                  --------------------

"""
from copper import IteratorBasedSource, Filter, StdOut, Apply, mainloop


source = IteratorBasedSource(((i+1, 1, 1) for i in range(100)))

_factorial = Apply(lambda value: (value[0], value[1]+1, value[2]*value[1]))
source >> _factorial
factorial = _factorial >> Filter(lambda x: x[1] <= x[0]) >> _factorial
factorial >> Filter(lambda x: x[1] > x[0]) >> Apply(lambda x: x[2]) >> Apply(lambda line: str(line)+ '\n') >> StdOut()

mainloop.run(source)
