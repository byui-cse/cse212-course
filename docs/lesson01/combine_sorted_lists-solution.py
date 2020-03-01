"""
CSE212 
(c) BYU-Idaho
01-Prove - Problem 2 - Solution

It is a violation of BYU-Idaho Honor Code to post or share this code with others or 
to post it online.  

This solution should not be shared with students.
"""

def combine_sorted_lists(list1, list2):
    """
    Assume that both list1 and list2 are sorted.  Combine
    the lists together into a new list such that the numbers
    are sorted.  The new list should be returned.
    Neither the sort nor the sorted Python functions
    should be used.  Assume no duplicated numbers in within
    the two lists or between the two lists.
    """
    list1_pos = 0
    list2_pos = 0
    result = []
    # In this while loop, we will select the smallest number
    # from each list and add it to the result list.  Since
    # list1 and list2 are already sorted, we know where the
    # smallest number is in each list (using list1_pos and
    # list2_pos).  Keep doing this until we run out of 
    # numbers in one of the list.
    while list1_pos < len(list1) and list2_pos < len(list2):
        if list1[list1_pos] < list2[list2_pos]:
            # List1 has the next smallest number
            result.append(list1[list1_pos])
            list1_pos += 1
        elif list1[list1_pos] > list2[list2_pos]:
            # List2 has the next smallest number
            result.append(list2[list2_pos])
            list2_pos += 1
    
    # If we have run out of numbers in one the lists, the 
    # we should just add the remaining numbers in the other list.
    # Again, we can do this because the lists are already sorted.
    
    # Copy all the remaining numbers (if they exist) from list1
    while list1_pos < len(list1):
        result.append(list1[list1_pos])
        list1_pos += 1

    # Copy all the remaining numbers (if they exist) from list2
    while list2_pos < len(list2):
        result.append(list2[list2_pos])
        list2_pos += 1

    """
    The above two while loops could also have been written 
    using list slicing as follows:

    if list1_pos < len(list1):
        result += list1[list1_pos:]
    
    if list2_pos < len(list2):
        result += list2[list2_pos:]        
    """

    return result

l1 = [1, 2, 5, 6, 8]
l2 = [3, 4, 7, 9, 10]
print(combine_sorted_lists(l1,l2)) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

l1 = [1, 2, 10]
l2 = [3, 4, 5, 6, 7]
print(combine_sorted_lists(l1,l2)) # [1, 2, 3, 4, 5, 6, 7, 10]