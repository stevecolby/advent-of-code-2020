def Day6():
    running_total = 0

    with open('day6/day6_input') as input_file:
        lines = input_file.readlines()
        first_of_group = True

        current_group = []

        for line in lines:
            line = line.strip('\n')

            if first_of_group:
                running_total += len(current_group)
                current_group = list(line)
                first_of_group = False

            elif line == '':
                first_of_group = True
            
            else:
                current_line = list(line)
                removed_items = []
                for item in current_group:
                    if item not in current_line:
                        removed_items.append(item)
                
                for item in removed_items:
                    current_group.remove(item)
        

        if len(current_group):
            running_total += len(current_group)
        
    print(running_total)    