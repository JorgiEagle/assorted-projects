letters = {'start': {'FF': set('A M T U V W Y B C D E K H I O X'.split()),  # lines
                     '3F': set('M V E M J S N U'.split()),  # planets
                     'BF': set('I V X L C D M'.split()),  # roman
                     '7F': set('T C R'.split())  # resistors
                     },
           'mid': {'FF': set('Z X C V B N M'.split()),  # qwerty
                   '3F': set('B C D F G H J K L M N P Q R S T V W X Y Z'.split()),  # constant
                   'BF': set('H I N O X Z'.split()),  # point
                   '7F': set('A B C D E F G'.split())  # music
                   },
           'end': {'FF': set('T I V C R M N F E C O N I C U'.split()),  # metals
                   '3F': set('A R N D C E Q G H I L K M F P S T W Y V'.split()),  # amino
                   'BF': set('P B C D E T V G Z '.split()),  # rhymes
                   '7F': set('A B X E H I K M N O P T Y Z'.split())  # greek
                   }
           }
filters = ['End User', 'Product', 'Widget', 'Card Sorting', 'Storyboard', ' Front End', 'Open Source', 'Interaction', 'Heat Map', 'Harmony']
codes = ['#FF3FBF', '#FF7FFF', '#FFBF3F', '#FF7F7F', '#BF7F3F', '#FF3F7F', '#3FBF7F', '#FFFFBF', '#FF3FBF', '#FFBF3F']
i = 0
for code in codes:
    combo = code[1:]
    front = combo[:2]
    middle = combo[2:4]
    back = combo[4:6]
    set_intersection = letters['start'][front].intersection(letters['mid'][middle], letters['end'][back])
    print('Set intersection: ', set_intersection)
    print('Intersection with word: ', set_intersection.intersection(filters[i]))
    i += 1
filter_codes = dict(zip(filters, codes))
print(', '.join(sorted(filter_codes, key=lambda x: x[0])))
