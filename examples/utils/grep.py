#! /usr/bin/env python

import re
import sys
from copper import StdOut, Filter, StdIn, mainloop


pattern = sys.argv[1].strip("'\"")
source = StdIn()
source >> Filter(lambda line: re.match(pattern, line)) >> StdOut()

mainloop.run(source)
