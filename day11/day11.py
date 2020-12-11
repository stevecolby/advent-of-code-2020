import more_itertools as mit
import copy

def Run(lines):
    should_occupy = True
    changes_found = True

    blue = []
    green = []

    for line in lines:
        blue.append(list(line))
        green.append(list(line))

    # loop until no changes were made during a full pass
    while changes_found:
        x = 0
        y = 0
        changes_found = False

        while y < len(lines[0]):
            x = 0
            while x < len(lines):
                current_seat = blue[x][y]
                num_occupied = count_occupied(blue, x, y)

                #record all changes to green
                if should_occupy:
                    if current_seat == 'L' and num_occupied == 0:
                        green[x][y] = '#'
                        changes_found = True
                else:
                    if current_seat == '#' and num_occupied >= 4:
                        green[x][y] = 'L'
                        changes_found = True
                x+=1
            y+=1
        
        should_occupy = not should_occupy
        blue = []
        blue = copy.deepcopy(green)
        print()
    
    total_seats = 0
    for row in blue:
        total_seats += row.count('#')
    
    print(total_seats)

def count_occupied(lines, x, y):
    occupied_count = 0
    
    if x > 0:
        min_x = x - 1
    else:
        min_x = 0
    
    if y > 0:
        min_y = y - 1
    else:
        min_y = 0
    
    if x < len(lines)-1:
        max_x = x + 1
    else:
        max_x = x
    
    if y < len(lines[0])-1:
        max_y = y + 1
    else:
        max_y = y

    
    while min_x <= max_x:
        y_counter = min_y
        while y_counter <= max_y:
            if not (min_x == x and y_counter == y):
                if lines[min_x][y_counter] ==  '#':
                    occupied_count+=1
            y_counter+=1
        min_x+=1
    
    return occupied_count

    