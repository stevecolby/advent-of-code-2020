def Day9(lines):
    invalid_number = 507622668
    numbers = []

    for line in lines:
        numbers.append(int(line))
    
    counter = 0
    while counter < len(numbers):
        current_sum = 0
        current_min = 1000000000
        current_max = 0

        sub_list = numbers[counter:]

        for number in sub_list:
            current_sum += number

            if number < current_min:
                current_min = number
            elif number > current_max:
                current_max = number
            
            if current_sum == invalid_number:
                print('Found at {0}. Min: {1}, Max: {2}. Sum: {3}'.format(
                    counter, current_min, current_max, current_min + current_max
                ))
                return
        
        counter += 1

    
        
