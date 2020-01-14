"""
CSE212 
(c) BYU-Idaho
04-Teach - Problem 2 - Solution

It is a violation of BYU-Idaho Honor Code to post or share this code with others or 
to post it online.  Storage into a personal and private repository (e.g. private
GitHub repository, unshared Google Drive folder) is acceptable.
"""

class CustomerService:
    """
    Maintain a Customer Service Queue.  Allows new customers to be 
    added and allows customers to be serviced.
    """

    class Customer:
        """
        Defines a Customer record for the service queue.
        This is an inner class.  Its real name is CustomerService.Customer
        """

        def __init__(self, name, account_id, problem):
            """
            Initialize the Customer Record
            """
            self.name = name
            self.account_id = account_id
            self.problem = problem

        def __str__(self):
            """
            Return a string representing the record so we can print it out later
            """
            return self.name + " (" + self.account_id + ") : " + self.problem

    def __init__(self, max_size):
        """
        Initialize the empty queue using a Python List.  The maximum size of the 
        queue is defined by parameter passed in by the user.
        """
        self.queue = []
        self.max_size = max_size

    def add_new_customer(self):
        """
        Prompt the user for the customer and problem information.  Put the 
        new record into the queue.
        """
        # Verify there is room in the service queue
        if len(self.queue) >= self.max_size:
            print("Maximum Number of Customers in Queue.")
            return

        name = input("Customer Name: ")
        account_id = input("Account Id: ")
        problem = input("Problem: ")

        # Create the customer object and add it to the queue
        customer = CustomerService.Customer(name, account_id, problem)
        self.queue.append(customer)

    def serve_customer(self):
        """
        Dequeue the next customer and display the information.
        """
        # Need to check to make sure there are customers in the queue
        if len(self.queue) == 0:
            print("No Customers in the Queue")
        else:
            # Need to read and save the customer before it is deleted
            # from the queue
            customer = self.queue[0]
            del self.queue[0]
            print(customer)

# Test Cases

# Test 1
# Scenario: Can I add one customer and then serve the customer?
# Expected Result: This should display the customer that was added
service = CustomerService(4)
service.add_new_customer()
service.serve_customer()  
# Defect Found: This found that the serve_customer should get the customer before deleting from the list

print("=================")

# Test 2
# Scenario: Can I add two customers and then serve the customers in the right order?
# Expected Result: This should display the customers in the same order that they were entered
service.add_new_customer()
service.add_new_customer()
service.serve_customer()
service.serve_customer()
# Defect Found: None :)

print("=================")

# Test 3
# Scenario: Can I serve a customer if there is no customer?
# Expected Result: This should display some error message
service.serve_customer()
# Defect Found: This found that I need to check the length in serve_customer and display an error message

print("=================")

# Test 4
# Scenario: Does the max queue size get enforced?
# Expected Result: This should display some error message when the 5th one is added
service.add_new_customer()
service.add_new_customer()
service.add_new_customer()
service.add_new_customer()
service.add_new_customer()
# Defect Found: This found that I need to do >= instead of > in add_new_customer


