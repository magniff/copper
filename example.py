from time import sleep
from copper import Source, Filter, Printer, Apply


def numbers():
    n = 0
    while 1:
        yield n
        sleep(0.01)
        n += 1


def is_prime(n):
    i, j = 2, 0
    while i ** 2 <= n and j != 1:
        if n % i == 0:
            j = 1
        i += 1
    return j != 1


def sum_digits(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s


#dummy data emitter
source = Source(numbers())

# now 'primes' is a stream of prime numbers
primes = source >> Filter(is_prime)

# this stream contains sums of digits of prime numbers
digit_sums = primes >> Apply(sum_digits)

# lets classify them )
digit_sums >> Filter(lambda x: x%2) >> Printer('not even sum:')
digit_sums >> Filter(lambda x: not x%2) >> Printer('even sum')
digit_sums >> Filter(is_prime) >> Printer('prime sum')

source.emit()
