#!/usr/bin/python3

def roman_to_int(roman_string):
    """Converts a Roman numeral to an integer"""
    my_list = []
    result = 0
    if roman_string and type(roman_string) == str:
        dictionary = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100,
                      'D': 500, 'M': 1000}
        for roman_num in roman_string:
            for key in dictionary:
                if roman_num == key:
                    my_list.append(dictionary[key])
        for i in range(len(my_list) - 1, -1, -1):
            if my_list[i] <= my_list[i - 1]:
                result += my_list[i]
            else:
                my_list[i - 1] = my_list[i - 1] * -1
                result += my_list[i]
        return result
    else:
        return 0
