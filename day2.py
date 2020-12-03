def main():
    validPasswordCount = 0
    with open('input') as input_file:
        lines = input_file.readlines()
        
        for line in lines:
            if isPasswordValid(line):
                validPasswordCount+=1

    print('Valid Line Count: ', validPasswordCount)

def isPasswordValid(input_line):
    line_elements = input_line.strip('\n').replace(':', '').split(' ')
    first_location = int(line_elements[0].split('-')[0])-1
    second_location = int(line_elements[0].split('-')[1])-1
    searchCharacter = line_elements[1]
    password = line_elements[2]

    matchCount = 0

    if password[first_location] == searchCharacter:
        matchCount += 1

    if password[second_location] == searchCharacter:
        matchCount += 1

    if matchCount == 1:
        print('MATCH:', input_line)
        return True

    elif matchCount == 2:
        print('DOUBLE MATCH: ', input_line)
    
    return False


if __name__ == "__main__":
    main()