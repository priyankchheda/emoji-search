""" Implementation of Insertion Sort algorithm """

def insertion(array):
    """ sort collection using insertion sort """
    length = len(array)

    for i in range(length):
        index = i
        value = array[i]

        while index > 0 and array[index-1] > value:
            array[index] = array[index-1]
            index -= 1

        array[index] = value
