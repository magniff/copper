#! /usr/bin/env python

import sys
from copper import FSFileReader, StdOut, mainloop


source = FSFileReader(sys.argv[1])
source >> StdOut()

mainloop.run(source)
