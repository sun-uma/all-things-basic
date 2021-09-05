import math
import sys


def integer(n: int, b: int) -> str:
    if n < b:
        if n > 9:
            return str(mapping[n])
        else:
            return str(n)
    mod = n % b
    if mod > 9:
        mod = mapping[mod]
    return integer(n // b, b) + str(mod)


def fraction(n: float, b: int) -> str:
    if n == 0:
        return '0'
    n = n * b
    i = math.floor(n)
    d = n - i
    if i > 9:
        i = mapping[i]
    return str(i) + fraction(d, b)


def print_result (neg: bool, int_value: int, fract: float, base: int):
    result = ''
    if neg:
        result += '-'
    result += integer(int_value, base)
    if not fract == 0:
        result += '.' + fraction(fract, base)
    print(result)


try:
    n = float(sys.argv[1])
    mapping = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    neg = False
    if n < 0:
        neg = True
    n = abs(n)
    int_value = math.floor(n)
    fract = n - int_value
    print('Binary: ', end="")
    print_result(neg, int_value, fract, 2)
    print('Octal: ', end="")
    print_result(neg, int_value, fract, 8)
    print('Hexadecimal: ', end="")
    print_result(neg, int_value, fract, 16)

except ValueError as v:
    print("Invalid values!")
    print(v)

except IndexError as i:
    print("Arguments not found!")
    print(i)
