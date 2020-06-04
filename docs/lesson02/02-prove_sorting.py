"""
CSE212 
(c) BYU-Idaho
02-Prove - Problem 1.1

It is a violation of BYU-Idaho Honor Code to post or share this code with others or 
to post it online.  Storage into a personal and private repository (e.g. private
GitHub repository, unshared Google Drive folder) is acceptable.
"""

def sort_list(data):
    for sort_pos in range(len(data)-1, 0, -1):
        max_swap_pos = 0
        for swap_pos in range(1, sort_pos+1):
            if data[swap_pos] > data[max_swap_pos]:
                max_swap_pos = swap_pos
        data[max_swap_pos], data[sort_pos] = data[sort_pos], data[max_swap_pos]

numbers = [3,2,1,6,4,9,8]
sort_list(numbers)
print(numbers)  #[1, 2, 3, 4, 6, 8, 9]