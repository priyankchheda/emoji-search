""" Implementation of Insertion Sort algorithm
"""


def insertion(array):
    """ Insertion sort is based on the idea that one element from the input
    elements is consumed in each iteration to find its correct position
    i.e, the position to which it belongs in a sorted array.

    :param array: list of elements that needs to be sorted
    :type array: list
    """
    length = len(array)

    for i in range(length):
        index = i
        value = array[i]

        while index > 0 and array[index-1] > value:
            array[index] = array[index-1]
            index -= 1

        array[index] = value
