import more_itertools as mit

def Run(lines):

    numbers = []

    for line in lines:
        numbers.append(int(line))

    numbers.append(0)
    
    numbers.sort()
    
    sequentials = [list(group) for group in mit.consecutive_groups(numbers)]
    cleaned_numbers = []
    multiplier = 1


    for seq_set in sequentials:
        if len(seq_set) == 5:
            seq_set.remove(seq_set[2])
            seq_set.remove(seq_set[1])
            multiplier *= 7

        elif len(seq_set) == 4:
            seq_set.remove(seq_set[2])
            seq_set.remove(seq_set[1])
            multiplier *= 4

        elif len(seq_set) == 3:
            seq_set.remove(seq_set[1])
            multiplier *= 2
        
        for clean_seq in seq_set:
            cleaned_numbers.append(clean_seq)
    
    numbers = cleaned_numbers
        

    counter = 0
    numbers.append(max(numbers)+3)
    valid_paths = 0

    valid_paths = find_paths(counter, 0, numbers)

    print(valid_paths*multiplier)



def find_paths(counter, increment, numbers):
    temp_paths = 0
    valid_paths = 0
    counter += increment

    if counter == max(numbers):
        return 1
    
    if counter + 1 in numbers:
        temp_paths += find_paths(counter, 1, numbers)
    
    if counter + 2 in numbers:
        temp_paths += find_paths(counter, 2, numbers)
    
    if counter + 3 in numbers:
        temp_paths += find_paths(counter, 3, numbers)

    valid_paths += temp_paths
    
    #print(valid_paths)
    return valid_paths
