def Run(lines):
    section_count = 0
    rules = []
    nearby_tickets = []
    your_ticket = []

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
            
            else:
                if ':' not in line:
                    int_list = []
                    
                    for item in line.split(','):
                        int_list.append(int(item))

                    if section_count == 1:
                        #your ticket
                        your_ticket.append(int_list)
            
                    elif section_count == 2:
                        #nearby tickets
                        nearby_tickets.append(int_list)
    
    valid_tickets = []

    for ticket in nearby_tickets:
        #check each number for validity
        is_valid = True

        for ticket_number in ticket:
            if not has_any_valid_match(int(ticket_number), rules):
                is_valid = False
                break
        
        if is_valid:
            valid_tickets.append(ticket)
    

    matching_positions = get_matching_positions(rules, your_ticket, valid_tickets)

    departure_positions = calculate_locations(matching_positions)

    departure_product = 1
    for location in departure_positions:
        ticket_val = your_ticket[0][location]
        departure_product *= ticket_val

    print(departure_product)

def calculate_locations(matching_positions):
    final_positions = []
    departure_positions = []
    fin_pos = {}

    while len(final_positions) < len(matching_positions):
        for position in matching_positions:
            if len(position) == 2:
                fin_pos.update({position[1] : position[0]})
                final_positions.append(position)

                if 'departure' in position[0]:
                    departure_positions.append(position[1])

                matched_value = position[1]
                for inner_position in matching_positions:
                    if len(inner_position) > 1:
                        inner_position.remove(matched_value)
                
                break
    
    return departure_positions

def get_matching_positions(rules, your_ticket, valid_tickets):
    positions = []

    for rule in rules:
        col_counter = 0
        current_rule = []
        current_rule.append(rule[0])

        while col_counter < len(your_ticket[0]):
            is_valid = True

            #check your ticket is valid
            if not has_valid_match(your_ticket[0][col_counter], rule):
                is_valid = False
        
            #check nearby tickets
            if is_valid:
                for ticket in valid_tickets:
                    if not has_valid_match(ticket[col_counter], rule):
                        is_valid = False
                        break
            
            if is_valid:
                current_rule.append(col_counter)
                
            col_counter+=1
        
        positions.append(current_rule)
    
    return positions

def has_any_valid_match(ticket_number, rules):
    for rule in rules:
        if has_valid_match(ticket_number, rule):
            return True
    return False

def has_valid_match(ticket_number, rule):
    if (rule[1] <= ticket_number <= rule[2]
    or rule[3] <= ticket_number <= rule[4]):
        return True
    
    return False