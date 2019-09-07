""" Selection Sort """

from utils import validate_input_collection, SortingException

def selection(array):
    """ sort collection using selection sort """
    if not validate_input_collection(array):
        raise SortingException("mixed type present in list")

    dataLen = len(array)
    for i in range(dataLen - 1):
        min_element_index = i
        for j in range(i+1, dataLen):
            if array[j] < array[min_element_index]:
                min_element_index = j
        array[i], array[min_element_index] = array[min_element_index], array[i]
