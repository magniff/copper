"""
This is simple example of streaming yo file.
Use pipe node File.
"""

import os
import sys
sys.path.insert(0, os.path.abspath('.'))

from copper import Source, File, mainloop


source = Source(iter(range(100)))
source >> File('data.txt')
mainloop.run()
