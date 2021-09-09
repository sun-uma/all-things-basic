"""
This project performs several operations on an input file and writes
the results into a unique OUTPUT file.

ReadWriteFile is a class which reads and writes to a file.

File Operations inherits ReadWriteFile and performs various file
operations on the class.
"""

import re
import uuid
import logging
import sys
import userconfig


class ReadWriteFile:
    """
    This class reads and writes to a text file.
    """

    def __init__(self, filename: str):
        self.file = filename

    def writefile(self, data: str):
        """
        :param data: this is a string
        :return: returns true if no exception is raised
        :raises: IOError Exception
        """
        try:
            with open(self.file, 'w', encoding='utf-8') as file_obj:
                file_obj.write(data)
                file_obj.close()
        except IOError as err:
            logging.error('File writing error. %s', err)

    def readfile(self) -> str:
        """
        :return: string containing the data
        :raises: IOError Exception
        """
        try:
            with open(self.file, 'r', encoding='utf-8') as file_obj:
                data = file_obj.read()
                file_obj.close()
        except IOError as err:
            logging.error('File reading error. %s', err)
        return data


class FileOperations(ReadWriteFile):
    """
    This class performs various file operations and prints the result
    into a new OUTPUT file.
    """
    def __init__(self, raw_input: str):
        super().__init__(str(uuid.uuid4())+'.txt')
        self.raw_input = raw_input

    def create_wordlist(self) -> list:
        """ :return: List of words with no special characters """
        # no_spec_char = ''.join(letter for letter in self.raw_input
        #                        if letter.isalpha() or letter.isspace())
        lower_input = self.raw_input.lower()
        wordlist = lower_input.split()
        for index, _ in enumerate(wordlist):
            wordlist[index] = wordlist[index].strip('?.!,;')
        return wordlist

    def to_prefix(self) -> int:
        """ :return: Number of words with prefix 'to' """
        logging.info('Inside to prefix method.')
        word_list = self.create_wordlist()
        count = 0
        for word in word_list:
            if word.startswith('to'):
                count += 1
        return count

    def ing_suffix(self) -> int:
        """ :return: Number of words with suffix 'ing' """
        logging.info('Inside ing suffix method.')
        word_list = self.create_wordlist()
        count = 0
        for word in word_list:
            if word.endswith('ing'):
                count += 1
        return count

    def max_found(self) -> str:
        """ :return: Word repeated maximum number of times """
        logging.info('Inside max found method.')
        max_occur = 1
        max_word = ''
        word_list = self.create_wordlist()
        unique_words = self.unique_words()
        for word in unique_words:
            count = word_list.count(word)
            if count > max_occur:
                max_occur = count
                max_word = word
        return max_word

    def list_palindrome(self) -> list:
        """ :return: List of all palindromes """
        logging.info('Inside list palindrome method.')
        word_list = self.create_wordlist()
        pal = []
        for word in word_list:
            if word == word[::-1] and len(word) > 1 and word not in pal:
                pal.append(word)
        return pal

    def unique_words(self) -> list:
        """ :return: List of unique words """
        logging.info('Inside unique words method.')
        word_list = self.create_wordlist()
        unique_words = []
        for word in word_list:
            if word not in unique_words:
                unique_words.append(word)
        return unique_words

    def word_dict(self) -> dict:
        """ :return: Dictionary of all words """
        logging.info('Inside word dict method.')
        word_list = self.create_wordlist()
        word_dictionary = {}
        for count, ele in enumerate(word_list, 1):
            word_dictionary[count] = ele
        return word_dictionary

    def alter_text(self) -> str:
        """
        This function reads the file contents and alters its contents.
        Unlike the other functions, alter text requires the data to
        retain newlines, spaces, and other special characters.
        """
        logging.info('Inside alter text method.')
        counter = 1

        altered_text = ''
        sentences = self.raw_input.split('\n')

        for sentence in sentences:
            words = sentence.split(' ')

            # Splitting each word based on vowels.
            new_words = []
            for word in words:
                new_words += re.split('[aeiouAEIOU]', word)

            # Capitalizing third letter and fifth word
            new_sentence = ''
            for index, _ in enumerate(new_words):
                if counter % 5 == 0:
                    new_words[index] = new_words[index].upper()
                elif len(new_words[index]) == 3:
                    new_words[index] = new_words[index][:2] + new_words[index][2].upper()
                elif len(new_words[index]) > 3:
                    new_words[index] = new_words[index][:2] \
                                   + new_words[index][2].upper() + new_words[index][3:]
                counter += 1

                # Replacing spaces with hyphens.
                new_sentence += new_words[index] + '-'

            # Replacing new lines with semi-colons
            altered_text += new_sentence + ';'

        logging.info('Altered text done successfully')

        return altered_text


if __name__ == '__main__':
    try:
        logging.basicConfig(filename='dev_logs.log', filemode='w', level=logging.INFO)
        logging.info('File run by %s from %s ID %s', userconfig.user['name'],
                     userconfig.user['org'], userconfig.user['id'])
        input_file = sys.argv[1]
        with open(input_file, 'r', encoding='utf-8') as file_object:
            input_string = file_object.read()
            file_object.close()

        file_operations = FileOperations(input_string)
        logging.info('File Operations object created.')

        # Calling and concatenating all the functions into one string.
        contents = ['Number of strings with "to" prefix: ' + str(file_operations.to_prefix()),
                    'Number of strings with "ing" suffix: ' + str(file_operations.ing_suffix()),
                    'Most common word: ' + file_operations.max_found(),
                    'Palindromes found: ' + str(file_operations.list_palindrome()),
                    'Unique Words present in the list: \n' + str(file_operations.unique_words()),
                    'Dictionary of words: \n' + str(file_operations.word_dict()),
                    'Altered text contents: ' + file_operations.alter_text()]

        logging.info('Created contents list')

        OUTPUT = ''
        for line in contents:
            OUTPUT += line + '\n\n'

        file_operations.writefile(OUTPUT)

        logging.info('File Operations carried out successfully.')

    except IndexError as i:
        logging.error('Index out of bounds error %s', str(i))

    except IOError as e:
        logging.error('File reading/writing error %s', e)
