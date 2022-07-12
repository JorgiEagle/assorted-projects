for test in range(int(input())):
    number_of_animals, dog_portions, cat_portions, extra_portions = map(int, input().split())
    portions = {'D': dog_portions, 'C': cat_portions}
    animal_string = input()

    case = 'Case #' + str(test+1) + ':'
    # if there are an insufficient number of dog portions
    if animal_string.count('D') > dog_portions:
        print(case, 'NO')
        continue
    for index, letter in enumerate(animal_string):
        if 'D' in animal_string[index:]:
            if portions[letter] > 0:
                portions[letter] -= 1
                if letter == 'D':
                    portions['C'] += extra_portions
            else:
                print(case, 'NO')
                break
        else:
            print(case, 'YES')
            break
    else:
        print(case, 'YES')
        print(time)