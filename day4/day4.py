import re

def Day4():
    valid_passport_count = 0
    invalid_passport_count = 0
    passport_list = []

    with open('day4_input') as input_file:
        lines = input_file.readlines()

        current_passport_attributes = {}

        for line in lines:
            attributes = line.strip('\n').split(' ')
            
            #blank line, so we've collected all attributes of a passport
            if attributes[0] == '':
                passport_list.append(current_passport_attributes)
                current_passport_attributes = {}
            
            else:
                for attribute in attributes:
                    key = attribute.split(':')[0]
                    val = attribute.split(':')[1]
                    current_passport_attributes.update({key : val})
                    #current_passport_attributes.append(current_attribute)
            
        
        if len(current_passport_attributes) > 0:
                passport_list.append(current_passport_attributes)


    for passport in passport_list:
        if is_passport_valid(passport):
            valid_passport_count += 1
        else:
            invalid_passport_count += 1
    
    print('Valid passports: ', valid_passport_count)
    print('Invalid passports: ', invalid_passport_count)

#check the attributes of the passport for validity
def is_passport_valid(passport_attributes):
    required_attributes = ['byr','iyr','eyr', 'hgt','hcl','ecl','pid']
    valid_eye_colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

    for req_attr in required_attributes:
        if not req_attr in passport_attributes.keys():
            return False
        else:
            if req_attr == 'byr':
                if (int(passport_attributes[req_attr]) < 1920 
                or int(passport_attributes[req_attr]) > 2002):
                    return False
            
            elif req_attr == 'iyr':
                if (int(passport_attributes[req_attr]) < 2010 
                or int(passport_attributes[req_attr]) > 2020):
                    return False
            
            elif req_attr == 'eyr':
                if (int(passport_attributes[req_attr]) < 2020 
                or int(passport_attributes[req_attr]) > 2030):
                    return False
            
            elif req_attr == 'hgt':
                #need to get unit
                if str(passport_attributes[req_attr]).find('cm') >= 0:
                    #in centimeters
                    value = int(passport_attributes[req_attr].strip('cm'))
                    if (value < 150 or value > 193):
                        return False
                elif str(passport_attributes[req_attr]).find('in') >= 0:
                    value = int(passport_attributes[req_attr].strip('in'))
                    if (value < 59 or value > 76):
                        return False
                else:
                    return False
            
            elif req_attr == 'ecl':
                if not passport_attributes[req_attr] in valid_eye_colors:
                    return False
            
            elif req_attr == 'hcl':
                matches = re.findall('#[0-9a-f]{6}', passport_attributes[req_attr])
                
                if len(matches) < 1:
                    return False
            
            elif req_attr == 'pid':
                matches = re.findall('[\d]{9}', passport_attributes[req_attr])

                if (len(matches) != 1
                    or len(passport_attributes[req_attr]) != 9):
                    return False
                else:
                    print(passport_attributes[req_attr])
            
    
    return True

