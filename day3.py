def Day3():
    tree_count = 0
    with open('day3_input') as input_file:
        lines = input_file.readlines()

        x_pos = 0
        is_first_line = True

        for line in lines:
            if is_first_line:
                is_first_line = False
            else:
                x_pos += 3
                tree_map = list(line.strip('\n'))
            
                if tree_map[x_pos % len(tree_map)] == '#':
                    tree_count += 1
    
    print(tree_count)