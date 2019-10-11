""" Implementation of Selection Sort algorithm """

def selection(array):
    """ sort collection using selection sort """
    length = len(array)
    for i in range(length - 1):
        min_element_index = i
        for j in range(i+1, length):
            if array[j] < array[min_element_index]:
                min_element_index = j
        array[i], array[min_element_index] = array[min_element_index], array[i]
