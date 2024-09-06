#!/usr/bin/python3
result = ""
for index in range(0, 99):
    result += f"{index} = {hex(index)}"
    if index != 98:
        result += "\n"
print("{}".format(result))
