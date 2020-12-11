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
                    if current_seat == '#' and num_occupied >= 5:
                        green[x][y] = 'L'
                        changes_found = True
                x+=1
            y+=1
        
        should_occupy = not should_occupy
        blue = []
        blue = copy.deepcopy(green)
    
    total_seats = 0
    for row in blue:
        total_seats += row.count('#')
    
    print(total_seats)

def count_occupied(lines, x, y):
    occupied_count = 0

    left = False
    right = False
    up = False
    down = False
    
    if x > 0:
        left = True
    
    if y > 0:
        up = True
    
    if x < len(lines)-1:
        right = True
    
    if y < len(lines[0])-1:
        down = True

    #check 8 combinations
    if up and left:
        if occupied_seat_found(-1, -1, x-1, y-1, lines):
            occupied_count += 1
    
    if up:
        if occupied_seat_found(0, -1, x, y-1, lines):
            occupied_count += 1
    
    if up and right:
        if occupied_seat_found(1, -1, x+1, y-1, lines):
            occupied_count += 1
    
    if right:
        if occupied_seat_found(1, 0, x+1, y, lines):
            occupied_count += 1
    
    if down and right:
        if occupied_seat_found(1, 1, x+1, y+1, lines):
            occupied_count += 1
    
    if down:
        if occupied_seat_found(0, 1, x, y+1, lines):
            occupied_count += 1
    
    if down and left:
        if occupied_seat_found(-1, 1, x-1, y+1, lines):
            occupied_count += 1
    
    if left:
        if occupied_seat_found(-1, 0, x-1, y, lines):
            occupied_count += 1
    
    return occupied_count

def occupied_seat_found(x_change, y_change, x, y, lines):
    
    if lines[x][y] == '#':
        return True
    elif lines[x][y] == 'L':
        return False
    
    if (y + y_change < len(lines[0]) and 
        y + y_change >= 0 and 
        x + x_change < len(lines) and
        x + x_change >= 0):
        check_seat =  occupied_seat_found(x_change, y_change, x + x_change, y + y_change, lines)
        return check_seat
    else:
        return False