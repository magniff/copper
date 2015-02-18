from time import sleep
from copper import Source, Filter, Printer, Apply


def numbers():
    n = 0
    while 1:
        yield n
        n += 1


def delay(time):
    def _delay(x):
        sleep(time)
        return x

    return _delay


def is_prime(n):
    i, j = 2, 0
    while i ** 2 <= n and j != 1:
        if n % i == 0:
            j = 1
        i += 1
    return j != 1


source = Source(numbers())

source >> Apply(lambda x: x**2) >> Printer('pipe1')
source >> Apply(lambda x: x**3) >> Printer('pipe2')

source.emit()
