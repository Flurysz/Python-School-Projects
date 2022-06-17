#!/usr/bin/env python3

from itertools import permutations

def all_permutations_substrings(a_str):
    """Generates all permutations of all substrings of the input string
    """

    return set(
        ''.join(item)
        for length in range(len(a_str)+1)
        for item in permutations(a_str, length))

# max 2 points
# the fuction needs to deal with very long lists of words so that the approach
# has to be very efficient (no interest in slow solutions for toy test examples)
def match_permutations_substrings(string, words):
    """Generates all permutations of all substrings of the input string and
       returns a set of input words that match one of the permutations.

    >>> match_permutations_substrings('okna', ['a', 'z', 'v', 'o', 'k', 'ok', 'ano', 'no', 'hlava', 'oko', 'noky', 'nok', 'on', 'ona', 'ony']) == {'ona', 'a', 'ok', 'o', 'nok', 'no', 'ano', 'on', 'k'}
    True

    >>> match_permutations_substrings('opak', ['ok', 'pak', 'pako', 'ano', 'noha', 'oka', 'kap', 'kopa', 'kopat', 'ona', 'okap']) == {'kopa', 'kap', 'pako', 'ok', 'pak', 'okap', 'oka' }
    True

    """


    # permutations as a set
    perms = all_permutations_substrings(string)
    x2 = set(words)
    x1 = all_permutations_substrings(string)
    return x1.intersection(x2)            # your solution


# max 1 point
# the fuction needs to deal with very long input sequences of words so that 
# the approach has to be very efficient (no interest in slow solutions for 
# limited test examples)
def uniq_srt(it):
    """Returns the input sequence unified and sorted (according to the values)

    >>> uniq_srt([3, 3, 5, 3, 4, 2, 4])
    [2, 3, 4, 5]

    >>> uniq_srt('abrakadabra')
    ['a', 'b', 'd', 'k', 'r']

    """

    temp = []

    if type(it) == list:
        it.sort()
        for i in it:
            if i not in temp:
                temp.append(i)
        it = temp

    if type(it) == str:
        it = list(it)
        it.sort()
        for i in it:
            if i not in temp:
                temp.append(i)
        it = temp

    return it                             # your solution


# max 2 points
# the fuction needs to deal with very long input sequences of words so that 
# the approach has to be very efficient (no interest in slow solutions for 
# limited test examples)
def uniq_orig_order(it):
    """Returns the input sequence, items ordered by the order of their
       first appearance

    >>> uniq_orig_order([3, 3, 5, 3, 4, 2, 4])
    [3, 5, 4, 2]

    >>> uniq_orig_order('abrakadabra')
    ['a', 'b', 'r', 'k', 'd']

    """

    temp = []

    if type(it) == list:
        for i in it:
            if i not in temp:
                temp.append(i)
        it = temp

    if type(it) == str:
        it = list(it)
        for i in it:
            if i not in temp:
                temp.append(i)
        it = temp

    return it                                      # your solution


if __name__ == "__main__":
    import doctest
    doctest.testmod()