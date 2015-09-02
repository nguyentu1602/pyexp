'''Module to solve the algoritm question:
Given a string S, how to count how many permutations
of S is in a longer string L, assuming, of course, that
permutations of S must be in contagious blocks in L.

I will solve it in O(len(L)) time.
For demonstration purpose, let's assume the characters
are ASCII lowercase letters only.
'''
import random, string    # for testing only

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

def gen_random_word(length):
    '''generate a random string of given length from
    ascii lowercase letters
    '''
    return ''.join(random.choice(string.ascii_lowercase)
                   for i in range(length))

def test_string_permu_hash(string_len=7, num_testcase=500):
    '''automatic roundtrip testing for hashing and de-hashing
    '''
    # TODO: edge cases? max values?
    base = string_len + 1
    for i in range(num_testcase):
        in_str = gen_random_word(string_len)
        hash_val = string_permu_hash(in_str)
        revert_string = convert_decomp_to_string(
            decomp_string_from_hash(hash_val, base))
        assert sort_char_string(in_str) == revert_string
    print("Done. string_permu_hash works like a charm.")

'''now I have everything to make a smart slider through L -
the given longer string. We will compute the hash_val once
for the string of first len(S) chars, and then keep updating
that hash value in O(1) as we slide.
We updating the hash_val by adding hash contribution from
of one more char from the right and subtracting hash
contribution from the left most char that we drop.
'''

def update_hash_val(hash_val, pop_char, push_char, base):
    '''helper function to update hash_val by popping and
    pushing chars.
    '''
    # TODO: check range maybe
    hash_val += base ** char_to_int(push_char)
    hash_val -= base ** char_to_int(pop_char)
    return hash_val

def sliding_permu_detect(short_str, long_str):
    '''this is the heart of the smart sliding solution!
    the special sliding function allows reducing complexity
    from O(S * L) to O(L)
    '''
    slider_len = len(short_str)
    base = slider_len + 1
    # make a hash_val out of short_str to be compared
    const_hash_val = string_permu_hash(short_str)
    # TODO: check len(long_str)
    moving_hash_val = string_permu_hash(long_str[:slider_len])
    # repeatedly compare sliding hash_val to short_str's hash val
    permu_count = int(moving_hash_val == const_hash_val)

    for pos in range(slider_len, len(long_str)):
        moving_hash_val = update_hash_val(moving_hash_val,
                                          long_str[pos - slider_len],
                                          long_str[pos],
                                          base)
        permu_count += (moving_hash_val == const_hash_val)
    return permu_count
