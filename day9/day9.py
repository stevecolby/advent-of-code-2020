def Day9(lines):
    buffer_length = 25
    numbers = []

    for line in lines:
        numbers.append(int(line))
    
    counter = buffer_length
    while counter < len(numbers):
        previous_numbers = numbers[counter-buffer_length:counter]

        found = False
        for first_number in previous_numbers:

            if not found:
                for second_number in previous_numbers:
                    
                    if (first_number != second_number and
                    first_number + second_number == numbers[counter]):
                        found = True
                        break
            else:
                break
        
        if not found:
            print('Match not found at {0}: {1}'.format(counter, numbers[counter]))
            return
        
        counter += 1

    
        
