def Run(lines):
    earliest_time = int(lines[0])
    active_bus_list = []

    for bus in lines[1].split(','):
        if bus is not 'x':
            active_bus_list.append(int(bus))
    
    min_wait_time = 10000000
    min_wait_bus_ID = 0

    for bus in active_bus_list:
        wait_time = ((1+int(earliest_time/bus))*bus) - earliest_time
        
        if wait_time < min_wait_time:
            min_wait_time = wait_time
            min_wait_bus_ID = bus
    
    print(min_wait_time * min_wait_bus_ID)
