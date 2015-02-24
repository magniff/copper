"""
This is simple example of streaming to file.
Use pipe node File.
"""

from copper import Source, File, mainloop


source = Source(iter(range(100)))
source >> File('data.txt')
mainloop.run()
