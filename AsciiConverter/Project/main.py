import sys

try:
    c = sys.argv[1]
    print(ord(c))

except TypeError as t:
    print('Invalid type')
    print(t)
except IndexError as i:
    print("Arguments not found!")
    print(i)
except Exception as e:
    print(e)