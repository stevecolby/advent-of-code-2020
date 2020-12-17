def Run(lines):
    #tracks number and age since last spoken
    last_turn_tracker = {}
    turn_count = 0
    starting_numbers = list(map(int, lines[0].split(',')))
    previous_number = -1

    while turn_count < 30000000:
        #for starting numbers:
        if turn_count < len(starting_numbers):
            current_number = starting_numbers[turn_count]
            current_turn = {current_number : [turn_count, 0]}
            last_turn_tracker.update(current_turn)
        else:            
            if last_turn_tracker[previous_number][1] == 0:
                #last time was first time spoken, use 0
                current_number = 0
            else:
                current_number = last_turn_tracker[previous_number][1]
            
            if current_number not in last_turn_tracker:
                age_since_last = 0
            else:
                age_since_last = turn_count - last_turn_tracker[current_number][0]

            current_turn = {current_number : [turn_count, age_since_last]}
            last_turn_tracker.update(current_turn)

        previous_number = current_number

        turn_count+=1
        if turn_count % 1000 == 0:
            print('Turn {0}: {1}'.format(turn_count, current_number))
            
    print(current_number)

        

