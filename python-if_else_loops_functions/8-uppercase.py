#!/usr/bin/python3

def uppercase(str):
    newstr = ""
    for index in range(0, len(str)):
        if ord(str[index]) > 96 and ord(str[index]) < 123:
            newstr += chr(ord(str[index]) - 32)
        else:
            newstr += str[index]
    print("{}".format(newstr))
