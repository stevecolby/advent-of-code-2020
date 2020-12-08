import importlib, sys

day = 8

def main():

    import_name = 'day{0}.day{0}'.format(day)
    importlib.import_module(import_name)
    input_filename = 'day{0}/day{0}_input'.format(day)
    test_input_filename = 'day{0}/day{0}_test_input'.format(day)

    with open(input_filename) as input_file:
        lines = input_file.readlines()

        clean_lines = []

        for line in lines:
            clean_lines.append(line.strip('\n.'))

        getattr(sys.modules[import_name], "Day%s" % day)(clean_lines)    
        

if __name__ == "__main__":
    main()