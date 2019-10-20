""" Dynamic Connectivity Problem (Quick Find Solution)

Given a set of N objects, connect two objects, or ask if two objects are
connected (directly or in-directly).

Quick-Find defect:
- Union too expensive (N array accesses)
- Trees are flat, but too expensive to keep them flat
"""


class QuickFind:
    """ QuickFind is a Eager Approach.
    interpretation: elem1 and elem2 are connected iff they have the same id
    """
    def __init__(self, n):
        """ initializing list of size n where value is same as index
        Time Complexity: O(n)
        """
        self.data = []
        for i in range(n):
            self.data.append(i)

    def connected(self, elem1, elem2):
        """ elem1 and elem2 are connected iff they have the same id
        Time Complexity: O(1)
        """
        return self.data[elem1] == self.data[elem2]

    def union(self, elem1, elem2):
        """ When connecting two objects elem1 and elem2, change the id of all
        objects that have the id of elem1 to that of elem2, or vice-versa.

        Time Complexity is O(n), which is too expensive.
        """
        pid = self.data[elem1]
        qid = self.data[elem2]
        for i in range(len(self.data)):
            if self.data[i] == pid:
                self.data[i] = qid


def main():
    """ operational function """
    print("initializing list of size 10")
    quick_find = QuickFind(10)
    print("connecting 1 and 2")
    quick_find.union(1, 2)
    print("connecting 3 and 4")
    quick_find.union(3, 4)
    print("connecting 0 and 5")
    quick_find.union(0, 5)
    print("connecting 5 and 6")
    quick_find.union(5, 6)
    print("connecting 2 and 7")
    quick_find.union(2, 7)
    print("connecting 8 and 3")
    quick_find.union(8, 3)
    print("is 8 and 9 connected?", quick_find.connected(8, 9))
    print("connecting 9 and 4")
    quick_find.union(9, 4)
    print("is 8 and 9 connected?", quick_find.connected(8, 9))


if __name__ == '__main__':
    main()
