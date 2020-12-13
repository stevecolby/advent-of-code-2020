def Run(lines):
    active_bus_list = []
    increment_amount = 0
    bus_list = lines[1].split(',')

    x = 0
    while x < len(bus_list):
        if bus_list[x] != 'x':
            bus_id = int(bus_list[x])
            bus_and_offset = [bus_id, x]
            active_bus_list.append(bus_and_offset)
        x+=1
    

    iteration_amt = active_bus_list[0][0]
    start = active_bus_list[0][0]
    
    for bus in active_bus_list[1:]:
        start = get_next_departure(start, iteration_amt, bus)
        iteration_amt = iteration_amt * int(bus[0])

    print(start)

def get_next_departure(start, iteration, bus):
    current_departure_counter = start
    found = False

    while not found:        
        if ((current_departure_counter + bus[1]) % bus[0]) == 0:
            #match
            return current_departure_counter
        
        current_departure_counter += iteration
                
        #if earliest_time_counter > 1068700:
        #print(current_departure_counter)
