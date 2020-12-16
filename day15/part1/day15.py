import copy 

def Run(lines):
    #tracks number and age since last spoken
    last_turn_tracker = {}
    turn_count = 0
    starting_numbers = list(map(int, lines[0].split(',')))
    previous_number = -1

    while turn_count < 2020:
        #for starting numbers:
        if turn_count < len(starting_numbers):
            current_number = starting_numbers[turn_count]
            current_turn = {turn_count : current_number}
            last_turn_tracker.update(current_turn)
        else:
            current_number = previous_number

            if list(last_turn_tracker.values()).count(current_number) <= 1:
                #last time was first time spoken, use 0
                current_number = 0
            else:
                reverse_list = list(last_turn_tracker.values())[::-1]
                most_recent = reverse_list.index(current_number)
                second_most_recent = reverse_list[most_recent+1:].index(current_number)
                
                current_number = second_most_recent - most_recent + 1
            current_turn = {turn_count : current_number}
            last_turn_tracker.update(current_turn)

            print()
            



        
        previous_number = current_number



        turn_count+=1
    print(last_turn_tracker[turn_count-1])

        

