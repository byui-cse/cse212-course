"""
CSE212 
(c) BYU-Idaho
01-Teach - Problem 2

It is a violation of BYU-Idaho Honor Code to post or share this code with others or 
to post it online.  Storage into a personal and private repository (e.g. private
GitHub repository, unshared Google Drive folder) is acceptable.
"""

def list_selector(list1, list2, selector):
    """
    The list1 and list2 inputs will be combined into a single
    list.  The order in which they are added is determined by 
    the selector list.  The selector list will only contain
    the values 1 or 2.  A value of 1 means to select the next
    value from list 1.  A value of 2 means to select the next 
    value from list 2.  It is assumed that the selector list
    will not contain any invalid values and it is also assumed
    that the sizes of list1 and list2 agree with the selector 
    list.
    """
    pass

l1 = [1, 2, 3, 4, 5]
l2 = [2, 4, 6, 8, 10]
select = [1, 1, 1, 2, 2, 1, 2, 2, 2, 1]
print(list_selector(l1, l2, select))  # [1, 2, 3, 2, 4, 4, 6, 8, 10, 5]

l1 = ['A', 'A', 'A', 'A', 'A']
l2 = ['B', 'B', 'B', 'B', 'B']
select = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2]
print(list_selector(l1, l2, select))  # ['A', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'B', ]