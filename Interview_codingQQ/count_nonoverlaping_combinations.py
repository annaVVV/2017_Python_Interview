###
# An artist is creating a collage out of newspaper of cut - outs.
# There is a long string of text from nespaper, where
# interesting substrings have been marked to cut out. Only two
# interesting positions of the text are needed, and the rest of the
# collage will be made of images. The two chosen interesting
# positions in the text should not overlap with each other. How
# many choices are there.

# Example:
# textLength = 10
# starting = [1, 1, 6, 7]
# ending = [5, 3, 8, 10]

# 1 2 3 4 5 6 7 8 9 10
# |_______|             1 to 5
# |____|                1 to 3
#           |____|      6 to 8
#             |_______| 7 to 10

# The interesting substrings go from starting[i] to ending[i].
#  A par can be chosen only if they do not overlap. If substrings
#  match exactly, discard all but 1 before counting choices

# The following combinations can be chosen:

# 1 and 3
# 1 and 4
# 2 and 3
# 2 and 4

# There are 4 ways to choose two non-overlaping interesting positions

# Function Description

# Complete the function paperCuttings in the editoe:
# paperCuttings has following paramethers:
# int textLength: the lenth of the newspaper text
# int starting: the strating points positions of the ith interesting positions
# int ending: the ending points positions of the ith interesting positions
# Returns:
# int: the number of ways to obtain two non-overlapping interesting positions in the text

# Constrains
# 1<= textLength <= 10**9
# 1<= n <= 10**5
# 1<= starting[i] <= endinging[i] <= n

# Input Format for Custom testing
# The 1st line contains an integer textLength the lenth of the newspaper text
# The 2nd line contains an integer n n, the number of interesting positions in the text
# Each line i in n subsequent lines (where 0<= i < n) contains an integer starting[i]
# The next line contains an integer n n, the number of interesting positions in the text
# Each line i in n subsequent lines (where 0<= i < n) contains an integer ending[i]

# Sample Case 0
# Input     Function
# -------------------
# 10 ->    textLength
# 5  ->    starting[] size n=5
# 3  -> starting = [3, 1, 2, 8, 8]
# 1
# 2
# 8
# 8
# 5  ->    ending[] size n=5
# 5  -> ending = [5, 3, 7, 10, 10]
# 3
# 7
# 10
# 10
# Sample outpot: 3

# Sample Case 1
# textLength = 8
# n=5
# starting = [3, 4, 5, 6, 8]
# ending = [4, 5, 6, 7, 18]
# Sample outpot: 7 choices
