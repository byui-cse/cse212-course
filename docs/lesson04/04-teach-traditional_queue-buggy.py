class Queue:
    """
    Maintain a Queue using a List
    """

    def __init__(self):
        """
        Initialize the empty queue using a Python List.  
        """
        self.queue = []

    def enqueue(self, value):
        """
        Enqueue the value provided into the queue
        """
        self.queue.insert(0, value)

    def dequeue(self):
        """
        Dequeue the next value and return it
        """
        if len(self.queue) < 0:
            raise IndexError()
        value = self.queue[1]
        del self.queue[1]
        return value

# Test Cases

# Test 1
# Scenario: Can I enqueue a value and dequeue it?
# Exepcted Result: It should display 100
queue = Queue()
queue.enqueue(100)
value = queue.dequeue()
print(value)
# Defect Found: This finds that the dequeue should be removing [0] instead of [1]

print("=================")

# Test 2
# Scenario: Can I enqueue multiple values and dequeue them in order?  
# Exepcted Result: It should display 200, then 300, then 400 in that order
queue = Queue()
queue.enqueue(200)
queue.enqueue(300)
queue.enqueue(400)
value = queue.dequeue()
print(value)
value = queue.dequeue()
print(value)
value = queue.dequeue()
print(value)
# Defect Found: This finds that the enqueue should use append instead of insert (which resulted in a stack)

print("=================")

# Test 3
# Scenario: Can I dequeue from an empty queue
# Exepcted Result: An exception should be raised
try:
    queue.dequeue()
    print("Oops ... This shouldn't have worked.")
except IndexError:
    print("I got the exception as expected.")
# Defect Found: None :)



