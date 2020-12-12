import math 

def Run(lines):
    current_direction_rad = 0
    x_change = 0
    y_change = 0

    for line in lines:
        direction = line[:1]
        amount = int(line[1:])


        print()
        
        if (direction == 'N' or 
            (direction == 'F' and current_direction_rad == 270)):
            y_change -= amount
        elif(direction == 'S' or 
            (direction == 'F' and current_direction_rad == 90)):
            y_change += amount
        elif(direction == 'E' or 
            (direction == 'F' and current_direction_rad == 0)):
            x_change += amount
        elif(direction == 'W' or 
            (direction == 'F' and current_direction_rad == 180)):
            x_change -= amount
        elif direction == 'R':
            current_direction_rad += amount
            current_direction_rad = current_direction_rad % 360
        elif direction == 'L':
            current_direction_rad -= amount
            current_direction_rad = current_direction_rad % 360
        




    print('(x,y) is ({0},{1}) - Sum: {2}'.format(x_change, y_change, x_change + y_change))