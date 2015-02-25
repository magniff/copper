"""
This is simple example of streaming to file.
Use pipe node File.
"""

from copper import Source, FileWriter, mainloop


source = Source(iter(range(100)))
source >> FileWriter('data.txt')
mainloop.run(source)
