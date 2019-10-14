""" Implementation of Selection Sort algorithm
"""


def selection(array):
    """ SelectionSort algorithm sorts an array by repeatedly finding the
    minimum element (considering ascending order) from unsorted part and
    putting it at the beginning.
    """
    length = len(array)
    for i in range(length - 1):
        min_element_index = i
        for j in range(i+1, length):
            if array[j] < array[min_element_index]:
                min_element_index = j
        array[i], array[min_element_index] = array[min_element_index], array[i]


def main():
    """ operational function """
    arr = [56, 23, 89, 3, 55, 124, 87]
    print("original array:", arr)
    selection(arr)
    print("  sorted array:", arr)


if __name__ == '__main__':
    main()
