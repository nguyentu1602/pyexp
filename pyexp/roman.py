'''Module to convert to and from Roman numerals.
Current range supported: 1-3999.
'''
import re

class OutOfRangeError(ValueError):
    pass

class NotIntegerError(ValueError):
    pass

class InvalidRomanNumeralError(ValueError):
    pass

ROMAN_NUMERAL_MAP = (('M', 1000),
                     ('CM', 900),
                     ('D', 500),
                     ('CD', 400),
                     ('C', 100),
                     ('XC', 90),
                     ('L', 50),
                     ('XL', 40),
                     ('X', 10),
                     ('IX', 9),
                     ('V', 5),
                     ('IV', 4),
                     ('I', 1))

ROMAN_NUMERAL_PATTERN = re.compile('''
    ^                         # beginning of string
    M{0,3}                    # thousands - 0 to 3 Ms
    (CM|CD|D?C{0,3})          # hundreds - 900 (CM), 400 (CD), 0-300 (0 to 3 Cs),
                              # or 500-800 (D, followed by 0 to 3 Cs)
    (XC|XL|L?X{0,3})          # tens - 90 (XC), 40 (XL), 0-30 (0 to 3 Xs),
                              # or 50-80 (L, followed by 0 to 3 Xs)
    (IX|IV|V?I{0,3})          # ones - 9 (IX), 4 (IV), 0-3 (0 to 3 Is),
                              # or 5-8 (V, followed by 0 to 3 Is)
    $                         # end of string
    ''', re.VERBOSE)


def to_roman(num_int):
    '''Take an integer between 1 and 3999 and return Roman numeral
    '''
    if not isinstance(num_int, int):
        raise NotIntegerError(
            'Input is not of integer type.')
    if num_int >= 4000 or num_int <= 0:
        raise OutOfRangeError(
            'Number out of range (must be betwen 1 and 3999 inclusive).')
    result = ''
    for numeral, integer in ROMAN_NUMERAL_MAP:
        while num_int >= integer:
            result += numeral
            num_int -= integer
    return result

def from_roman(numeral_string):
    '''Convert Roman numeral to integer'''
    if not ROMAN_NUMERAL_PATTERN.search(numeral_string):
        raise InvalidRomanNumeralError(
            'Invalid Roman numeral: {0}'.format(numeral_string))
    result = 0
    index = 0
    '''iterate through the map and match numeral string from largest
    to smallest, adding to the result once match
    '''
    for numeral, integer in ROMAN_NUMERAL_MAP:
        while numeral_string[index:index+len(numeral)] == numeral:
            result += integer
            index += len(numeral)
    return result
