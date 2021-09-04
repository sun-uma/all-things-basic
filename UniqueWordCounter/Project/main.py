import re
import sys

try:
    input_file = sys.argv[1]
    input_file = open(input_file, 'r')
    input_string = input_file.read()
    input_string = re.sub('[;.,&!?"&]', '', input_string)
    words = re.split('[ \n]', input_string)
    u_words = []
    for x in words:
        if x not in u_words:
            u_words.append(x)
    u_words.sort(key=len)
    input_file.close()
    output_file = open('output.txt', 'w')
    for x in u_words:
        output_file.write(x+" ")
        output_file.write(str(len(x))+'\n')
    output_file.close()

except IOError as e:
    print('File error')
    print(e)
