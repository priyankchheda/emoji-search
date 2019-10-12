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


def main():
    """ operational function """
    arr = [56, 23, 89, 3, 55, 124, 87]
    print("original array:", arr)
    bubble(arr)
    print("  sorted array:", arr)


if __name__ == '__main__':
    main()
