from copper import Source, Filter, Printer, Apply, mainloop


def nums():
    n=0
    while 1:
        yield n
        n += 1


def is_prime(n):
    i, j = 2, 0
    while i ** 2 <= n and j != 1:
        if n % i == 0:
            j = 1
        i += 1
    return j != 1


source = Source(nums())
stream0_squares = source.add_sink(Apply(lambda x: x**2))
stream0_cubes = source.add_sink(Apply(lambda x: x**2))

source.add_sink(Printer('origin'))
stream0_squares.add_sink(Printer('squares'))
stream0_cubes.add_sink(Printer('cubes'))

mainloop.run()
