#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    result = 0
    for index in range(1, len(sys.argv)):
        if len(sys.argv) - 1 == 0:
            continue
        result += int(sys.argv[index])
    print("{}".format(result))
