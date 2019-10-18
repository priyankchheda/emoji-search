""" Dynamic Connectivity Problem (Quick Union Solution)

Given a set of N objects, connect two objects, or ask if two objects are
connected (directly or in-directly).

Quick-Union defect:
- Trees can get tall
- Find too expensive (could be N array accesses)
"""


class QuickUnion:
    """ QuickUnion is a lazy approach.
    interpretation: data[i] is parent of i. Root of i is id[id[...id[i]...]]
    """
    def __init__(self, n):
        """ initializing list of size n where value is same as index
            Here it means that each node is a root of it's own tree
        """
        self.data = []
        for i in range(n):
            self.data.append(i)

    def root(self, elem):
        """ finding the root of element """
        while elem != self.data[elem]:
            elem = self.data[elem]
        return elem

    def connected(self, elem1, elem2):
        """ elem1 and elem2 are connected iff they have same root """
        return self.root(elem1) == self.root(elem2)

    def union(self, elem1, elem2):
        """ To merge components containing elem1 and elem2, set the id of
        elem1's root to the id of elem2's root
        """
        root_elem1 = self.root(elem1)
        root_elem2 = self.root(elem2)
        self.data[root_elem1] = root_elem2


def main():
    """ operational function """
    print("initializing list of size 10")
    quick_union = QuickUnion(10)
    print("connecting 1 and 2")
    quick_union.union(1, 2)
    print("connecting 3 and 4")
    quick_union.union(3, 4)
    print("connecting 0 and 5")
    quick_union.union(0, 5)
    print("connecting 5 and 6")
    quick_union.union(5, 6)
    print("connecting 2 and 7")
    quick_union.union(2, 7)
    print("connecting 8 and 3")
    quick_union.union(8, 3)
    print("is 8 and 9 connected?", quick_union.connected(8, 9))
    print("connecting 9 and 4")
    quick_union.union(9, 4)
    print("is 8 and 9 connected?", quick_union.connected(8, 9))


if __name__ == '__main__':
    main()
