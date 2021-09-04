import csv
import sys

try:
    input_file = sys.argv[1]
    with open(input_file, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        L = []
        for row in csv_reader:
            L.append(row)
        for D in L:
            print(D)
    csv_file.close()
except IOError as e:
    print('File error')
    print(e)
