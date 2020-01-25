""" Implementation of Singly Linked List Data Structure """


class Node:
    """ Node class contains everything related to Linked List node """

    def __init__(self, data):
        """ initializing single node with data """
        self.data = data
        self.next = None

    def __repr__(self):
        return f"Node: data={self.data}"

    def get_data(self):
        """ Return the self.data attribute. """
        return self.data

    def set_data(self, new_data):
        """ Replace the existing value of the self.data attribute with
        new_data parameter.
        """
        self.data = new_data

    def get_next(self):
        """ Return the self.next attribute. """
        return self.next

    def set_next(self, new_next):
        """ Replace the existing value of the self.next attribute with
        new_next parameter.
        """
        self.next = new_next


class SinglyLinkedList:
    """ Singly Linked List is a linear data structure.
    Unlike arrays, linked list elements are not stored at a contiguous
    location; the elements are linked using pointers.
    """

    def __init__(self):
        """ initializing singly linked list with zero node """
        self.head = None
        self.tail = None
        self.length = 0

    def __len__(self):
        """returns the number of nodes currently present in linked list """
        return self.length

    def __repr__(self):
        return f"SinglyLinkedList: head={self.head}"

    def get_head(self):
        """ returns the first linked list node """
        return self.head

    def get_tail(self):
        """ returns the last linked list node """
        return self.tail

    def is_empty(self):
        """ Returns True if the Linked List is empty. Otherwise, return False.
        """
        return self.length == 0

    def insert_head(self, node):
        """ inserts node at the start of linked list """

    def insert_tail(self, node):
        """ inserts node at the end of linked list """

    def insert_at(self, node, position):
        """ inserts node at specified position in linked list """

    def delete_head(self):
        """ removes first linked list node and returns data. Returns None,
        if linkedlist is empty
        """

    def delete_tail(self):
        """ removes last linked list node and returns data. Returns None,
        if linkedlist is empty
        """

    def delete_at(self):
        """ removes specified node from linked list and returns data.
        Returns None, if position is invalid.
        """

    def data_at(self, position):
        """ returns node data without removing it.
        Returns None, if position is invalid.
        """

    def reverse_iterative(self):
        """ reverse original linked list using iterative approach """

    def reverse_recursive(self):
        """ reverse original linked list using recursive approach """

    def print_list(self):
        """ prints entire linked list without changing underlying data """

    def print_reverse_recursive(self):
        """ prints entire linked list in reverse order without
        changing underlying data. It uses recursive approach.
        """

    def print_recursive(self):
        """prints entire linked list without changing underlying data.
        It uses recursive approach.
        """


def main():
    """ operation function """


if __name__ == "__main__":
    main()
