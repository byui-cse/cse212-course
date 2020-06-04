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
    and return it.  Remember to both express the solution 
    in terms of recursive call on a smaller problem and 
    to identify a base case (terminating case).  
    A loop should not be used.
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
    Implement an improved version of the fibonacci
    function using recursion and a dictionary to 
    remember previously calculated Fibonacci values.  
    Without the dictionary, the recursive version 
    of the Fibonacci algorithm would not be able 
    to calculate the 100th Fibonacci number in 
    your life time.  The Fibonacci algorithm is 
    defined as fib(n) = fib(n-1) + fib(n-2) 
    where fib(1) and fib(2) are equal to 1.  
    You can assume that the value of n will be 
    an integer greater than 0.
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
    Finish the find function which will 
    search for a target value in a sorted list in O(log n) 
    time.  This is achievable by comparing the middle 
    item in the list with the target value.  If the 
    middle item is less than the target, then you can 
    exclude the first half of the list (because the 
    list is already sorted).  Likewise, if the middle 
    item is greater than the target, then you can exclude 
    the second half of the list.  Use recursion to 
    appropriately call the find function 
    resulting in the ability to determine if the target 
    value is in the list.  You will likely need 
    to use list slicing to complete this problem:
    
    data[:a] - Creates a new list from index 0 to index a-1
    data[a:] - Creates a new list from index a to len(data)-1
    data[a:b] - Creates a new list from index a to index b-1
    data[a:b:c] - Creates a new list from index a to index b-1 stepping by c
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

def count_ways_to_climb(s):
    """
    Imagine that there was a staircase with s stairs.  
    We want to count how many ways there are to climb 
    the stairs.  If the person could only climb one 
    stair at a time, then the total would be just one.  
    However, if the person could choose to climb either 
    one, two, or three stairs at a time (in any order), 
    then the total possibilities become much more 
    complicated.  If there were just three stairs, 
    the possible ways to climb would be four as follows:
    
        1 step, 1 step, 1 step
        1 step, 2 step
        2 step, 1 step
        3 step

	Using recursion, determine how many ways there are 
    to climb s stairs.  Note that the problem requires 
    that the person land on the top stair.  For example, 
    if you are on the second to last stair, you can do 
    a 1 step but not a 2 or 3 step.  You should assume 
    that if there are no stairs, then the number of ways 
    to climb would be 0.
    """
    pass

# Sample Test Cases (may not be comprehensive)
print(count_ways_to_climb(5))   # 13
print(count_ways_to_climb(20))  # 121415


#############
# Problem 5 #
#############

def wildcard_binary(pattern):
    """
    A binary string is a string consisting of 
    just 1's and 0's.  For example, 1010111 is 
    a binary string.  If we introduce a wildcard 
    symbol * into the string, we can say that 
    this is now a pattern for multiple binary 
    strings.  For example, 101*1 could be used 
    to represent 10101 and 10111.  A pattern can
    have more than one * wildcard.  For example, 
    1**1 would result in 4 different binary 
    strings: 1001, 1011, 1101, and 1111.</p>
	
    Using recursion, display all possible binary 
    strings for a given pattern.  You might find 
    some of the Python str functions like find 
    and replace to be useful in solving this problem.
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


