def Day5():
    max_seat_id = 0

    with open('day5/day5_input') as input_file:
        lines = input_file.readlines()

        for line in lines:
            current_seat_id = get_seat_id(line)

            if current_seat_id > max_seat_id:
                max_seat_id = current_seat_id
    
    print('Max Seat ID: ', max_seat_id)

def get_seat_id(seat_location):
    seat_id = 0
    current_min = 0
    current_max = 127
    diff = current_max - current_min + 1

    location_list = list(seat_location[0:7])

    for step in location_list:
        diff = int(diff / 2)
        if step == 'F':
            current_max = current_max - diff
        else:
            current_min = current_min + diff

    row = calculate_location(0, 127, list(seat_location[0:7]))
    seat = calculate_location(0, 7, list(seat_location[7:10]))

    seat_id = (row * 8) + seat

    print('(', row, ', ', seat, ') - ', seat_id)

    return seat_id

def calculate_location(current_min, current_max, location_list):
    diff = current_max - current_min + 1

    for step in location_list:
        diff = int(diff / 2)
        if (step == 'F' or step == 'L'):
            current_max = current_max - diff
        else:
            current_min = current_min + diff

    return current_max



    print('')