#!/usr/bin/python3
str = ""
for first_digit in range(0, 10):
	for second_digit in range(first_digit + 1, 10):
		str += f"{first_digit}{second_digit}"
		if not (first_digit == 8 and second_digit == 9):
			str += f", "
print (str)
