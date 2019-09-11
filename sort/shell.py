""" Shell Sort """

from utils import validate_input_collection, SortingException

def shell(array):
    """ sort collection using shell sort """
    if not validate_input_collection(array):
        raise SortingException("mixed type present in list")

    array_len = len(array)

    h = 1
    while h < array_len/3:
        h = h * 3 + 1

    while h >= 1:
        for i in range(h, array_len):
            j = i
            while j >=h and array[j] < array[j-h]:
                array[j], array[j-h] = array[j-h], array[j]
                j = j-h
        h = h//3
