import importlib, sys
import time

day = 10
use_test_data = False

def main():

    import_name = 'day{0}.day{0}'.format(day)
    importlib.import_module(import_name)
    if use_test_data:
        input_filename = 'day{0}/day{0}_test_input'.format(day)
    else:
        input_filename = 'day{0}/day{0}_input'.format(day)

    with open(input_filename) as input_file:
        lines = input_file.readlines()

        clean_lines = []

        for line in lines:
            clean_lines.append(line.strip('\n.'))

        getattr(sys.modules[import_name], "Run")(clean_lines)    
        

if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))