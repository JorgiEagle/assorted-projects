import string


def generate_substrings(given_set, set_to_add, given_string):
    for character in given_set:
        string_to_change = given_string
        while string_to_change.find(character) + 1:
            index_of_character = string_to_change.find(character)
            string_to_change = string_to_change[index_of_character:]
            for length_of_substring in range(1, len(string_to_change) + 1):
                set_to_add.add(string_to_change[:length_of_substring])
            string_to_change = string_to_change[1:]




def occurences_of_substring(given_string, sub_string):
    count = 0
    for i in range(len(given_string)):
        if given_string[i:].startswith(sub_string):
            count += 1
    return count


def minion_game(given_string):
    kevin_letters = set('AEIOU').intersection(given_string)
    stuart_letters = set(string.ascii_uppercase).difference(kevin_letters).intersection(given_string)

    kevin_substrings = set()
    stuart_substrings = set()

    generate_substrings(kevin_letters, kevin_substrings, given_string)
    generate_substrings(stuart_letters, stuart_substrings, given_string)

    kevin_score = 0
    stuart_score = 0

    for substrings in kevin_substrings:
        kevin_score += occurences_of_substring(given_string, substrings)
    for substrings in stuart_substrings:
        stuart_score += occurences_of_substring(given_string, substrings)

    if kevin_score > stuart_score:
        print('Kevin', kevin_score)
    elif stuart_score > kevin_score:
        print('Stuart', stuart_score)
    else:
        print('Draw')

if __name__ == '__main__':
    s = input()
    s = s.upper()
    minion_game(s)
