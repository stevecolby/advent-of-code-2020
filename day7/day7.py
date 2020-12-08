class Bag(object):
    color = ""
    contents = []
    count = 0
    
    def __init__(self):
        self.color = ''
        self.contents = []
        self.count = 0

def Day7(lines):
    bags = []

    #with open('day7/day7_input') as input_file:
    #lines = input_file.readlines()

    for line in lines:
        line = line.strip('\n.').replace(',', '').replace('bags', 'bag')+' '

        #striped tan bags contain 2 light silver bags, 1 drab black bag, 2 clear tan bags, 2 mirrored tan bags.
        main_bag = Bag()
        main_bag.color = line.split(' bag contain ')[0].replace(' ', '')
        main_bag.count = 1

        rest_of_line = line.split(' bag contain ')[1].split()

        if 'other' not in rest_of_line:
            content_bag = Bag()
            #2 light silver bag 1 drab black bag 2 clear tan bag 2 mirrored tan bag
            for item in rest_of_line:
                if item == 'bag':
                    main_bag.contents.append(content_bag)
                    content_bag = Bag()
                elif item.isdigit():
                    content_bag.count = int(item)
                else:
                    content_bag.color += item
        else:
            print('')
        
        bags.append(main_bag)
    total_bag_count = 0

    shiny_gold_bag = [x for x in bags if x.color == 'shinygold'][0]

    x = sum_contents(shiny_gold_bag, 1, bags)

    print('total bags: ', total_bag_count)

def sum_contents(bag, multiplier, bags):
    total_bag_count = 0
    prev_call = 0

    if len(bag.contents) > 0:
        for child_bag in bag.contents:
            next_bag = [x for x in bags if x.color == child_bag.color][0]
            next_bag.count = child_bag.count
            prev_call += sum_contents(next_bag, child_bag.count*multiplier, bags)
    total_bag_count = multiplier + prev_call
    return total_bag_count