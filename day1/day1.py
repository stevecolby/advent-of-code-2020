def Day1():
    numbers = []

    with open('day1/day1_input') as input_file:
        lines = input_file.readlines()

        for line in lines:
            numbers.append(int(line.strip('\n')))
        
        for current_number in numbers:
            for second_number in numbers:
                if 2020 - current_number - second_number in numbers:
                    pair = 2020 - current_number - second_number
                    print('found! ', current_number, ', ', second_number, ' and ', pair)
                    print('Product = ', current_number * second_number * pair)
                    break