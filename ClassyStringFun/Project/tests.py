import pytest
from main import FileOperations


@pytest.mark.parametrize('strings, result', [('  going beach tomorrow. sunday!! 12## blah',
                                              ['going', 'beach', 'tomorrow', 'sunday', '12##', 'blah']),
                                             ('123 123 1345', ['123', '123', '1345']),
                                             ('####%$(@)@*!)#_$_', ['####%$(@)@*!)#_$_']), ('   ', []),
                                             ('BLAHBLAHBLAHBLAH', ['blahblahblahblah'])])
def test_create_wordlist(strings, result):
    obj = FileOperations(strings)
    assert obj.create_wordlist() == result


@pytest.mark.parametrize('strings, result', [(' to today TO TOO TOMORROW t?o', 5),
                                             ('   to 2 ? to -t=o t/o toni8', 3),
                                             ('two _to  to t0 TTo To TO', 3),
                                             ('Today tomorrow tonight tototo fito', 4)])
def test_to_prefix(strings, result):
    obj = FileOperations(strings)
    assert obj.to_prefix() == result


@pytest.mark.parametrize('strings, result', [('ing GOInG ? ging Ingling ang', 4),
                                             ('     11111 11ing 23ing 31ing', 3),
                                             ('I N G i n g i  n  g coming', 1),
                                             ('ing3553 @iNg ing2434ing!@# ingding', 2)])
def test_ing_suffix(strings, result):
    obj = FileOperations(strings)
    assert obj.ing_suffix() == result


@pytest.mark.parametrize('strings, result', [('goING blAH no choi', ''),
                                             ('ada ada ADA ada aDa a9a', 'ada'),
                                             ('bl&&&29023 1320 90', ''),
                                             ('', '')])
def test_max_found(strings, result):
    obj = FileOperations(strings)
    assert obj.max_found() == result


@pytest.mark.parametrize('strings, result', [('refer madam abba acdefgfedca 121',
                                              ['refer', 'madam', 'abba', 'acdefgfedca', '121']),
                                             ('********', ['********']), ('12', []),
                                             ('bubbles CNC cnc GuG gUg', ['cnc', 'gug'])])
def test_palindrome_list(strings, result):
    obj = FileOperations(strings)
    assert obj.list_palindrome() == result


@pytest.mark.parametrize('strings, result', [('Hi hi HI hi! hi.', ['hi']),
                                             ('no NO N O', ['no', 'n', 'o']), ('', []),
                                             ('dot dot DoT dOt DOT', ['dot']),
                                             ('do boo boO Do DO BoO', ['do', 'boo'])
                                             ])
def test_unique_words(strings, result):
    obj = FileOperations(strings)
    assert obj.unique_words() == result
