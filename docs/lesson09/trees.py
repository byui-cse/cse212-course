"""
CSE212 
(c) BYU-Idaho
08-Prove - Problems

It is a violation of BYU-Idaho Honor Code to post or share this code with others or 
to post it online.  Storage into a personal and private repository (e.g. private
GitHub repository, unshared Google Drive folder) is acceptable.
"""

class BST:
    """
    Implement the Binary Search Tree (BST) data structure.  The Node 
    class below is an inner class.  An inner class means that its real 
    name is related to the outer class.  To create a Node object, we will 
    need to specify BST.Node
    """

    class Node:
        """
        Each node of the BST will have data and links to the 
        left and right sub-tree. 
        """

        def __init__(self, data):
            """ 
            Initialize the node to the data provided.  Initially
            the links are unknown so they are set to None.
            """
       
            self.data = data
            self.left = None
            self.right = None

    def __init__(self):
        """
        Initialize an empty BST.
        """
        self.root = None

    def insert(self, data):
        """
        Insert 'data' into the BST.  If the BST
        is empty, then set the root equal to the new 
        node.  Otherwise, use _insert to recursively
        find the location to insert.
        """
        if self.root is None:
            self.root = BST.Node(data)
        else:
            self._insert(data, self.root)  # Start at the root

    #############
    # Problem 1 #
    #############
    def _insert(self, data, node):
        """
        This function will look for a place to insert a node
        with 'data' inside of it.  The current sub-tree is
        represented by 'node'.  This function is intended to be
        called the first time by the insert function.
        """
        if data < node.data:
            # The data belongs on the left side.
            if node.left is None:
                # We found an empty spot
                node.left = BST.Node(data)
            else:
                # Need to keep looking.  Call _insert
                # recursively on the left sub-tree.
                self._insert(data, node.left)
        elif data >= node.data:
            # The data belongs on the right side.
            if node.right is None:
                # We found an empty spot
                node.right = BST.Node(data)
            else:
                # Need to keep looking.  Call _insert
                # recursively on the right sub-tree.
                self._insert(data, node.right)


    def __in__(self, data):
        """ 
        Checks if data is in the BST.  This function
        supports the ability to use the 'in' keyword:

        if 5 in my_bst:
            ("5 is in the bst")

        """
        return self._contains(data, self.root)  # Start at the root

    #############
    # Problem 2 #
    #############
    def _contains(self, data, node):
        """
        This funciton will search for a node that contains
        'data'.  The current sub-tree being search is 
        represented by 'node'.  This function is intended
        to be called the first time by the __in__ function.
        """
        pass

    def __iter__(self):
        """
        Perform a formward traversal (in order traversal) starting from 
        the root of the BST.  This function is called when a loop
        is performed:

        for value in my_bst:
            print(value)

        """
        yield from self._traverse_forward(self.root)  # Start at the root
        
    def _traverse_forward(self, node):
        """
        Does a forward traversal (in-order traversal) through the 
        BST.  If the node that we are given (which is the current
        sub-tree) exists, then we will keep traversing on the left
        side (thus getting the smaller numbers first), then we will 
        provide the data in the current node, and finally we will 
        traverse on the right side (thus getting the larger numbers last).

        The use of the 'yield' will allow this function to support loops
        like:

        for value in my_bst:
            print(value)

        The keyword 'yield' will return the value for the 'for' loop to
        use.  When the 'for' loop wants to get the next value, the code in
        this function will start back up where the last 'yield' returned a 
        value.  The keyword 'yield from' is used when we want to 'yield' a
        value that is returned from a function.

        This function is intended to be called the first time by 
        the __iter__ function.
        """
        if node is not None:
            yield from self._traverse_forward(node.left)
            yield node.data
            yield from self._traverse_forward(node.right)
        
    def __reversed__(self):
        """
        Perform a formward traversal (in order traversal) starting from 
        the root of the BST.  This function is called when a the 
        reversed function is called and is frequently used with a for
        loop.

        for value in reversed(my_bst):
            print(value)

        """        
        yield from self._traverse_backward(self.root)  # Start at the root

    #############
    # Problem 3 #
    #############
    def _traverse_backward(self, node):
        """
        Does a backwards traversal (reverse in-order traversal) through the 
        BST.  If the node that we are given (which is the current
        sub-tree) exists, then we will keep traversing on the right
        side (thus getting the larger numbers first), then we will 
        provide the data in the current node, and finally we will 
        traverse on the left side (thus getting the smaller numbers last).

        This function is intended to be called the first time by 
        the __reversed__ function.        
        """
        pass

    def get_height(self):
        """
        Determine the height of the BST.  If the tree is empty, then
        return 0.  Otherwise, call _get_height on the root which will
        recursively determine the height of the tree.
        """
        if self.root is None:
            return 0
        else:
            return self._get_height(self.root)  # Start at the root

    #############
    # Problem 4 #
    #############
    def _get_height(self, node):
        """
        Determine the height of the BST.  The height of a sub-tree 
        (represented by 'node') is 1 plus the height of either the 
        left sub-tree or the right sub-tree (whichever one is bigger).

        This function intended to be called the first time by 
        get_height.
        """
        pass

# NOTE: Functions below are not part of the BST class above. 

def create_bst_from_sorted_list(sorted_list):
    """
    Given a sorted list (sorted_list), create a balanced BST.  If 
    the values in the sorted_list were inserted in order from left
    to right into the BST, then it would resemble a linked list.  To
    get a balanced BST, the _insert_middle function is called to 
    find the middle item in the list to add first to the BST.  The 
    _insert_middle function takes the whole list but also takes a 
    range (first to last) to consider.  For the first call, the full 
    range of 0 to len()-1 used.
    """
    bst = BST()  # Create an empty BST to start with 
    _insert_middle(sorted_list, 0, len(sorted_list)-1, bst)
    return bst

#############
# Problem 5 #
#############
def _insert_middle(sorted_list, first, last, bst):
    """
    This function will attempt to insert the item in the middle
    of 'sorted_list' into the 'bst' tree.  The middle is 
    determined by using indicies represented by 'first' and 'last'.
    For example, if the function was called on:

    sorted_list = [10, 20, 30, 40, 50, 60]
    first = 0
    last = 5

    then the value 30 (index 2) would be added to the 'bst' 
    (the insert function above can be used to do this).  

    After adding the middle, the middle of the first half of the list 
    (defined by start = 0 and last = 1) and the middle of the second 
    half of the list (defined by start = 3 and last = 5) must be added to 
    the bst. This will result in a balanced tree if this is recursively 
    done until there are no more values to insert.

    This function is intended to be called the first time by 
    create_bst_from_sorted_list.
    """
    pass

# Sample Test Cases (You may need to add more)
tree = BST()
tree.insert(5)
tree.insert(3)
tree.insert(7)
tree.insert(7)  # After implementing 'no duplicates' rule,
                # this insert will have no effect on the tree.
tree.insert(10)
tree.insert(1)
print(3 in tree) # True
print(4 in tree) # False
for x in tree:
    print(x)  # 1, 3, 5, 7, 10
for x in reversed(tree):
    print(x)  # 10, 7, 5, 3, 1
print(tree.get_height()) # 3

tree2 = create_bst_from_sorted_list([x for x in range(127)]) # 2^7 - 1
tree3 = create_bst_from_sorted_list([x for x in range(128)]) # 2^7
print(tree2.get_height()) # 7 .. any higher and its not balanced
print(tree3.get_height()) # 8 .. any higher and its not balanced



