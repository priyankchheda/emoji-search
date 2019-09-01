""" Bubble Sort """


class SortingException(Exception):
    """ General sorting exception """


def validate_input_collection(collection):
    """ checks if the input collection list consists of elements of same type
        :param collection: list of input element
        :return: returns true if all elements of collections are of same type
            else false
    """
    if not collection:
        return True

    element_type = type(collection[0])
    return all(isinstance(x, element_type) for x in collection)


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
