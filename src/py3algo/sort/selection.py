""" Implementation of Selection Sort algorithm
"""


def selection(array):
    """ Selection sort algorithm sorts an array by repeatedly finding the
    minimum element (considering ascending order) from unsorted part and
    putting it at the beginning.

    :param array: list of elements that needs to be sorted
    :type array: list
    """
    length = len(array)
    for i in range(length - 1):
        min_element_index = i
        for j in range(i+1, length):
            if array[j] < array[min_element_index]:
                min_element_index = j
        array[i], array[min_element_index] = array[min_element_index], array[i]
