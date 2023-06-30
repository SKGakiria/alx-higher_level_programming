#!/usr/bin/python3
"""Finding a peak in a list of unsorted integers"""

def find_peak(list_of_integers):
    """Function finds a peak in a list of unsorted integers"""

    size = len(list_of_integers)

    if size == 0:
        return None
    
    min = 0
    max = size - 1

    while min < max:
        mid = (min + max) // 2
        
        if list_of_integers[mid] < list_of_integers[mid + 1]:
            min = mid + 1
        else:
            max = mid
    
    return list_of_integers[min]
