import time
import sys

try:

    input_text_file = sys.argv[1]
    input_file = open(input_text_file, 'r')
    contents = input_file.read()
    lines = contents.split(' ')
    print('\n\n', lines, '\n\n')
    vowels = ['a', 'e', 'i', 'o', 'u']
    words = []
    for line in lines:
        words_line = line.split(' ')
        for word in words_line:
            words.append(word)

    input_file.close()
    output_file = open('outputfile'+str(time.time())+'.txt', 'w')
    third_letter_counter = 0
    fifth_word_counter = 1
    blank_space = False

    for x in contents:
        if x.isspace():
            if not blank_space:
                output_file.write('-')
                blank_space = True
                third_letter_counter = 0
                fifth_word_counter += 1
        elif x == '\n':
            output_file.write(';')
            blank_space = False
        elif x in vowels:
            if not blank_space:
                output_file.write('-')
                blank_space = '-'
                third_letter_counter = 0
                fifth_word_counter += 1
        elif x.isalpha():
            if fifth_word_counter % 5 == 0:
                output_file.write(x.upper())
            elif third_letter_counter == 3:
                output_file.write(x.upper())
            else:
                output_file.write(x)
                third_letter_counter += 1
            blank_space = False

    output_file.close()

    # def alter_text(self):
    #     """
    #     This function reads the file contents and alters its contents.
    #     Unlike the other functions, alter text requires the data to
    #     retain newlines, spaces, and other special characters.
    #     """
    #     logging.info('Inside alter text method.')
    #     counter = 1
    #
    #     altered_text = ''
    #     sentences = self.raw_input.split('\n')
    #
    #     for sentence in sentences:
    #         words = sentence.split(' ')
    #
    #         # Splitting each word based on vowels.
    #         new_words = []
    #         for word in words:
    #             new_words += re.split('[aeiouAEIOU]', word)
    #
    #         # Capitalizing third letter and fifth word
    #         new_sentence = ''
    #         for index in range(len(new_words)):
    #             if len(new_words[index]) > 2:
    #                 new_words[index] = new_words[index][:2] \
    #                     + new_words[index][2].upper() + new_words[index][3:]
    #             if counter % 5 == 0:
    #                 new_words[index] = new_words[index].upper()
    #             counter += 1
    #
    #             # Replacing spaces with hyphens.
    #             new_sentence += new_words[index] + '-'
    #
    #         # Replacing new lines with semi-colons
    #         altered_text += new_sentence + ';'
    #
    #     logging.info('Altered text done successfully')
    #
    #     return altered_text

    to_prefix = 0
    ing_suffix = 0
    palindrome = []
    unique_words = []

    for word in words:
        if word[0:2] == 'To':
            to_prefix += 1
        if word[-3:] == 'ing':
            ing_suffix += 1
        if word[::-1] == word and word not in palindrome:
            palindrome.append(word)
        if word not in unique_words:
            unique_words.append(word)

    max_occur = 0
    max_word = ''

    for word in unique_words:
        count = words.count(word)
        if count > max_occur:
            max_occur = count
            max_word = word

    word_dict = {}
    for count, ele in enumerate(words, 1):
        word_dict[count] = ele

    print("Words having prefix 'To': ", to_prefix)
    print("Words having suffix 'ing':", ing_suffix)
    print("Word repeated maximum number of times: ", max_word)
    print("Words that are palindromes: ", end="")
    for word in palindrome:
        print(word, end=" ")
    print("\nUnique list of words: ")
    for word in unique_words:
        print(word)
    print("Dictionary of words and index: ")
    for i in range(1, len(word_dict) + 1):
        print(i, ':', word_dict[i])

except IOError as e:
    print('File not found')
    print(e)

except IndexError as i:
    print('Arguments not found')
    print(i)

except Exception as e:
    print(e)
