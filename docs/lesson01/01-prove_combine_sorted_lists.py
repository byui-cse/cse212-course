"""
CSE212 
(c) BYU-Idaho
01-Prove - Problem 2

It is a violation of BYU-Idaho Honor Code to post or share this code with others or 
to post it online.  Storage into a personal and private repository (e.g. private
GitHub repository, unshared Google Drive folder) is acceptable.
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
    pass

l1 = [1, 2, 5, 6, 8]
l2 = [3, 4, 7, 9, 10]
print(combine_sorted_lists(l1,l2)) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

l1 = [1, 2, 10]
l2 = [3, 4, 5, 6, 7]
print(combine_sorted_lists(l1,l2)) # [1, 2, 3, 4, 5, 6, 7, 10]