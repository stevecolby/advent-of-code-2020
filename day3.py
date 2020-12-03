def Day3():
    line_count = 0
    right_down_combos = [[1,1],
            [3,1],
            [5,1],
            [7,1],
            [1,2]]
            
    tree_tracker = [0 for _ in range(len(right_down_combos))]

    with open('day3_input') as input_file:
        lines = input_file.readlines()

        x_pos_tracker = [0 for _ in range(len(right_down_combos))]

        for line in lines:
            tree_map = list(line.strip('\n'))
            
            if line_count > 0:
                slope_count = 0

                #loop through each slope we need to check
                while slope_count < len(x_pos_tracker):
                    xy = right_down_combos[slope_count]
                    right_increment = xy[0]
                    down_increment = xy[1]
                    
                    #only do the lines we need
                    if line_count % down_increment == 0: 
                        
                        #on the right line, so move right and check for tree
                        x_pos_tracker[slope_count]+=right_increment

                        if tree_map[x_pos_tracker[slope_count] % len(tree_map)] == '#':
                            tree_tracker[slope_count] += 1
                    
                    slope_count+=1
            
            line_count+=1

    tree_sum = 1
    for tree_count in tree_tracker:
        tree_sum = tree_sum * tree_count
    
    print('Sum: ', sum)