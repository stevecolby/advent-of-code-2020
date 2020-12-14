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
            val_as_bits = list(bin(int(value))[2:].zfill(len(mask)))

            bit_counter = 0
            result_bitmask = []

            while bit_counter < len(val_as_bits):
                if mask[bit_counter] != 'X':
                    result_bitmask.append(mask[bit_counter])
                else:
                    result_bitmask.append(val_as_bits[bit_counter])
                
                bit_counter+=1
            
            mem_as_int = int(''.join(str(e) for e in result_bitmask), 2)

            
            #entry = {'location': mem_location, 'value': value}
            memory_instances.update({mem_location : mem_as_int})
    
    val_sum = 0
    for value in memory_instances.values():
        val_sum+=value

    print(val_sum)

