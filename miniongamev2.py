import string

def minion_game(given_string):
    kevin_letters = set('AEIOU').intersection(given_string)
    stuart_letters = set(string.ascii_uppercase).difference(kevin_letters).intersection(given_string)
    string_length = len(given_string)
    kevin_score = 0
    stuart_score = 0

    for character in range(string_length):
        if given_string[character] in kevin_letters:
            kevin_score += (string_length - character)
        else:
            stuart_score += (string_length - character)

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
