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
    min_count = int(line_elements[0].split('-')[0])
    max_count = int(line_elements[0].split('-')[1])
    searchCharacter = line_elements[1]
    password = line_elements[2]

    numCharsFound = password.count(searchCharacter)

    if numCharsFound >= min_count and numCharsFound <= max_count :
        print(numCharsFound, ' is between ', min_count, ' and ', max_count)
        return True
    
    return False


if __name__ == "__main__":
    main()