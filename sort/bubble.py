""" Bubble Sort """

from utils import validate_input_collection, SortingException

def bubble(array):
    """ sort collection using bubble sort """
    if not validate_input_collection(array):
        raise SortingException("mixed type present in list")

    lenght = len(array)
    swapped = True

    while swapped:
        swapped = False
        for i in range(lenght - 1):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
                swapped = True
