class Bag(object):
    color = ""
    contents = []
    count = 0
    
    def __init__(self):
        self.color = ''
        self.contents = []
        self.count = 0

unique_parents = []

def Day7():
    bags = []

    with open('day7/day7_input') as input_file:
        lines = input_file.readlines()

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
    
    has_golden_count = 0
    loopcount = 0

    for bag in bags:
        loopcount+= 1
        if check_for_shinygold(bag, bags):
            has_golden_count += 1
         #   print(loopcount, ' hit: ', bag.color)
        #else:
            #print(loopcount, ' miss:', bag.color)
    
    print('total bags: ', has_golden_count)

def check_for_shinygold(bag, bags):
    if bag.color == 'shinygold':
        return True
    else:
        for child_bag in bag.contents:
            if child_bag.color == 'shinygold':
                print(bag.color)
                if bag.color not in unique_parents:
                    unique_parents.append(bag.color)
                return True
    
    #bag is not gold, doesn't contain gold. Call to check each content bag
    for content_bag in bag.contents:
        next_bag = [x for x in bags if x.color == content_bag.color]
        if check_for_shinygold(next_bag[0], bags):
            return True
    
    return False