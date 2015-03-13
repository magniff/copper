"""
This is simple example of streaming to file.
Use pipe node File.
"""

from copper import IteratorBasedSource, FSFileWriter, mainloop


source = IteratorBasedSource(iter(range(100)))
source >> FSFileWriter('data.txt')
mainloop.run(source)
