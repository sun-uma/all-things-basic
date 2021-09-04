import random
import time


def millerTest(d, n):
    a = 2 + random.randint(1, n - 4)

    x = pow(a, d, n)

    if x == 1 or x == n - 1:
        return True

    while d != n - 1:
        x = (x * x) % n
        d *= 2

        if x == 1:
            return False
        if x == n - 1:
            return True

    return False


def isPrime(n, k):
    # Corner cases
    if n <= 1 or n == 4:
        return False
    if n <= 3:
        return True

    d = n - 1
    while d % 2 == 0:
        d //= 2

    for i in range(k):
        if not millerTest(d, n):
            return False

    return True


k = 4

n = 0
while 1:
    if isPrime(n, k):
        print(n, end=" ")
        time.sleep(5)
    n += 1
