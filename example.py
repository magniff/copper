from time import sleep
from copper import Source, Filter, Printer, Apply


def numbers():
    n = 0
    while 1:
        yield n
        sleep(0.1)
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


#dummy data emitter
source = Source(numbers())

# Lets fork source
pipe0 = source >> Filter(lambda x: not x%7) >> Apply(lambda x: x**2)
pipe1 = source >> Apply(lambda x: x**3) >> Apply(lambda x: x+10)

# ok, lets pipe pipe1 object to Printer
pipe1 >> Printer('I am pipe1')

# lets fork pipe0
pipe0 >> Printer('I am pipe00')
pipe0 >> Apply(lambda x: x-3) >> Printer('I am pipe01')

source.emit()
