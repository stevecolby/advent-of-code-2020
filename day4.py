def Day4():
    valid_passport_count = 0
    invalid_passport_count = 0
    passport_list = []
    required_attributes = ['byr','iyr','eyr', 'hgt','hcl','ecl','pid']



    with open('day4_input') as input_file:
        lines = input_file.readlines()

        current_passport_attributes = []

        for line in lines:
            attributes = line.strip('\n').split(' ')
            
            for attribute in attributes:
                current_passport_attributes.append(attribute.split(':')[0])
            
            #blank line, so we've collected all attributes of a passport
            if attributes[0] == '':
                passport_list.append(current_passport_attributes)
                current_passport_attributes = []
        
        if current_passport_attributes[0] != '':
                passport_list.append(current_passport_attributes)


    for passport in passport_list:
        if is_passport_valid(required_attributes, passport):
            valid_passport_count += 1
        else:
            invalid_passport_count += 1
    
    print('Valid passports: ', valid_passport_count)
    print('Invalid passports: ', invalid_passport_count)

#check the attributes of the passport for validity
def is_passport_valid(required_attributes, passport_attributes):
    for req_attr in required_attributes:
        if not req_attr in passport_attributes:
            return False
    
    return True

