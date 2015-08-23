class OutOfRangeError(ValueError):
    pass

class NotIntegerError(ValueError):
    pass

roman_numeral_map = (('M', 1000),
                     ('CM', 900),
                     ('D', 500),
                     ('CD', 400),
                     ('C', 100),
                     ('XC', 90),
                     ('L', 50),
                     ('XL', 40),
                     ('X', 10),
                     ('IX', 9),
                     ('V',  5),
                     ('IV', 4),
                     ('I', 1))


def to_roman(n):
    '''Take an integer between 1 and 3999 and return Roman numeral
    '''
    if not isinstance(n, int):
        raise NotIntegerError(
            'Input is not of integer type.')
    if n >= 4000 or n <= 0:
        raise OutOfRangeError(
            'Number out of range (must be betwen 1 and 3999 inclusive).')
    result = ''
    for numeral, integer in roman_numeral_map:
        while n >= integer:
            result += numeral
            n -= integer
    return result

def from_roman(s):
    '''Convert Roman numeral to integer'''
    result = 0
    index = 0
    '''iterate through the map and match numeral string from largest
    to smallest, adding to the result once match
    '''
    for numeral, integer in roman_numeral_map:
        while s[index:index+len(numeral)] == numeral:
            result += integer
            index += len(numeral)
    return result
