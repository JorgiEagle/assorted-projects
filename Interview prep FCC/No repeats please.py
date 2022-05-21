'''
Return the number of total permutations of the provided string that don't have repeated consecutive letters.
Assume that all characters in the provided string are each unique.

For example, aab should return 2 because it has 6 total permutations (aab, aab, aba, aba, baa, baa),
but only 2 of them (aba and aba) don't have the same letter (in this case a) repeating.

permAlone("aab") should return a number.
permAlone("aab") should return 2.
permAlone("aaa") should return 0.
permAlone("aabb") should return 8.
permAlone("abcdefa") should return 3600.
permAlone("abfdefa") should return 2640.
permAlone("zzzzzzzz") should return 0.
permAlone("a") should return 1.
permAlone("aaab") should return 0.
permAlone("aaabb") should return 12.
'''
import itertools


def repeated_letter(given_string):
    last_letter = given_string[-1]
    for letter in range(len(given_string)-1):
        if given_string[letter] == given_string[letter+1]:
            return False
    return True


def perm_alone(given_string):
    all_perms = [non_repeated for non_repeated in itertools.permutations(given_string, len(given_string)) if repeated_letter(non_repeated)]
    return len(all_perms)

tests = {"aab":2,
         "aaa":0,
         "aabb":8,
         "abcdefa":3600,
         "abfdefa":2640,
         "zzzzzzzz":0,
         "a":1,
         "aaab":0,
         "aaabb":12}

for test, result in tests.items():
    assert perm_alone(test) == result