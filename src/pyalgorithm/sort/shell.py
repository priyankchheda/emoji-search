""" Implementation of Shell Sort algorithm """

def shell(array):
    """ sort collection using shell sort """
    length = len(array)
    gaps = [701, 301, 132, 57, 23, 10, 4, 1]

    for gap in gaps:
        j = gap
        while j < length:
            temp = array[j]
            i = j
            while i >= gap and array[i - gap] > temp:
                array[i] = array[i - gap]
                i -= gap
            array[i] = temp
            j += 1
