import importlib, sys

day = 7

def main():

    import_name = 'day{0}.day{0}'.format(day)
    importlib.import_module(import_name)
    input_filename = 'day{0}/day{0}_input'.format(day)

    with open(input_filename) as input_file:
        lines = input_file.readlines()

        getattr(sys.modules[import_name], "Day%s" % day)(lines)    
        

if __name__ == "__main__":
    main()