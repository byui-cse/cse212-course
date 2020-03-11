class LinkedList:

    class Node:

        def __init__(self, data):
            self.data = data
            self.next = None
            self.prev = None

    def __init__(self):
        self.head = None
        self.tail = None

    def insert_head(self, value):
        new_node = LinkedList.Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert_tail(self, value):
        new_node = LinkedList.Node(value)
        if self.head is None:  # Can also check .tail
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def remove_head(self):
        if self.head == self.tail:
            self.head = None
            self.tail = None
        elif self.head is not None:
            self.head.next.prev = None
            self.head = self.head.next

    def remove_tail(self):
        if self.head == self.tail:
            self.head = None
            self.tail = None
        elif self.tail is not None:
            self.tail.prev.next = None
            self.tail = self.tail.prev

    def insert_after(self, value, new_value):
        curr = self.head
        while curr is not None:
            if curr.data == value:
                if curr == self.tail:
                    self.insert_tail(new_value)
                else:
                    new_node = LinkedList.Node(new_value)
                    new_node.prev = curr
                    new_node.next = curr.next
                    curr.next.prev = new_node
                    curr.next = new_node
                return
            curr = curr.next

    def remove(self, value):
        curr = self.head
        while curr is not None:
            if curr.data == value:
                if curr == self.head:
                    self.remove_head()
                elif curr == self.tail:
                    self.remove_tail()
                else:
                    curr.next.prev = curr.prev
                    curr.prev.next = curr.next
                return
            curr = curr.next

    def replace(self, old_value, new_value):
        curr = self.head
        while curr is not None:
            if curr.data == old_value:
                curr.data = new_value
            curr = curr.next

    def __iter__(self):
        curr = self.head
        while curr is not None:
            yield curr.data
            curr = curr.next

    def __reversed__(self):
        curr = self.tail
        while curr is not None:
            yield curr.data
            curr = curr.prev

    def __str__(self):
        output = "linkedlist["
        first = True
        for value in self:
            if first:
                first = False
            else:
                output += ", "
            output += str(value)
        output += "]"
        return output

    



ll = LinkedList()
ll.insert_head(1)
ll.insert_head(2)
ll.insert_head(2)
ll.insert_head(3)
ll.insert_head(4)
ll.insert_head(5)
print(ll)
ll.insert_tail(0)
ll.insert_tail(-1)
print(ll)
ll.insert_after(3, 3.5)
ll.insert_after(5, 6)
print(ll)
ll.remove(-1)
print(ll)
ll.remove(3)
print(ll)
ll.remove(6)
print(ll)
print(list(reversed(ll)))
ll.replace(2, 10)
print(ll)
