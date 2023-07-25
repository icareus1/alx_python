from sys import argv
if __name__ == '__main__':
    if len(sys.argv) == 1:
        print("{} argument:".format(len(argv)))
    elif len(sys.argv) == 0:
        print("{} arguments.".format(len(argv)))
    else:
        print("{} arguments:".format(len(arg)))

    for i in range(1, len(argv)):
        print("{}: {}".format(i, argv[i]))