import sys


def lcm(v1: int, v2: int) -> int:
    lcm_result = v1 * v2 // hcf(v1, v2)
    return lcm_result


def hcf(v1: int, v2: int) -> int:
    if v2 > v1:
        v1, v2 = v2, v1
    for x in range(v1 // 2, 1, -1):
        if v1 % x == 0 and v2 % x == 0:
            return x
    return 1


try:
    a = int(sys.argv[1])
    b = int(sys.argv[2])

    if a == 0 or b == 0:
        print('Undefined')

    else:
        a = abs(a)
        b = abs(b)
        choice = input('Enter hcf or lcm: ').lower().strip()
        if choice == "hcf":
            print(hcf(a, b))
        elif choice == "lcm":
            print(lcm(a, b))
        else:
            print('Invalid choice')

except IndexError as e:
    print('Terminal arguments not found')
    print(e)

except ValueError as v:
    print('Invalid values')
    print(v)
