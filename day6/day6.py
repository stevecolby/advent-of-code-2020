def Day6():
    running_total = 0

    with open('day6/day6_input') as input_file:
        lines = input_file.readlines()

        current_group = []

        for line in lines:
            line = line.strip('\n')

            if line == '':
                running_total += len(current_group)
                current_group = []
            else:
                for answer in list(line):
                    if answer not in current_group:
                        current_group.append(answer)
                print('')
        

        if len(current_group):
            running_total += len(current_group)
        
    print(running_total)    