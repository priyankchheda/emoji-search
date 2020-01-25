""" Implementation for Stack Data Structure """


class Stack:
    """ A stack is an abstract data type that serves as a collection of
    elements with two principal operations: push() and pop(). push() adds an
    element to the top of the stack, and pop() removes an element from the top
    of a stack. The order in which elements come off of a stack are
    Last In, First Out (LIFO).
    https://en.wikipedia.org/wiki/Stack_(abstract_data_type)
    """

    def __init__(self):
        """ Initializing empty stack."""
        self._items = []

    def push(self, item):
        """ Accepts an item as a parameter and appends it to the end of the
        list. Returns nothing.

        The runtime for this method is o(1), or constant time, because
        appending to the end of a list happens in constant time.

        :param item: item to be inserted on top of stack
        """
        self._items.append(item)

    def pop(self):
        """ Returns and removes the last item for the list, which is also the
        top item of the stack.

        The runtime here is constant time, because all it does is index to the
        last item of the list.

        :return: return top item of the stack or None, if stack is empty
        """
        if self._items:
            return self._items.pop()
        return None

    def peek(self):
        """  This method returns the last item in the list, which is also the
        item at the top of the Stack.

        This method runs in constant time because indexing into a list is done
        in constant time.

        :return: returns top of the stack or None, if stack is empty
        """
        if self._items:
            return self._items[-1]
        return None

    def size(self):
        """ This method returns the length of the list that is representing
        the stack.

        This method runs in constant time because finding the length of a list
        also in constant time.

        :return: length of list
        :rtype: int
        """
        return len(self._items)

    def is_empty(self):
        """ This method returns a boolean value describing whether or not the
        stack is empty.

        Runs in constant time, because testing for equality happens in
        constant time.

        :return: returns true if stack is empty, else false
        """
        return self._items == []


def main():
    """ operational function """
    stack = Stack()
    print("stack is empty: ", stack.is_empty())
    print("stack size: ", stack.size())
    for i in range(5):
        stack.push(i)

    print("after inserting 5 elements")
    print("stack is empty: ", stack.is_empty())
    print("stack size: ", stack.size())

    print("top element on stack: ", stack.peek())
    print("popped element from stack: ", stack.pop())
    print()
    print("after popping one elements")
    print("stack size: ", stack.size())
    print("top element on stack: ", stack.peek())


if __name__ == "__main__":
    main()
