#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            if i >= len(my_list_1) or i >= len(my_list_2):
                raise IndexError("out of range")
            num1 = my_list_1[i]
            num2 = my_list_2[i]
            if not isinstance(num1, (int, float)):
                raise TypeError("wrong type")
            if not isinstance(num2, (int, float)):
                raise TypeError("wrong type")
            result.append(num1 / num2)
        except IndexError:
            result.append(0)
            print("out of range")
        except TypeError:
            result.append(0)
            print("wrong type")
        except ZeroDivisionError:
            result.append(0)
            print("division by 0")
        finally:
            pass
    return result
