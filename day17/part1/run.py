import numpy as np

def Run(lines):
    num_cycles = 6
    num_starting_cube_side = len(lines)
    max_bounds = num_starting_cube_side + (num_cycles*2)
    
    cube_array = set_starting_positions(num_cycles, lines, max_bounds)

    cycle_count = 0

    while cycle_count < num_cycles:
        cube_array = do_cycle(cube_array, num_cycles, lines, max_bounds)
        cycle_count+=1
        print(get_actives(cube_array))

    active_count = get_actives(cube_array)

    print(active_count)

def get_actives(cube_array):
    active_count = 0

    for z in cube_array:
        for y in z:
            for x in y:
                if x == 1:
                    active_count += 1
    
    return active_count

def do_cycle(cube_array, num_cycles, lines, max_bounds):
    x = 0
    y = 0
    z = 0

    temp_array = set_starting_positions(num_cycles, lines, max_bounds)

    while z < len(cube_array[0]):
        y = 0
        while y < len(cube_array[0]):
            x = 0
            while x < len(cube_array[0]):
                active_neighbor_count = get_active_neighbors(cube_array, x, y, z)

                #if active but doesn't have 2 or 3 active neighbors, flip
                if (cube_array[z][y][x] == 1 and 
                    (active_neighbor_count != 2 and
                    active_neighbor_count != 3)):
                    temp_array[z][y][x] = 0
                
                #if inactive and has 3 active neighbors, flip
                elif (cube_array[z][y][x] == 0 and 
                    active_neighbor_count == 3):
                    temp_array[z][y][x] = 1
                
                else:
                    temp_array[z][y][x] = cube_array[z][y][x]
                
                x+=1
            y+=1
        z+=1
    
    return temp_array


def get_active_neighbors(cube_array, x, y, z):
    active_count = 0

    current_x = max(0, x-1)
    current_y = max(0, y-1)
    current_z = max(0, z-1)

    print('Actives for {0}, {1}, {2}'.format(z, y, x))

    while current_z <= min(len(cube_array[0])-1, z+1):
        current_y = max(0, y-1)
        while current_y <= min(len(cube_array[0])-1, y+1):
            current_x = max(0, x-1)
            while current_x <= min(len(cube_array[0])-1, x+1):
                if (current_x != x or current_y != y or current_z != z):
                    if cube_array[current_z][current_y][current_x] == 1:

                        print('{0}, {1}, {2} - 1'.format(current_z, current_y, current_x))
                        active_count+=1
                    else:
                        print('{0}, {1}, {2} - 0'.format(current_z, current_y, current_x))
                        
                current_x+=1
            current_y+=1
        current_z+=1
    
    return active_count
    


def set_starting_positions(num_cycles, lines, max_bounds):
    cube_array = np.zeros((max_bounds,max_bounds,max_bounds)) # 3D array

    y = 0
    z = int(max_bounds/2) - int(len(lines)/2)
    for line in lines:
        x = 0
        for cube in list(line):
            if cube == '.':
                active_val = 0
            else:
                active_val = 1

            cube_array[z][y+num_cycles][x+num_cycles] = active_val
            x+=1
        y+=1
    
    return cube_array
