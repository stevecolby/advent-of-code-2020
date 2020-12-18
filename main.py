import importlib, sys, time

day = 17
part = 2
use_test_data = False

def main():

    import_name = 'day{0}.part{1}.run'.format(day, part)
    importlib.import_module(import_name)
    if use_test_data:
        input_filename = 'day{0}/part{1}/test_input'.format(day, part)
    else:
        input_filename = 'day{0}/part{1}/input'.format(day, part)

    with open(input_filename) as input_file:
        lines = input_file.readlines()

        clean_lines = []

        for line in lines:
            clean_lines.append(line.strip('\n'))

        getattr(sys.modules[import_name], "Run")(clean_lines)    
        

if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))