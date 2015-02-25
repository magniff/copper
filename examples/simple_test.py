from copper import Source, Printer, Apply, mainloop


source = Source(iter(range(10)))
source >> Printer()

mainloop.run()
