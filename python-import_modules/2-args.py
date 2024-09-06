#!/usr/bin/python3
import sys

index = 1

if len(sys.argv) == 1:
    print("0 argument.")
elif len(sys.argv) == 2:
    print(f"1 argument:")
    print(f"1: {sys.argv[1]}")
else:
    print(f"{len(sys.argv) - 1} arguments:")
    while index < len(sys.argv):
        print(f"{index}: {sys.argv[index]}")
        index += 1
