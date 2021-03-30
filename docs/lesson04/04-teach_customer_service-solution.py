"""
CSE212 
(c) BYU-Idaho
04-Teach - Problem 2 - Solution

It is a violation of BYU-Idaho Honor Code to post or share this code with others or 
to post it online.  Storage into a personal and private repository (e.g. private
GitHub repository, unshared Google Drive folder) is acceptable.
"""

class Customer_Service:
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
        queue is defined by parameter passed in by the user.  If the size is 
        invalid (less than or equal to 0) then the size will default to 10.
        """
        self.queue = []
        if max_size <= 0:
            self.max_size = 10  # Default value if max size is invalid
        else:
            self.max_size = max_size

    def add_new_customer(self):
        """
        Prompt the user for the customer and problem information.  Put the 
        new record into the queue.
        """
        # Verify there is room in the service queue
        #if len(self.queue) > self.max_size:    # Defect 3 - Should use >=
        if len(self.queue) >= self.max_size:
            print("Maximum Number of Customers in Queue.")
            return

        name = input("Customer Name: ")
        account_id = input("Account Id: ")
        problem = input("Problem: ")

        # Create the customer object and add it to the queue
        customer = Customer_Service.Customer(name, account_id, problem)
        self.queue.append(customer)

    def serve_customer(self):
        """
        Dequeue the next customer and display the information.
        """
        # Need to check to make sure there are customers in the queue
        if len(self.queue) == 0:      # Defect 2 - Need to check queue length
            print("No Customers in the Queue")
        else:
            # Need to read and save the customer before it is deleted
            # from the queue
            customer = self.queue[0]
            del self.queue[0]         # Defect 1 - Delete should be done after 
            print(customer)

    def __str__(self):
        """ 
        Suppport the str() function to provide a string representation of the
        customer service queue.  This is useful for debugging.  If you have a 
        Customer_Service object called cs, then you run print(cs) to see the 
        contents.
        """
        result = "[size=" + str(len(self.queue)) + " max_size=" + str(self.max_size) +" => "
        for customer in self.queue:
            result += "{"+str(customer)+"}"  # Uses the __str__ from Customer class
            result += ", "
        result += "]"
        return result

# Test Cases

# Test 1
# Scenario: Can I add one customer and then serve the customer?
# Expected Result: This should display the customer that was added
print("Test 1")
service = Customer_Service(4)
service.add_new_customer()
service.serve_customer()  
# Defect(s) Found: This found that the serve_customer should get the customer before deleting from the list

print("=================")

# Test 2
# Scenario: Can I add two customers and then serve the customers in the right order?
# Expected Result: This should display the customers in the same order that they were entered
print("Test 2")
service = Customer_Service(4)
service.add_new_customer()
service.add_new_customer()
print("Before serving customers: ",service)
service.serve_customer()
service.serve_customer()
print("After serving customers: ",service)
# Defect(s) Found: None :)

print("=================")

# Test 3
# Scenario: Can I serve a customer if there is no customer?
# Expected Result: This should display some error message
print("Test 3")
service = Customer_Service(4)
service.serve_customer()
# Defect(s) Found: This found that I need to check the length in serve_customer and display an error message

print("=================")

# Test 4
# Scenario: Does the max queue size get enforced?
# Expected Result: This should display some error message when the 5th one is added
print("Test 4")
service = Customer_Service(4)
service.add_new_customer()
service.add_new_customer()
service.add_new_customer()
service.add_new_customer()
service.add_new_customer()
print("Service Queue: ", service)
# Defect(s) Found: This found that I need to do >= instead of > in add_new_customer

print("=================")

# Test 5
# Scenario: Does the max size get defaulted to 10 if an invalid value is provided?
# Expected Result: It should display 10
print("Test 5")
service = Customer_Service(0)
print(service.max_size)
# Defect(s) Found: None :)


