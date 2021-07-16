colours = {'metals': set('T I V C R M N F E C O N I C U'.split()),
           'amino': set('A R N D C E Q G H I L K M F P S T W Y V'.split()),
           'rhymes': set('P B C D E T V G Z '.split()),
           'greek': set('A B X E H I K M N O P T Y Z'.split()),
           'FF0000': set('A M T U V W Y B C D E K H I O X'.split()),
           'initial': set('M V E M J S N U'.split()),
           'roman': set('I V X L C D M'.split()),
           'resistors': set('T C R'.split()),
           'qwerty': set('Z X C V B N M'.split()),
           'point': set('H I N O X Z'.split()),
           'constant': set('B C D F G H J K L M N P Q R S T V W X Y Z'.split()),
           'music': set('A B C D E F G'.split())
           }
while input('Continue: Y/N ').upper() == 'Y':
    combo = input().split()
    print(colours[combo[0]].intersection(colours[combo[1]], colours[combo[2]]))
