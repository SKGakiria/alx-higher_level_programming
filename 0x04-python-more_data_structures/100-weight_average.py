#!/usr/bin/python3

def weight_average(my_list=[]):
    """Returns the weighted average of all integers tuple."""
    dot_product = 0
    add_values = 0
    if my_list:
        for element in my_list:
            dot_product += element[0] * element[1]
            add_values += element[1]
        weight_average = dot_product / add_values
        return weight_average
    else:
        return 0
