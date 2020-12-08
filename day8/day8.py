def Day8(lines):
    accum = 0
    lines_executed = []
    nop_jmp_change_counter = 0
    current_line = 0

    while nop_jmp_change_counter < 605:
        lines_executed = []
        current_line = 0
        accum = 0
        while (current_line not in lines_executed and
        current_line < 605):
            lines_executed.append(current_line)

            execution_type = lines[current_line].split()[0]
            execution_amt = int(lines[current_line].split()[1])

            if execution_type == 'acc':
                accum += execution_amt
                current_line+=1                            
            else:
                #invert jmp and nop
                if nop_jmp_change_counter == current_line:
                    if execution_type == 'nop':
                        current_line += execution_amt
                    elif execution_type == 'jmp':
                        current_line+=1
                else:
                    if execution_type == 'jmp':
                        current_line += execution_amt
                    else:
                        current_line+=1
    
        if current_line == 605:
            print(accum)
        else:
            nop_jmp_change_counter+=1
        