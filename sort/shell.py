""" Implementation of Shell Sort algorithm """


def shell(array):
    """ ShellSort is mainly a variation of Insertion Sort. In insertion sort,
    we move elements only one position ahead. When an element has to be moved
    far ahead, many movements are involved. The idea of shellSort is to allow
    exchange of far items. In shellSort, we make the array h-sorted for a large
    value of h. We keep reducing the value of h until it becomes 1. An array is
    said to be h-sorted if all sublists of every h’th element is sorted.
    """
    length = len(array)
    gaps = [701, 301, 132, 57, 23, 10, 4, 1]

    for gap in gaps:
        h = gap
        while h < length:
            temp = array[h]
            i = h
            while i >= gap and array[i - gap] > temp:
                array[i] = array[i - gap]
                i -= gap
            array[i] = temp
            h += 1


def main():
    """ operational function """
    arr = [56, 23, 89, 3, 55, 124, 87]
    print("original array:", arr)
    shell(arr)
    print("  sorted array:", arr)


if __name__ == '__main__':
    main()
