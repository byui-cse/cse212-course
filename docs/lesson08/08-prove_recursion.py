"""
CSE212 
(c) BYU-Idaho
08-Prove - Problems

It is a violation of BYU-Idaho Honor Code to post or share this code with others or 
to post it online.  Storage into a personal and private repository (e.g. private
GitHub repository, unshared Google Drive folder) is acceptable.
"""

#############
# Problem 1 #
#############

def sum_recursive(n):
    """
    Using recursion, find the sum of 1 + 2 + 3 + ... + n
    and return it.
    """
    pass

# Sample Test Cases (may not be comprehensive)
print(sum_recursive(10))  # 55
print(sum_recursive(100)) # 5050

#############
# Problem 2 #
#############

def fibonacci(n, remember = dict()):
    """
    Using recursion, the n'th fibonacci number
    is found.  The formula for a fibonacci number
    is fib(n) = fib(n-1) + fib(n-2) where the first
    two fib numbers are fib(1) = 1 and fib(2) = 1.

    In this algorithm, a dictionary ('remember') is used
    to keep track of previously determine fibonacci
    numbers.  Without this dictionary, you would not
    be able to go much past the 40th fibonacci number
    """
    pass

print(fibonacci(1))    # 1
print(fibonacci(2))    # 1
print(fibonacci(3))    # 2
print(fibonacci(4))    # 3
print(fibonacci(10))   # 55
print(fibonacci(100))  # 354224848179261915075 (This one will
                       # not work if you don't have the 
                       # 'remember' dictionary implemented).


#############
# Problem 3 #
#############

def find(sorted_list, target):
    """
    Searches for a 'target' in a 'sorted_list'.  The base case
    is when the size of the list is 1 (we just have to compare
    the 'target' to the one item in the 'sorted_list').

    The algorithm uses recursion to look in the first half or the
    second half of the list based on comparing the value in the middle
    of the 'sorted_list' with the desired 'target'.
    """
    if len(sorted_list) == 1:  
        # Base Case
        return sorted_list[0] == target
    else:
        # Find the middle and compare
        middle = len(sorted_list) // 2
        if target == sorted_list[middle]:
            # We got lucky and the middle was the match
            return True
        elif target < sorted_list[middle]:
            # ADD YOUR CODE HERE
            pass
        else:
            # ADD YOUR CODE HERE
            pass

# Sample test cases (may not be comprehensive)
print(find([1, 3, 6, 18, 20, 25, 34, 38, 89, 95, 99, 100], 89)) # True
print(find([1, 3, 6, 18, 20, 25, 34, 38, 89, 95, 99, 100], 1))  # True
print(find([1, 3, 6, 18, 20, 25, 34, 38, 89, 95, 99, 100], 17)) # False

#############
# Problem 4 #
#############

def count_steps(s):
    """
    Using recursion, determine how many different ways to climb 
    's' stairs.  When climbing, the person can only take 1 step, 
    2 steps, or 3 steps at a time.  The person must land on the top
    stair exactly.  You should assume that if there are no stairs 
    (the invalid case) then the number of ways to climb would be 0.
    """
    pass

# Sample Test Cases (may not be comprehensive)
print(count_steps(5))   # 13
print(count_steps(20))  # 121415


#############
# Problem 5 #
#############

def wildcard_binary(pattern):
    """
    Using recursion, display all valid binary numbers (only
    contains 0's and 1's) based on a pattern that conatins
    zero or more *'s.  A * represents either a 0 or a 1.  For 
    example, 1* would result is 10 and 11.

    The pattern is a string (str).  The use of the find and replace 
    functions in Python may be useful to solve this problem.
    """
    pass

# Sample Test Cases (may not be comprehensive)
wildcard_binary("110*0*")
# 110000
# 110001
# 110100
# 110101
wildcard_binary("***")
# 000   
# 001   
# 010
# 011
# 100
# 101
# 110
# 111


