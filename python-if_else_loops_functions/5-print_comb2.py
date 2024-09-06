#!/usr/bin/python3

str = ""
for index in range(0, 100):
    str += f"{index:02d}"
    if index != 99:
        str += ", "
print("{}".format(str))
