#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    index = 1
    result = 0

    if len(sys.argv) == 1:
        pass
    else:
        while index < len(sys.argv):
            result += int(sys.argv[index])
            index += 1
        print("{}".format(result))
