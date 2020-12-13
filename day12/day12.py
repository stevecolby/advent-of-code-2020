import math 

def Run(lines):
    waypoint_x = 10
    waypoint_y = -1
    current_direction_rad = 0
    x_change = 0
    y_change = 0

    for line in lines:
        direction = line[:1]
        amount = int(line[1:])


        print()
        
        if direction == 'N':
            waypoint_y -= amount
        elif direction == 'S':
            waypoint_y += amount
        elif direction == 'E':
            waypoint_x += amount
        elif direction == 'W':
            waypoint_x -= amount
        elif direction == 'R':
            turn_times = amount/90
            counter = 0
            
            while counter < turn_times:
                #+x >> +y >> -x >> -y
                temp_x = waypoint_x
                waypoint_x = waypoint_y*-1
                waypoint_y = temp_x
                counter += 1
            
        elif direction == 'L':
            turn_times = amount/90
            counter = 0

            while counter < turn_times:
                #+x >> -y >> -x >> +y
                temp_y = waypoint_y
                waypoint_y = waypoint_x*-1
                waypoint_x = temp_y
                counter += 1
        
        elif direction == 'F':
            x_change += (waypoint_x * amount)
            y_change += (waypoint_y * amount)
            
        




    print('(x,y) is ({0},{1}) - Sum: {2}'.format(x_change, y_change, abs(x_change) + abs(y_change)))