def Run(lines):
    numbers = []
    jolt_jump_counts = [0, 0, 0, 0]

    for line in lines:
        numbers.append(int(line))
    
    numbers.sort()

    last_marker = 0
    counter = 0
    while counter <= max(numbers):
        if counter in numbers:
            jolt_jump_counts[counter-last_marker]+=1
            last_marker = counter
        
        counter += 1
    
    jolt_jump_counts[3] += 1 #add one as device can be 3 jolts higher rated

    print('single jumps: {0}\ntriple jumps: {1}\nproduct: {2}'.format(
        jolt_jump_counts[1], jolt_jump_counts[3],
         jolt_jump_counts[1] * jolt_jump_counts[3]))

    
        
