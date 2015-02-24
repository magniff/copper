def fib():
    a, b = 1, 1
    while 1:
        yield a
        a, b = b, a+b


buffer = []
for i in fib():
    if len(buffer) <= 1000:
        buffer.append(i)
    else:
        with open('fib.txt', 'a') as f:
            f.write('\n'.join(map(str, buffer)))

        buffer = []
