""" Implementation of Bubble Sort algorithm """

def bubble(array):
    """ sort collection using bubble sort """
    length = len(array)
    swapped = True

    while swapped:
        swapped = False
        for i in range(length - 1):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
                swapped = True
