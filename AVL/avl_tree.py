""" AVL Tree Implementation in Python

AVL tree is a self-balancing Binary Search Tree (BST) where the difference
between heights of left and right subtrees cannot be more than one for
all nodes.
"""

class Node:
    """ Node contains actual data and address to left and right node """
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    """ AVL Tree Implementation """
    def __init__(self):
        self.root = None

    def insert(self, key):
        """ inserts new integer data into the tree at the position, so that
            the AVL tree property is maintained.
        """
        def _insert(root, key):
            """ recursive internal method which works on node level """
            if root is None:
                return Node(key)

            if key < root.data:
                root.left = _insert(root.left, key)
            else:
                root.right = _insert(root.right, key)

            root.height = max(self.get_height(root.left),
                              self.get_height(root.right)) + 1

            balance_factor = self.get_balance_factor(root)

            # if node is unbalanced
            # case 1 - left left
            if balance_factor > 1 and key < root.left.data:
                return self.right_rotate(root)

            # case 2 - right right
            if balance_factor < -1 and key > root.right.data:
                return self.left_rotate(root)

            # case 3 - left right
            if balance_factor > 1 and key > root.left.data:
                root.left = self.left_rotate(root.left)
                return self.right_rotate(root)

            # case 4 - right left
            if balance_factor < -1 and key < root.right.data:
                root.right = self.right_rotate(root.right)
                return self.left_rotate(root)

            return root

        self.root = _insert(self.root, key)

    def right_rotate(self, node):
        """ perform right rotation on given node """
        left_node = node.left
        subtree = left_node.right

        # perform rotation
        left_node.right = node
        node.left = subtree

        node.height = max(self.get_height(node.left),
                          self.get_height(node.right)) + 1
        left_node.height = max(self.get_height(left_node.left),
                               self.get_height(left_node.right)) + 1
        return left_node

    def left_rotate(self, node):
        """ perform left rotation on given node """
        right_node = node.right
        subtree = right_node.left

        # perform rotation
        right_node.left = node
        node.right = subtree

        node.height = max(self.get_height(node.left),
                          self.get_height(node.right)) + 1
        right_node.height = max(self.get_height(right_node.left),
                                self.get_height(right_node.right)) + 1
        return right_node

    def get_height(self, node):
        """ returns height of node """
        if node is None:
            return 0

        return node.height

    def get_balance_factor(self, node):
        """ returns balance factor at node """
        if node is None:
            return 0

        return self.get_height(node.left) - self.get_height(node.right)


def pre_order(node):
    """ prints pre order traversal """
    if node is None:
        return

    print(node.data, end=" ")
    pre_order(node.left)
    pre_order(node.right)


def main():
    """ operational function """
    avl_tree = AVLTree()
    avl_tree.insert(10)
    avl_tree.insert(20)
    avl_tree.insert(30)
    avl_tree.insert(40)
    avl_tree.insert(50)
    avl_tree.insert(25)

    pre_order(avl_tree.root) # 30 20 10 25 40 50
    print()


if __name__ == "__main__":
    main()
