"""
This is simple example of streaming to file.
Use pipe node File.
"""

from copper import Source, FSFileWriter, mainloop


source = Source(iter(range(100)))
source >> FSFileWriter('data.txt')
mainloop.run(source)
