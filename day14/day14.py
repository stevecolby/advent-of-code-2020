import copy 

def Run(lines):
    memory_instances = {}

    for line in lines:
        if 'mask = ' in line:
            mask = list(line.split(' = ')[1])
            print('New Mask: {0}'.format(''.join(str(e) for e in mask)))
        else:
            clean_line = line.replace('mem[', '').replace(']', '')
            mem_location = clean_line.split(' = ')[0]
            value = clean_line.split(' = ')[1]

            #fill with leading zeros
            location_as_bits = list(bin(int(mem_location))[2:].zfill(len(mask)))

            bit_counter = 0
            result_bitmask = []

            while bit_counter < len(location_as_bits):
                if mask[bit_counter] != '0':
                    result_bitmask.append(mask[bit_counter])
                else:
                    result_bitmask.append(location_as_bits[bit_counter])
                
                bit_counter+=1
            
            set_values(result_bitmask, int(value), memory_instances)
            
    
    val_sum = 0
    for value in memory_instances.values():
        val_sum+=value

    print(val_sum)

def set_values(result_bitmask, value, memory_instances):
    if 'X' in result_bitmask:
        first_x = result_bitmask.index('X')

        temp_bitmask = copy.deepcopy(result_bitmask)
        temp_bitmask[first_x] = '0'
        set_values(temp_bitmask, value, memory_instances)


        temp_bitmask = copy.deepcopy(result_bitmask)
        temp_bitmask[first_x] = '1'
        set_values(temp_bitmask, value, memory_instances)
    
    else:
        mem_as_int = int(''.join(str(e) for e in result_bitmask), 2)
        memory_instances.update({mem_as_int : value})

        

