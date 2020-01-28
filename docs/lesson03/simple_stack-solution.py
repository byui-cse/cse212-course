"""
CSE212 
(c) BYU-Idaho
03-Teach - Problem 1 - Solution

It is a violation of BYU-Idaho Honor Code to post or share this code with others or 
to post it online.  Storage into a personal and private repository (e.g. private
GitHub repository, unshared Google Drive folder) is acceptable.
"""

stack = []          # []
stack.append(1)     # [1]      
stack.append(2)     # [1, 2]   
stack.append(3)     # [1, 2, 3]
stack.pop()         # [1, 2]   
stack.pop()		    # [1]      
stack.append(4)		# [1, 4]   
stack.append(5)		# [1, 4, 5]
stack.pop()		    # [1, 4]
stack.append(6)		# [1, 4, 6]
stack.append(7)		# [1, 4, 6, 7]
stack.append(8)		# [1, 4, 6, 7, 8]
stack.append(9)		# [1, 4, 6, 7, 8, 9]
stack.pop()		    # [1, 4, 6, 7, 8]
stack.pop()		    # [1, 4, 6, 7]
stack.append(10)	# [1, 4, 6, 7, 10]
stack.pop()		    # [1, 4, 6, 7]
stack.pop()		    # [1, 4, 6]
stack.pop()		    # [1, 4]
stack.append(11)	# [1, 4, 11]
stack.append(12)	# [1, 4, 11, 12]
stack.pop()		    # [1, 4, 11]
stack.pop()		    # [1, 4]
stack.pop()		    # [1]
stack.append(13)	# [1, 13]
stack.append(14)	# [1, 13, 14]
stack.append(15)	# [1, 13, 14, 15]
stack.append(16)	# [1, 13, 14, 15, 16]
stack.pop()		    # [1, 13, 14, 15]
stack.pop()		    # [1, 13, 14]
stack.pop()		    # [1, 13]
stack.append(17)	# [1, 13, 17]
stack.append(18)	# [1, 13, 17, 18]
stack.pop()		    # [1, 13, 17]
stack.append(19)	# [1, 13, 17, 19]
stack.append(20)	# [1, 13, 17, 19, 20]
stack.pop()		    # [1, 13, 17, 19]
stack.pop()		    # [1, 13, 17]
print(stack)        # It will print [1, 13, 17]
