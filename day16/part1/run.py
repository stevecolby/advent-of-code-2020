def Run(lines):
    section_count = 0
    rules = []
    nearby_tickets = []

    for line in lines:
        if line == '':
            section_count += 1
        else:
            if section_count == 0:
                #rules
                index = line.index(':')
                words = list(line[index:].split())
                rule_name = line[0:index].replace(':', '')
                range_1_min = int(words[1].split('-')[0])
                range_1_max = int(words[1].split('-')[1])
                range_2_min = int(words[3].split('-')[0])
                range_2_max = int(words[3].split('-')[1])

                rules.append([rule_name, range_1_min, range_1_max, range_2_min, range_2_max])
            
            #elif section_count == 1:
                #your ticket
            
            elif section_count == 2:
                #nearby tickets
                if ':' not in line:
                    nearby_tickets.append(list(line.split(',')))
    
    scanning_error_rate = 0

    for ticket in nearby_tickets:
        #check each number for validity
        for ticket_number in ticket:
            if not has_any_valid_match(int(ticket_number), rules):
                scanning_error_rate += int(ticket_number)
    print(scanning_error_rate)

def has_any_valid_match(ticket_number, rules):
    for rule in rules:
        if (rule[1] <= ticket_number <= rule[2]
        or rule[3] <= ticket_number <= rule[4]):
            return True
    return False