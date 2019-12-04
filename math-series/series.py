def fibonacci(num):
    return sum_series(num)

def lucas(num):
    return sum_series(num, 2)

def sum_series(num, a=0, b=1):
    if num == 0:
        return a

    if num == 1:
        return b

    if num < 2:
        return num

    for i in range(2, num + 1):
        c = a + b
        a = b
        b = c

    return c


