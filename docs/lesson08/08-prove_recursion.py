"""
CSE212 
(c) BYU-Idaho
08-Prove - Solutions

It is a violation of BYU-Idaho Honor Code to post or share this code with others or 
to post it online.  

This solution should not be shared with students.
"""

#############
# Problem 1 #
#############

def sum_squares_recursive(n):
    """
    Using recursion, find the sum of 1^2 + 2^2 + 3^2 + ... + n^2
    and return it.  Remember to both express the solution 
    in terms of recursive call on a smaller problem and 
    to identify a base case (terminating case).  If the value of
    n <= 0, just return 0.   A loop should not be used.
    """
    pass

# Sample Test Cases (may not be comprehensive) 
print("\n=========== PROBLEM 1 TESTS ===========")
print(sum_squares_recursive(10))  # 385
print(sum_squares_recursive(100)) # 338350

#############
# Problem 2 #
#############

def permutations_choose(letters, size, word=""):
    """
    Using recursion print permutations of length
    'size' from a list of 'letters'.  This function
    should assume that each letter is unique (i.e. the 
    function does not need to find unique permutations).

    In mathematics, we can calculate the number of permutations
    using the formula: len(letters)! / (len(letters) - size)!

    For example, if letters was [A,B,C] and size was 2 then
    the following would display: AB, AC, BA, BC, CA, CB (might be in 
    a different order).

    You can assume that the size specified is always valid (between 1 
    and the length of the letters list).
    """
    pass

# Sample Test Cases (may not be comprehensive) 
print("\n=========== PROBLEM 2 TESTS ===========")
permutations_choose(list("ABCD"),3)
"""
Expected Result (order may be different):
ABC
ABD
ACB
ACD
ADB
ADC
BAC
BAD
BCA
BCD
BDA
BDC
CAB
CAD
CBA
CBD
CDA
CDB
DAB
DAC
DBA
DBC
DCA
DCB
"""

print("---------")
permutations_choose(list("ABCD"),2)  
"""
Expected Result (order may be different):
AB
AC
AD
BA
BC
BD
CA
CB
CD
DA
DB
DC
"""

print("---------")         
permutations_choose(list("ABCD"),1)
"""
Expected Result (order may be different):
A
B
C
D
"""

#############
# Problem 3 #
#############

def count_ways_to_climb(s, remember = None):
    """
    Imagine that there was a staircase with 's' stairs.  
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

	With just one step to go, the ways to get
    to the top of 's' stairs is to either:
    
    - take a single step from the second to last step, 
    - take a double step from the third to last step, 
    - take a triple step from the fourth to last step

    We don't need to think about scenarios like taking two 
    single steps from the third to last step because this
    is already part of the first scenario (taking a single
    step from the second to last step).

    These final leaps give us a sum:

    count_ways_to_climb(s) = count_ways_to_climb(s-1) + 
                             count_ways_to_climb(s-2) +
                             count_ways_to_climb(s-3)

    To run this function for larger values of 's', you will need
    to update this function to use memoization.  The parameter
    'remember' has already been added as an input parameter to 
    the function for you to complete this task.
    
    The last test case is commented out because it will not work
    until the memoization is implemented.
    """
    # Base Cases
    if s == 0:
        return 0
    elif s == 1:
        return 1
    elif s == 2:
        return 2
    elif s == 3:
        return 4

    # Solve using recursion
    else:
        ways = count_ways_to_climb(s-1) + count_ways_to_climb(s-2) + count_ways_to_climb(s-3)
        return ways

# Sample Test Cases (may not be comprehensive) 
print("\n=========== PROBLEM 3 TESTS ===========")
print(count_ways_to_climb(5))   # 13
print(count_ways_to_climb(20))  # 121415
# Uncomment out the test below after implementing memoization.  It won't work without it.
#print(count_ways_to_climb(100))  # 180396380815100901214157639

#############
# Problem 4 #
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
print("\n=========== PROBLEM 4 TESTS ===========")
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

#############
# Problem 5 #
#############

"""
A maze is defined as a list of lists.  The outer list
contains a representation of each row in the maze.  You can
assume that the maze will be square (same number of rows
and columns). The inner lists show what is in the maze:

0 = Wall (You can't go through this)
1 = Open Path (You can go through this)
2 = End (You want to get to this point to win)

See the Prove instructions for graphical representations of
the 2 test mazes defined below.

The 'is_end_maze' and the 'is_valid_move' functions are
already written for you.  These functions assume that the first
square in the maze is (0,0).  These functions also assume
that you can't leave the boundaries of the maze and that you 
can't visit the same square in the same path (no circles).

The 'curr_path' variable is a list of (x,y) tuples that 
represent the path we are currently on.  If you add a new position
to the path, make sure that you add the tuple to the list so that the
'is_valid_move' function works properly.

The goal is to implement the 'solve_maze' function to display
all paths to the end square using recursion.  When you find a path, 
then displaying will be as simple as 'print(curr_path)'.
"""

def is_end_maze(maze, x, y):
    """
    Helper function to determine if the (x,y) position is at 
    the end of the maze.
    """
    return maze[y][x] == 2

def is_valid_move(maze, curr_path, x, y):
    """
    Helper function to determine if the (x,y) position is a valid
    place to move given the size of the maze, the content of the maze,
    and the current path already traversed.
    """
    # Can't go outside of the maze boundary (assume maze is a square)
    if x > len(maze)-1 or x < 0:
        return False
    if y > len(maze)-1 or y < 0:
        return False
    # Can't go if there is something in the way
    if maze[y][x] not in (1,2):
        return False
    # Can't go if we have already been there (don't go in circles)
    if (x,y) in curr_path:
        return False
    # Otherwise, we are good
    return True

def solve_maze(maze, x=0, y=0, curr_path=None):
    """
    Use recursion to print all paths that start at (0,0) and end at the
    'end' square.
    """

    # If this is the first time running the function, then we need
    # to initialize the curr_path list.
    if curr_path is None:
        curr_path = []

    # ADD CODE HERE    


# Sample Test Cases (may not be comprehensive) 
print("\n=========== PROBLEM 5 TESTS ===========")
small_maze = [[1,1,1],[1,0,1],[1,1,2]]
solve_maze(small_maze)
"""
Two Solutions (order in each solution should match):
[(0, 0), (0, 1), (0, 2), (1, 2), (2, 2)]
[(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)]
"""

big_maze = [[1,0,1,1,0,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0],
[1,1,1,1,0,1,0,0,0,0,1,0,1,1,1,1,1,1,1,1],
[1,0,0,0,0,1,0,0,0,0,1,0,1,0,0,1,0,1,0,1],
[1,1,1,1,0,1,1,1,1,0,1,0,1,0,0,1,0,1,0,1],
[0,0,0,1,0,1,0,0,0,0,1,0,1,0,0,0,0,1,0,0],
[0,0,0,1,0,1,0,0,0,0,1,0,1,1,1,1,0,1,1,1],
[1,1,1,1,0,1,0,0,1,1,1,0,0,0,0,1,0,0,0,1],
[0,1,0,1,0,1,0,0,1,0,1,0,1,1,1,1,0,1,1,1],
[0,1,0,1,0,1,0,1,1,0,1,0,0,0,0,1,0,0,0,1],
[1,1,0,0,0,1,0,1,0,0,1,0,1,1,1,1,0,1,1,1],
[0,1,1,1,1,1,0,1,0,0,1,0,1,0,0,0,0,0,0,1],
[0,1,0,0,0,0,0,1,0,0,1,0,1,0,1,0,0,0,0,1],
[0,1,0,0,0,0,0,1,0,0,1,0,1,0,1,1,1,1,1,1],
[0,1,0,0,0,1,1,1,0,0,1,0,1,0,0,0,1,0,0,1],
[1,1,0,1,0,1,0,0,0,0,1,0,1,0,1,1,1,0,0,0],
[0,1,0,1,0,1,0,1,0,0,1,0,1,0,1,0,1,1,1,0],
[0,1,1,1,0,1,0,1,0,0,1,0,1,0,0,0,0,0,1,1],
[0,1,0,0,0,1,0,1,1,1,1,0,1,1,1,0,0,1,1,0],
[0,1,0,0,0,1,0,0,0,0,0,0,1,0,1,0,0,0,1,0],
[1,1,1,1,0,1,1,1,1,1,1,1,1,0,1,1,0,0,1,2]]
solve_maze(big_maze)
"""
One Solution (order should match):
[(0, 0), (0, 1), (0, 2), (0, 3), (1, 3), (2, 3), (3, 3), (3, 4), (3, 5), (3, 6), (2, 6), 
(1, 6), (1, 7), (1, 8), (1, 9), (1, 10), (2, 10), (3, 10), (4, 10), (5, 10), (5, 9), (5, 8), 
(5, 7), (5, 6), (5, 5), (5, 4), (5, 3), (5, 2), (5, 1), (5, 0), (6, 0), (7, 0), (8, 0), 
(9, 0), (10, 0), (10, 1), (10, 2), (10, 3), (10, 4), (10, 5), (10, 6), (9, 6), (8, 6), 
(8, 7), (8, 8), (7, 8), (7, 9), (7, 10), (7, 11), (7, 12), (7, 13), (6, 13), (5, 13), (5, 14), 
(5, 15), (5, 16), (5, 17), (5, 18), (5, 19), (6, 19), (7, 19), (8, 19), (9, 19), (10, 19), 
(11, 19), (12, 19), (12, 18), (12, 17), (12, 16), (12, 15), (12, 14), (12, 13), (12, 12), 
(12, 11), (12, 10), (12, 9), (13, 9), (14, 9), (15, 9), (15, 8), (15, 7), (15, 6), (15, 5), (14, 5), 
(13, 5), (12, 5), (12, 4), (12, 3), (12, 2), (12, 1), (13, 1), (14, 1), (15, 1), (16, 1), 
(17, 1), (17, 2), (17, 3), (17, 4), (17, 5), (18, 5), (19, 5), (19, 6), (19, 7), (19, 8), 
(19, 9), (19, 10), (19, 11), (19, 12), (18, 12), (17, 12), (16, 12), (16, 13), (16, 14), (16, 15), 
(17, 15), (18, 15), (18, 16), (18, 17), (18, 18), (18, 19), (19, 19)]
"""


