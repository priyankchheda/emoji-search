""" Implementation of Insertion Sort algorithm
"""


def insertion(array):
    """ InsertionSort is based on the idea that one element from the input
    elements is consumed in each iteration to find its correct position
    i.e, the position to which it belongs in a sorted array.
    """
    length = len(array)

    for i in range(length):
        index = i
        value = array[i]

        while index > 0 and array[index-1] > value:
            array[index] = array[index-1]
            index -= 1

        array[index] = value


def main():
    """ operational function """
    arr = [56, 23, 89, 3, 55, 124, 87]
    print("original array:", arr)
    insertion(arr)
    print("  sorted array:", arr)


if __name__ == '__main__':
    main()
