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
    base = len(in_str) + 1
    hash_result = 0
    for c in in_str:
        hash_result += base ** char_to_int(c)
    return hash_result
