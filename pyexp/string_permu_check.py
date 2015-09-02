'''Module to solve the algoritm question:
Given a string S, how to count how many permutations
of S is in a longer string L, assuming, of course, that
permutations of S must be in contagious blocks in L.

I will solve it in O(len(L)) time.
For demonstration purpose, let's assume the characters
are ASCII lowercase letters only.
'''

# Q: given a character, how to convert it into its
# ASCII value? A: using ord() and chr()
SHIFT = ord('a')

def char_to_int(char):
    '''convert char in a-z to 0-25
    '''
    # TODO: range check
    return ord(char) - SHIFT

def int_to_char(num):
    '''convert num in 0-25 to a-z
    '''
    # TODO: range check
    return chr(num + SHIFT)

def string_permu_hash(in_str):
    '''hash a string based on the numbers of each char
    in the string. So 2 permutations of a string give
    the same hash. You can decompose this hash to get
    back the number of each char.
    '''
    base = len(in_str) + 1
    hash_result = 0
    for c in in_str:
        hash_result += base ** char_to_int(c)
    return hash_result

def increment_char(char, by=1):
    '''helper function to incremnt the char by 1
    '''
    return int_to_char(char_to_int(char) + 1)

def decomp_string_from_hash(hashnum, base):
    '''given a hash and a base, decompose the hash to give
    back the combination of letters that made up the string
    '''
    result_list_tuple = []
    current_char = 'a'
    # emulate a do-while loop here
    while True:
        (div, rem) = divmod(hashnum, base)
        hashnum = div
        if rem > 0:
            result_list_tuple.append((current_char, rem))
        current_char = increment_char(current_char)
        if hashnum == 0:
            break
    return result_list_tuple

def convert_decomp_to_string(list_tuple):
    '''Take a list of tuples in form (char, num) that
    represents the decomp of a string and back it out.
    '''
    result = []
    for (char, num) in list_tuple:
        result.append(char * num)
    return ''.join(result)

def sort_char_string(in_str):
    '''sort characters in a string
    '''
    return ''.join(sorted(in_str))
