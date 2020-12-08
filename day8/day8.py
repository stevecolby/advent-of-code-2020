def Day8(lines):
    accum = 0
    lines_executed = []
    current_line = 0

    while current_line not in lines_executed:
        lines_executed.append(current_line)

        execution_type = lines[current_line].split()[0]
        execution_amt = int(lines[current_line].split()[1])

        if execution_type == 'acc':
            accum += execution_amt
            current_line+=1
        elif execution_type == 'jmp':
            current_line += execution_amt
        else:
            current_line+=1
        

        print(accum)
        