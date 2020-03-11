import networkx

class BST:

    class Node:

        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = BST.Node(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, node):
        if data < node.data:
            if node.left is None:
                node.left = BST.Node(data)
            else:
                self._insert(data, node.left)
        elif data > node.data:
            if node.right is None:
                node.right = BST.Node(data)
            else:
                self._insert(data, node.right)

    def _contains(self, data, node):
        if data == node.data:
            return True
        elif data < node.data:
            if node.left is None:
                return False
            else:
                return self._contains(data, node.left)
        else:
            if node.right is None:
                return False
            else:
                return self._contains(data, node.right)
            
    def __in__(self, data):
        self.contains(data, self.root)

    def _traverse_forward(self, node):
        if node is not None:
            yield from self._traverse_forward(node.left)
            yield node.data
            yield from self._traverse_forward(node.right)
        
    def __iter__(self):
        yield from self._traverse_forward(self.root)

    def _traverse_backward(self, node):
        if node is not None:
            yield from self._traverse_backward(node.right)
            yield node.data
            yield from self._traverse_backward(node.left)

    def __reversed__(self):
        yield from self._traverse_backward(self.root)

    def _get_height(self, node):
        if node is None:
            return 0
        else:
            return 1 + max(self._get_height(node.left), self._get_height(node.right))

    def get_height(self):
        if self.root is None:
            return 0
        else:
            return self._get_height(self.root)


def _insert_middle(sorted_list, first, last, bst):
    if first > last:
        return
    middle = (last - first) // 2 + first
    bst.insert(sorted_list[middle])
    _insert_middle(sorted_list, first, middle-1, bst)
    _insert_middle(sorted_list, middle+1, last, bst)

def create_bst_from_sorted_list(sorted_list):
    bst = BST()
    _insert_middle(sorted_list, 0, len(sorted_list)-1, bst)
    return bst

tree = BST()
tree.insert(5)
tree.insert(3)
tree.insert(7)
tree.insert(10)
tree.insert(1)
print(3 in tree) # True
print(4 in tree) # False
for x in tree:
    print(x)  # 1, 3, 5, 7, 10
for x in reversed(tree):
    print(x)  # 10, 7, 5, 3, 1
print(tree.get_height()) # 3

tree2 = create_bst_from_sorted_list([x for x in range(127)])
tree3 = create_bst_from_sorted_list([x for x in range(128)])
print(tree2.get_height()) # 7
print(tree3.get_height()) # 8

# Modify the BST class so that no duplicate values
# can be added.  This will make the BST a Set (but with
# O(log n) instead of O(1) ... but now the values in the
# Set are sorted).

tree4 = BST()
tree4.insert(3)
tree4.insert(2)
tree4.insert(1)
for x in tree4:
    print(x) # 1, 2, 3
tree4.insert(2) 
for x in tree4: # Before the change: 1, 2, 2, 3
    print(x)    # After the change: 1, 2, 3


