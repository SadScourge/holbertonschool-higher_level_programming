#!/usr/bin/python3
char = ""
for index in range(97, 123):
	if (index != 101) and (index != 113):
		char += chr(index)

print("{}".format(char), end="")
