from copper import Source, Filter, Printer


def numbers():
    n = 0
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


source = Source(numbers())

pipe0 = source >> Filter(is_prime)
source.run()
