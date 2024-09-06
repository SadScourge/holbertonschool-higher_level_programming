#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    
    index = 1
    
    if len(sys.argv) == 1:
        print("0 argument.")
    elif len(sys.argv) == 2:
        print("1 argument:")
        print("1: {}".format(sys.argv[1]))
    else:
        print("{} arguments:".format(len(sys.argv) - 1))
        while index < len(sys.argv):
            print("{}: {}".format(index, sys.argv[index]))
            index += 1
