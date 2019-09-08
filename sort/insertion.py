""" Insertion Sort """

from utils import validate_input_collection, SortingException

def insertion(array):
    """ sort collection using insertion sort """
    if not validate_input_collection(array):
        raise SortingException("mixed type present in list")

    data_len = len(array)

    for i in range(data_len):
        index = i
        value = array[i]

        while index > 0 and array[index-1] > value:
            array[index] = array[index-1]
            index -= 1

        array[index] = value
