"""
This is simple example of streaming to file.
"""

from copper import IteratorBasedSource, OutLines, FSFileWriter, mainloop


source = IteratorBasedSource(iter(range(100)))
source >> OutLines(FSFileWriter('data.txt'))
mainloop.run(source)
